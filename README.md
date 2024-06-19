# model-serving

```
docker build -t vllm-base -f Dockerfile .
```

# honeybee
```
# pytorch 2.0.1 환경
docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# container
docker run --gpus '"device=1,2,3,4"' -it --name honeybee -v /home/jh/my_code/model-serving/honeybee:/workspace pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# 패키지 설치 (gradio, flash-attn==2.3.2 제외) -> flash-attn설치 필요? no, png가 안됨.
pip install -r requirements.txt
pip install pandas

# opencv error
apt-get update -y
apt-get install -y libgl1-mesa-glx
apt-get install -y libglib2.0-0

# server
uvicorn main:app --host "0.0.0.0" --port 8007 --reload
```