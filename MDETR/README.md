# RefEgo-MDETR

MDETR implementation for RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D.

## Get Started

### Environment
**Prerequirements**
- Docker
- CUDA > 11.2

We prepare a Makefile for docker build and run.
```
# Specify the data directory for training/validation of RefEgo
# For inference-only purpose, you can specify an empty dir.
$ export DATADIR=path\to\data

# Build docker image
$ make build

# Run docker container
$ make run
```

### Get Model and try!
You can get the off-the-shelf model of MDETR binary-head. Place the fintuned model
```sh
wget -P checkpoints/refego_mdetr_binary_scratch.pth http://a000.amtvirtual.net/refego/checkpoints/refego_mdetr_binary_scratch.pth
```
and [demo](MDETR/MDETR_BH_inference.ipynb).

### Data directory tree structure
```
data
├── models
│   └── refcoco_EB3_checkpoint.pth
└── refego
    ├── annotations
    │   ├── test.json
    │   ├── train.json
    │   └── val.json
    └── images
        ├── 000786a7-3f9d-4fe6-bfb3-045b368f7d44--643-10
        │   ├── img0000000643.jpg
        │   ├── img0000000644.jpg
        │   ├── img0000000645.jpg
        │   ├── img0000000646.jpg
        │   ├── img0000000647.jpg
```

### Training MDETR on Ref-Egocentric
```
$ make train_conventional
$ make train_all
$ make train_binary_head
```

## Acknowledgement
Thanks for the open-source MDETR
* [MDETR: Modulated Detection for End-to-End Multi-Modal Understanding, Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel Synnaeve, Ishan Misra, Nicolas Carion](https://github.com/ashkamath/mdetr)
