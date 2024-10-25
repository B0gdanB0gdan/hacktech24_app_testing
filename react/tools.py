import pyautogui
from PIL import Image
from io import BytesIO
import base64

    
def pil_image_to_base64(image: Image.Image) -> str:
    # Create a BytesIO object to hold the image in memory
    buffered = BytesIO()
    
    # Save the PIL image to the BytesIO object in a specific format (e.g., PNG or JPEG)
    image.save(buffered, format="PNG")
    
    # Get the bytes value of the image
    image_bytes = buffered.getvalue()
    
    # Encode the image bytes to a base64 string
    base64_string = base64.b64encode(image_bytes).decode('utf-8')
    
    return base64_string

def click(coord):
    x, y = coord.split(", ")
    x = int(x.replace("(", ""))
    y = int(y.replace(")", ""))
    pyautogui.click(x, y)
    return pil_image_to_base64(pyautogui.screenshot())

def type_text(text):
    pyautogui.write(text)
    return pil_image_to_base64(pyautogui.screenshot())

def scroll(amount):
    pyautogui.scroll(int(amount))
    return pil_image_to_base64(pyautogui.screenshot())


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