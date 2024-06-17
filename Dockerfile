FROM nvcr.io/nvidia/pytorch:23.10-py3

WORKDIR /workspace
RUN git clone https://github.com/vllm-project/vllm.git
WORKDIR /workspace/vllm

RUN pip install vllm
RUN pip install -e .