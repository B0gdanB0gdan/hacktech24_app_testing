import pyautogui
from utils import pil_image_to_base64


def make_screenshot():
    return pil_image_to_base64(pyautogui.screenshot())


def click(coord):
    x, y = coord.split(", ")
    x = int(x.replace("(", ""))
    y = int(y.replace(")", ""))
    pyautogui.click(x, y)
    return make_screenshot()


def type_text(text):
    pyautogui.write(text)
    return make_screenshot()


def scroll(amount):
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
            func=lambda coord: click(coord),
            description="Click at screen position (x, y)."
        ),
        Tool(
            name="Type",
            func=lambda text: type_text(text),
            description="Type a string using the keyboard."
        ),
        Tool(
            name="Scroll",
            func=lambda amount: scroll(amount),
            description="Scroll the screen up or down by an amount."
        ),
    ]

def get_tool_by_name(name):
    tools = get_tools()
    for tool in tools:
        if tool.name == name:
            return tool