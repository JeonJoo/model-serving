from PIL import Image
import math


def calculate_image_token(image_path: str):
    image = Image.open(image_path)
    width, height = image.size
    max_length = max(width, height)

    if max_length <= 512:
        return "low", 85

    image_token = _calculate_token(width, height, max_length)

    return "high", image_token


def _calculate_token(width, height, max_length):
    if max_length > 2048:
        width, height = _resize_iamge(width, height, 2048, max_length)

    min_length = min(width, height)
    if min_length > 768:
        width, height = _resize_iamge(width, height, 768, min_length)

    w = math.ceil(width / 512)
    h = math.ceil(height / 512)
    return (w * h) * 170 + 85


def _resize_iamge(width, height, max_value, base_length):
    factor = max_value / base_length
    return round(width * factor), round(height * factor)
