# honeybee

```
# pytorch 2.0.1 환경
<!-- docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel -->
docker pull nvcr.io/nvidia/pytorch:23.05-py3

# container
docker run --gpus '"device=1,2"' -it --name honeybee -p 8007:8007 -v [경로]/workspace nvcr.io/nvidia/pytorch:23.10-py3
docker run -it --name honeybee nvcr.io/nvidia/pytorch:23.05-py3

# 패키지 설치
pip install --upgrade pip
pip install opencv-python==4.8.0.74
pip install -r requirements.txt


# server
uvicorn main:app --host "0.0.0.0" --port 8007 --reload
```
