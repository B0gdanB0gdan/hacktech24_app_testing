from utils import encode_image
import textwrap


def get_system_prompt(tools):

    tool_description = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
    tool_names = ", ".join([tool.name for tool in tools])
    return f"""
    You are an intelligent assistant capable of interacting with applications through specific commands. 
    You have access to the following tools, which you can use to perform actions:

    {tool_description}

    Use the following format:

    Query: The instruction you must follow. You start from this state described in the following image: [base64 encoded image] 
    Thought: You should always think about what to do.
    Action: The action to take, should be one of [{tool_names}].
    Action Input: The input to the action. For example, the text to type, the coordinates to click or the number to scrollHello World.
    Observation: The result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer.
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
                    "text": example["user"]["text"]
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
        for i in range(1, example["steps"]):
            step_base64 = encode_image(example["assistant"][f"step{i}"]["image_path"])
            few_shots.append({
                "role": "assistant",
                "content": [{
                    "type": "text", 
                    "text": textwrap.dedent(example["assistant"][f"step{i}"]["text"])
                },
                {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{step_base64}", "detail": "high"}
                }]
            })
        few_shots.append({
            "role": "assistant",
            "content": [{
                "type": "text", 
                "text": textwrap.dedent(example["assistant"][f"step{example['steps']}"]["text"])
            }]
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