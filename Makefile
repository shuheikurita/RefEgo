TOKENIZERS_PARALLELISM=false
CUBLAS_WORKSPACE_CONFIG=:16:8

.PHONY: build
build:
	DOCKER_BUILDKIT=1 docker build -t ref-egocentric --build-arg UID=`id -u` .

.PHONY: run
run:
	docker run --rm -it --shm-size 32G --name refego --gpus all -v $(PWD):/opt/ml -v $(DATADIR)/:/opt/ml/data/refego  ref-egocentric:latest

.PHONY: train_conventional
train_conventional:
	python -m torch.distributed.launch --nproc_per_node=2 --use_env \
	main.py --dataset_config configs/refego.json --batch_size 4 \
	--backbone timm_tf_efficientnet_b3_ns \
	--output-dir ./logs/refego_mdetr_conventional \
	--ema \
	--num_workers 8 \
	--load ./data/models/refcoco_EB3_checkpoint.pth

.PHONY: train_all
train_all:
	python -m torch.distributed.launch --nproc_per_node=2 --use_env \
	main.py --dataset_config configs/refego.json --batch_size 4 \
	--backbone timm_tf_efficientnet_b3_ns \
	--output-dir ./logs/refego_mdetr_all \
	--ema \
	--num_workers 8 \
	--load ./data/models/refcoco_EB3_checkpoint.pth \
	--use_no_target

.PHONY: train_binary_head
train_binary_head:
	python -m torch.distributed.launch --nproc_per_node=2 --use_env \
	main.py --dataset_config configs/refego.json --batch_size 4 \
	--backbone timm_tf_efficientnet_b3_ns \
	--output-dir ./logs/refego_mdetr_binary \
	--ema \
	--num_workers 8 \
	--load ./data/models/refcoco_EB3_checkpoint.pth \
	--use_no_target \
	--binary_head
