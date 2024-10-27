import litellm
from utils import encode_image
from glob import glob
from dotenv import load_dotenv
load_dotenv("../.env")
from PIL import Image
from tools import inference_sam_m2m_auto
from sam_model import ModelSingleton
from time import time
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def convert(frame_dir):
    for i, frame_path in enumerate(glob(frame_dir)):
        model = ModelSingleton().get_model()
        im = Image.open(frame_path)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        inference_sam_m2m_auto(model, im, dest_path=f'./test_{i}.png', anno_mode=['Mask','Mark'], save=True)


def get_instruction_set(frame_dir):
    context = ""
    for i, frame_path in enumerate(glob(frame_dir)):
        base64_image = encode_image(frame_path)
        prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": 
"""
You are a helpful assistant that describes how a user operates an application. 
You will be provided a recording of the application frame by frame. 
Pay attention to what elements the user interacts with. 
When providing the description in each frame you must follow this structure:

1. Always mention the label of the element the user interacts with. For example "The user interacts with File menu item, save button, etc".
2. Shortly mention where the element is located.
3. Describe the action the user performs on the element. For example "The user clicks on the File menu item, types text in the input field, etc".
4. When it is the case also mention the input the user provides. For example "The user types 'Hello World' in the input field, scrolls 3 times, etc".
"""}]},
            {"role": "user",
                "content": [{"type": "text", "text": "Describe shortly with what elements the user interacts with in the next frame:"}, 
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "high"}}]},
        ]
        response = litellm.completion(model="gpt-4o",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=0.3).choices[0].message.content
        context += response
    
    prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": "You are a helpful assistant that describes how a user operates an application.\n"}]},
            {"role": "user",
                "content": [{"type": "text", "text": f"Summarize the elements the user interacted with using an instruction list based on the following context: \n {context}. Try to understand what the user wants and merge together steps when necessary or remove duplicate ones. \n Start:\n"}]},
        ]
    response = litellm.completion(model="gpt-4o",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=0.3).choices[0].message.content
    return response
       

if __name__ == '__main__':
    p = r"examples/example2/*"
    print(get_instruction_set(p))
    # convert(p)