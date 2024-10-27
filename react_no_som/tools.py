import pyautogui
from utils import pil_image_to_base64
import sys
sys.path.append('../segmentation')
from PIL import Image

from time import time

def make_screenshot():
    # model = ModelSingleton().get_model()
    ss = pyautogui.screenshot()
    if ss.mode != 'RGB':
        ss = ss.convert('RGB')
    # im, coords, pil_image = inference_sam_m2m_auto(model, ss, dest_path=f'./test_{time()}.png', anno_mode=['Mask','Mark'], save=True)
    return pil_image_to_base64(ss), None
    # return pil_image_to_base64(pil_image), coords


import re

def extract_coordinates(text):
    match = re.search(r'\((\d+),\s*(\d+)\)', text)
    if match:
        x, y = int(match.group(1)), int(match.group(2))
        return x, y
    else:
        return None  # Returns None if no match is found

def click(label, prev_lookup):
    try:
        coords = label.split(', ')
        # coord = prev_lookup[int(label)]
        x,y = coords
        pyautogui.click(int(x), int(y))
    except:
        x,y=extract_coordinates(label)
        pyautogui.click(int(x), int(y))
    return make_screenshot()
    
    


def type_text(text, prev_lookup):
    pyautogui.write(text)
    return make_screenshot()


def scroll(amount, prev_lookup):
    pyautogui.scroll(int(amount))
    return make_screenshot()


class Tool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description
    

def get_tools():
    return [
        Tool(
            name="Click",
            func=click,
            description="Click on coordinates x, y."
        ),
        Tool(
            name="Type",
            func=type_text,
            description="Type a string using the keyboard."
        ),
        Tool(
            name="Scroll",
            func=scroll,
            description="Scroll the screen up or down by an amount."
        ),
    ]

def get_tool_by_name(name):
    tools = get_tools()
    for tool in tools:
        if tool.name == name:
            return tool