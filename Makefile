.PHONY: build
build:
	DOCKER_BUILDKIT=1 docker build -t ref-egocentric --build-arg UID=`id -u` .

.PHONY: run
run:
	docker run --rm -it --name refego --gpus all -v $(PWD):/opt/ml -v $(DATADIR)/:/opt/ml/data/refego  ref-egocentric:latest