# honeybee

```
# pytorch 2.0.1 환경
<<<<<<< Updated upstream
<!-- docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel -->
docker pull nvcr.io/nvidia/pytorch:23.10-py3

# container
docker run --gpus '"device=1,2"' -it --name honeybee -p 8007:8007 -v [경로]/workspace nvcr.io/nvidia/pytorch:23.10-py3
docker run -it --name honeybee nvcr.io/nvidia/pytorch:23.10-py3

# 패키지 설치
pip install --upgrade pip
pip install opencv-python==4.8.0.74
pip install -r requirements.txt

=======
docker pull pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# container
docker run --gpus '"device=1,2,3,4"' -it --name honeybee -v /home/jh/my_code/model-serving/honeybee:/workspace pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# 패키지 설치 (gradio, flash-attn==2.3.2 제외) -> flash-attn설치 필요?
pip install -r requirements.txt
pip install pandas

# opencv error
apt-get update -y
apt-get install -y libgl1-mesa-glx
apt-get install -y libglib2.0-0
>>>>>>> Stashed changes

# server
uvicorn main:app --host "0.0.0.0" --port 8007 --reload
```

<<<<<<< Updated upstream
- 2.0.1 환경에서 flash-attn 설치가 안됐음
- 두번째로 사용한 환경은 torch 2.1.0
- 두 환경 모두 에러가 완전히 해결되지는 않았지만 실행은 가능했다.
=======
- multi gpu
- png
- env
>>>>>>> Stashed changes
