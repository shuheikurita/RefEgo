# RefEgo-MDETR

MDETR implementation for RefEgo: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D.

[RefEgo dataset](https://github.com/shuheikurita/RefEgo) [[Paper](https://arxiv.org/abs/2308.12035)]

## Get Started

### Environment
**OS**
- Ubuntu 20.04 LTS
**Software**
- Docker
- CUDA > 11.2

```
$ export DATADIR=path\to\data
# build docker image
$ make build
# run docker container
$ make run
```

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
