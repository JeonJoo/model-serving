import os
from PIL import Image
import torch
from uuid import uuid4
from fastapi import FastAPI, File, UploadFile
from pipeline.interface import get_model


app = FastAPI()


def construct_input_prompt(user_prompt):
    SYSTEM_MESSAGE = "The following is a conversation between a curious human and AI assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    IMAGE_TOKEN = "Human: <image>\n"
    USER_PROMPT = f"Human: {user_prompt}\n"

    return SYSTEM_MESSAGE + IMAGE_TOKEN + USER_PROMPT + "AI: "


# Load trained model
ckpt_path = "checkpoints/7B-C-Abs-M144/last/"
model, tokenizer, processor = get_model(ckpt_path, use_bf16=True)
model.cuda("cuda")
print("Model initialization is done.")

model.eval()


@app.post("/honeybee-serving")
def honeybee_serving(
    files: list[UploadFile] = File(None), question: str = "explain the image"
):
    image_list = []
    if files is not None:
        for file in files:
            if file.filename is None:
                raise KeyError("filename is null")

            extension = file.filename.rsplit(".", 1)[1].lower()
            save_path = os.path.join(
                "images/",
                str(uuid4()) + "." + extension,
            )
            image_list.append(save_path)
            binary_image = file.file.read()

            with open(save_path, "wb") as f:
                f.write(binary_image)

    prompts = [construct_input_prompt(question)]

    images = [Image.open(_) for _ in image_list]
    inputs = processor(texts=prompts, images=images)
    inputs = {
        k: v.bfloat16() if v.dtype == torch.float else v for k, v in inputs.items()
    }
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    generate_kwargs = {"do_sample": True, "top_k": 5, "max_length": 512}

    with torch.no_grad():
        res = model.generate(**inputs, **generate_kwargs)
    sentence = tokenizer.batch_decode(res, skip_special_tokens=True)
    result = sentence[0]

    print(f"generated: {result}")

    return result
