from PIL import Image
from transformers import AutoModel, AutoTokenizer
from fastapi import FastAPI
from pydantic import BaseModel
import base64
import io

"""
# openai requests
response = requestDTO(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": "./data/test.png",
                },
            ],
        }
    ],
    max_tokens=300,
)

"""
app = FastAPI()


class requestDTO(BaseModel):
    model: str
    messages: list
    max_tokens: int


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode("utf-8")

    return img


model = AutoModel.from_pretrained(
    "openbmb/MiniCPM-Llama3-V-2_5-int4", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    "openbmb/MiniCPM-Llama3-V-2_5-int4", trust_remote_code=True
)
model.eval()


@app.post("/")
async def root(data: requestDTO):
    image = None
    image_url = [
        content["image_url"]
        for content in data.messages[0]["content"]
        if content["type"] == "image_url"
    ]
    question = [
        content["text"]
        for content in data.messages[0]["content"]
        if content["type"] == "text"
    ][0]
    msgs = [{"role": "user", "content": question}]

    base64_image = encode_image(image_url[0])
    imgdata = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(imgdata)).convert("RGB")

    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        temperature=0.7,
        sampling=True,
        stream=True,
    )

    generated_text = ""
    for new_text in res:
        generated_text += new_text
        print(new_text, flush=True, end="")

    return generated_text
