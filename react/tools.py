import pyautogui
from utils import pil_image_to_base64
import sys
sys.path.append('../segmentation')
from segmentation import inference_sam_m2m_auto
from sam_model import ModelSingleton
from PIL import Image



def make_screenshot():
    model = ModelSingleton().get_model()
    ss = pyautogui.screenshot()
    if ss.mode != 'RGB':
        ss = ss.convert('RGB')
    _, sorted_anns, pil_image = inference_sam_m2m_auto(model, ss, dest_path='./test.png', anno_mode=['Mask','Mark'], save=True)
    mappings = {}
    for i in range(len(sorted_anns)):
        mappings[i+1] = sorted_anns[i]['point_coords'][0]
    return pil_image_to_base64(pil_image), mappings


def click(label, prev_lookup):
    print("label:",label)
    coord = prev_lookup[label]
    print(coord)
    x, y = coord.split(", ")
    x = int(x.replace("(", ""))
    y = int(y.replace(")", ""))
    pyautogui.click(x, y)
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