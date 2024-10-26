from PIL import Image
from io import BytesIO
import base64


def pil_image_to_base64(image: Image.Image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    base64_string = base64.b64encode(image_bytes).decode('utf-8')    
    return base64_string


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')