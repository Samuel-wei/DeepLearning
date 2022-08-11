# Copyright from Sharebee.cn Inc, All rights reserved
# Author: Samuel
# Date: June 27, 2021
# Reference: https://github.com/Samuel-wei/mediapipe/blob/master/Dockerfile

FROM nvcr.io/nvidia/l4t-tensorflow:r32.5.0-tf2.3-py3

MAINTAINER <samueltwei@163.com>

WORKDIR /home/workspace/DeepLearning/PythonDeepLearning

ENV DEBIAN_FRONTEND=noninteractive

# install setuptools and pip
# ARG setuptools=3.4.1
RUN mkdir /jupyternotebook/ && \
    wget https://files.pythonhosted.org/packages/88/fc/d17731c0cc67a5a8e385e4f47c3b0b186720e198b70f076ccb4676804a8f/setuptools-57.0.0.tar.gz && \
    tar -zxvf setuptools-57.0.0.tar.gz && \
    cd setuptools-57.0.0 && \
    python3 setup.py build  && \
    python3 setup.py install && \
	wget https://files.pythonhosted.org/packages/4d/0c/3b63fe024414a8a48661cf04f0993d4b2b8ef92daed45636474c018cd5b7/pip-21.1.3.tar.gz && \
	tar -zxvf pip-21.1.3.tar.gz && \
	python3 setup.py build && \
	python3 setup.py install && \
	pip3 -v && \
	rm -rf /jupyternotebook/

RUN apt-get update && apt-get install -y --no-install-recommends \
		unzip \
		vim \
		libffi-dev \
		python3-dev \
        python3-opencv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install wheel
RUN pip3 install Jupyter notebook 
RUN pip3 install keras


WORKDIR /dbdata/DeepLearning/PythonDeepLearning/

# RUN 
