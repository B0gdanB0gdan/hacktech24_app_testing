import pyautogui
from utils import pil_image_to_base64
from segm.segmentation import inference_sam_m2m_auto
from sam_model import ModelSingleton
from time import time


def make_screenshot():
    model = ModelSingleton().get_model()
    ss = pyautogui.screenshot()
    if ss.mode != 'RGB':
        ss = ss.convert('RGB')
    _, mappings, pil_image = inference_sam_m2m_auto(model, ss, dest_path=f'phase2/test_{time()}.png', anno_mode=['Mask','Mark'], save=True)
    return pil_image_to_base64(pil_image), mappings


def click(label, input, prev_lookup):
    try:
        coord = prev_lookup[int(label)]
    except:
        return make_screenshot()
    y, x = coord
    x = int(x)
    y = int(y)
    pyautogui.click(x, y)
    return make_screenshot()


def type_text(label, input, prev_lookup):
    pyautogui.write(input)
    return make_screenshot()


def scroll(label, input, prev_lookup):
    pyautogui.scroll(int(input))
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
            description="Click on label x."
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