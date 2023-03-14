from pathlib import Path

import torch
import torchvision

from transformers import RobertaTokenizerFast
from datasets.coco import ConvertCocoPolysToMask, make_coco_transforms

from scripts.utils.text import get_root_and_nouns

class RefEgoDataset(torchvision.datasets.CocoDetection):
    def __init__(self, img_folder, ann_file, transforms, return_masks, return_tokens, tokenizer, use_no_target=False):
        super().__init__(img_folder, ann_file)
        self._transforms = transforms # Augmentation, ToTensor, Normalize
        self.prepare = ConvertCocoPolysToMask(return_masks, return_tokens, tokenizer=tokenizer) # targetの生成

        if not use_no_target:
            # remove no referred object images
            print("Use only images that include the referred object.")
            self.ids = [id for id in self.ids if self.coco.loadAnns(self.coco.getAnnIds(id))[0]["is_obj_in"]]
        else:
            print("Use images that don't include the referred object.")
        
        # check the number of captions per image 
        caption = self.coco.loadImgs(self.ids[0])[0]["caption"]
        self.num_caption_per_img = len(caption) if isinstance(caption, list) else 1
        print(f"the number of captions per image : {self.num_caption_per_img}")

    def __len__(self):
        return len(self.ids) * self.num_caption_per_img

    def __getitem__(self, index):
        idx = index // self.num_caption_per_img

        img, target = super().__getitem__(idx)
        image_id = self.ids[idx]

        coco_img = self.coco.loadImgs(image_id)[0]
        caption = coco_img["caption"]
        caption = caption[index % self.num_caption_per_img]

        # NOTE: the number of RefEgocentric's target per image is single
        obj = target[0]
        obj["category_id"] = 0

        # create tokens positive mask
        tokens_positive = get_root_and_nouns(caption)[2]
        tokens_positive = list(map(list, tokens_positive))
        tokens_positive = sorted(tokens_positive, key=lambda x: x[0])
        
        obj["tokens_positive"] = tokens_positive
        obj["area"] = img.size[0] * img.size[1]
        answer = int(obj['is_obj_in'])
        
        target = [target[0]]

        dataset_name = coco_img["dataset_name"] if "dataset_name" in coco_img else None

        target = {"image_id": image_id, "annotations": target, "caption": caption}
        img, target = self.prepare(img, target)

        if self._transforms is not None:
            img, target = self._transforms(img, target)
        target["dataset_name"] = dataset_name
        
        
        for extra_key in ["sentence_id", "original_img_id", "original_id", "task_id"]:
            if extra_key in coco_img:
                target[extra_key] = coco_img[extra_key]

        if "tokens_positive_eval" in coco_img and not self.is_train:
            tokenized = self.prepare.tokenizer(caption, return_tensors="pt")
            target["positive_map_eval"] = create_positive_map(tokenized, coco_img["tokens_positive_eval"])
            target["nb_eval"] = len(target["positive_map_eval"])

        # answer binary
        target["answer_binary"] = torch.tensor(answer)
        target["answer_type"] = torch.tensor(0) # binary

        return img, target

def build(image_set, args):
    root = Path("/opt/ml/data/refego/")
    img_folder = root / "images"
    ann_file = root / f"dataset/{image_set}.json"

    tokenizer = RobertaTokenizerFast.from_pretrained(args.text_encoder_type)

    dataset = Ego4dDataset(
        img_folder,
        ann_file,
        transforms=make_coco_transforms(image_set, cautious=True),
        return_masks=args.masks,
        return_tokens=True,
        tokenizer=tokenizer,
        use_no_target=args.use_no_target,
    )

    return dataset
