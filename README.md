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
export TOKENIZERS_PARALLELISM=false
export CUBLAS_WORKSPACE_CONFIG=:16:8

python -m torch.distributed.launch --nproc_per_node=2 --use_env \
main.py --dataset_config configs/ego4d.json --batch_size 4 \
--backbone timm_tf_efficientnet_b3_ns \
--output-dir ./logs/refego \
--ema \
--num_workers 8 \
--load ./data/pretrained/refcoco_EB3_checkpoint.pth
```

## Acknowledgement
Thanks for the open-source MDETR
* [MDETR: Modulated Detection for End-to-End Multi-Modal Understanding, Aishwarya Kamath, Mannat Singh, Yann LeCun, Gabriel Synnaeve, Ishan Misra, Nicolas Carion](https://github.com/ashkamath/mdetr)