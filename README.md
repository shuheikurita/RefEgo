# RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D

![RefEgo teaser](misc/refego_teaser.gif)

Dataset and codebase for the ICCV2023 paper RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D.

- Referring expression comprehension & object tracking dataset on Ego4D
- 12,038 annotated clips of 41 hours total. 
- 2FPS for annotation bboxes with two textual referring expressions for a single object.
- Objects can be out-of-frame of the first-person video (no-referred-object). 

[\[paper\]](https://arxiv.org/abs/2308.12035)[\[video\]](https://refegopublic.s3.amazonaws.com/refego.mp4)[\[code\]](https://github.com/shuheikurita/RefEgo)[\[RefEgo dataset\]](https://refegopublic.s3.amazonaws.com/RefEgoAnnotations.zip)

## Dataset
Annotations can be downloaded from [\[RefEgo dataset\]](https://refegopublic.s3.amazonaws.com/RefEgoAnnotations.zip).
See [dataset/README.md](dataset/README.md) for details.

## Model
MDETR-based models and checkpoints and are [here](MDETR/README.md). We also add a [notebook](MDETR/MDETR_BH_inference.ipynb) for trying our model!

## Leaderboard
Coming soon. 

## Dataset License
RefEgo dataset annotations (bounding boxes and texts) are distributed under CC BY-SA 4.0.
Please also follow Ego4D license for videos and images.

## Cite

```sh
@InProceedings{Kurita_2023_ICCV,
    author    = {Kurita, Shuhei and Katsura, Naoki and Onami, Eri},
    title     = {RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2023},
    pages     = {15214-15224}
}
```

## Acknowledgement
[Ego4D](https://ego4d-data.org/)
