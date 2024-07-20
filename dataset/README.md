# Annotation files

We use RefCOCO-compatible annotation files for MDETR training.

- dataset/refego_train_RefCOCOstyle_fps2.json
- dataset/refego_val_RefCOCOstyle_fps2.json
- dataset/refego_test_RefCOCOstyle_fps2.json
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

Requirement
- ffmpeg

We prepare two shell scripts for converting Ego4D videos into RefEgo images.
```sh
# Apply ffmpeg for Ego4D v1 videos.
bash extract_images.sh path_to_ego4d path_to_fps2_images (--cuda)

# Split images into RefEgo style video clips
bash split_video_clips.sh path_to_fps2_images path_to_extracted_fps2 
```

For exmaple, if you place Ego4D videos in `/data/ego4d/v1/full_scale/`, then
```sh
bash extract_images.sh /data/ego4d/v1/full_scale/ /data/ego4d_images
bash split_video_clips.sh /data/ego4d_images /data/refego/images
```

- `--cuda` is optional when `-hwaccel cuda` is available in ffmpeg.

# Clip ID

We introduce the unique "clip ID" for each extracted video clip:
`{Ego4D uid}--{the image number where the video clip starts (1-base)}-{length of images in the video clip}`
Clip ID is used to specify the range of video clips in annotation files.
