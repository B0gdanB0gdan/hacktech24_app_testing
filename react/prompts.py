from utils import encode_image
import textwrap


def get_system_prompt(tools):

    tool_description = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
    tool_names = ", ".join([tool.name for tool in tools])
    return f"""
    You are an intelligent assistant capable of interacting with applications through specific commands. 
    You can see the application interface step by step in a series of frames.
    Each frame contains a set of labels (integers) overlapped to help you identify the elements to interact with.
    For example if you are thinking to interact with a menu item you need to find the closest label to that menu item.
    Always analyze what happened in the previous frame and if the interaction was not successful try again.
    You have access to the following tools, which you can use to perform actions:

    {tool_description}

    Use the following format:

    Query: The instruction you must follow. You will start from a state described in an image: [base64 encoded image] 
    Thought: You should always think about what to do and identify the label you need interact with from the last image .
    Label: The label value of the element to interact with. You should find this label next to the element to interact with in the last image.
    Action: The action to take, should be one of [{tool_names}].
    Input: The input to the action. For example, the text to type or the number to scroll. Button clicks do not require input so you can type \"None\".
    Observation: The result of the action
    ... (this Thought/Action/Input/Observation can repeat N times)
    Thought: Task is finished.
    Action: Finish

    """

def get_few_shot_prompt(examples):
    few_shots = []
    for example in examples:
        im = encode_image(example["user"]["image_path"])
        few_shots.append({
            "role": "user", 
            "content": [
                {
                    "type": "text", 
                    "text": example["user"]["text"] + "You start from this state described in the following image:"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{im}", 
                        "detail": "high"
                        }
                }
            ]
        })
        assistant_content = []
        for i in range(1, example["steps"]):
            step_base64 = encode_image(example["assistant"][f"step{i}"]["image_path"])
            assistant_content.extend([
                {
                    "type": "text", 
                    "text": textwrap.dedent(example["assistant"][f"step{i}"]["text"])
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{step_base64}", "detail": "high"}
                }
            ])
        assistant_content.append(
           {
                "type": "text", 
                "text": textwrap.dedent(example["assistant"][f"step{example['steps']}"]["text"])
            }
        )
        few_shots.append({
            "role": "assistant",
            "content": assistant_content
        })
 
    return few_shots


def build_react_prompt(system_prompt, few_shot, query, image_starting_point):
    return [
        {
            "role": "system", 
            "content": [{"type": "text", "text": system_prompt}]
        }
    ] + few_shot + [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "\nQuery: \n"+ query + "You start from this state described in the following image:"
                },
                {
                    "type": "image_url", 
                    "image_url": {"url": f"data:image/jpeg;base64,{image_starting_point}", "detail": "high"}
                }
            ]
        }
    ]