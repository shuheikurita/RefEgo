# Ref-Egocentric: Referring Expression Comprehension Dataset from First-Person Perception of Ego4D

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

### Training MDETR on Ref-Egocentric
```
$ make train_conventional
$ make train_all
$ make train_binary_head
```

## Acknowledgement
Thanks for the open-source MDETR
* [MDETR: Modulated Detection for End-to-End Multi-Modal Understanding, Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel Synnaeve, Ishan Misra, Nicolas Carion](https://github.com/ashkamath/mdetr)