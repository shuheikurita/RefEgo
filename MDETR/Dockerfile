FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04
LABEL maintainer=""

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV PYTHONUTF8=1

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    zip unzip \
    htop tree \
    wget curl \
    vim ssh tmux \
    libopencv-dev \
    build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev \
    libffi-dev \
    dpkg-dev \
    python3 python3-pip python3-dev \
    default-jre \
    ffmpeg
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

#ARG UID
#RUN useradd docker -l -u $UID -G sudo -s /bin/bash -m
#RUN echo 'Defaults visiblepw' >> /etc/sudoers
#RUN echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

#USER docker

ENV PYENV_ROOT /home/docker/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

ENV PYTHON_VERSION 3.8.6
RUN pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}

RUN pip install -U pip setuptools
RUN pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
ADD requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install pydantic==1.7.4 spacy==3.5.2 spacy-legacy==3.0.12 spacy-loggers==1.0.4 nltk
RUN pip install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI&egg=pycocotools
RUN python -m spacy download en_core_web_sm
RUN pip install timm==0.4.12

ENV TOKENIZERS_PARALLELISM false
ENV CUBLAS_WORKSPACE_CONFIG :4096:8
WORKDIR /opt/ml

ENTRYPOINT [ "/bin/bash" ]
