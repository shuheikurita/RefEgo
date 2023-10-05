# Annotation files

We use RefCOCO-compatible annotation files for MDETR training.

- dataset/refego_train_RefCOCOstyle_fps2.json
- dataset/refego_val_RefCOCOstyle_fps2.json

- dataset/refego_video_list.json : video list


Check `['annotation']` of json files:
```
'ref': referring expression patterns: [0,1]
'id': global_count
'bbox': bbox
'video_id': Ego4D uid
'clip_id': clip id
'img_id': img id
'img_clip_id': sequential image number (0-base)
'img_clip_length': length of images
"label" : object label
'is_obj_in': whether the target object in the image or not
'caption': referring expression
'stationary': is the object in motion in the video clip
'is_multi': are there multiple same type of objects or not
```

# Extract images from Ego4D

Use ffmpeg to extract images from Ego4D. This is an example of FPS-2 extracting:
```sh
ffmpeg -hwaccel cuda -i ego4d/v1/full_scale/{uid}.mp4 -vf "fps=2,scale=640:-1" -qscale 1 {outdir}/{video_id}/img%10d.jpg
```
- video_id: video ID of Ego4D.

# Clip ID

We introduce the unique "clip ID" for each extracted video clip:
`{Ego4D uid}--{the image number where the video clip starts (1-base)}-{length of images in the video clip}`
Clip ID is used to specify the range of video clips in annotation files.
