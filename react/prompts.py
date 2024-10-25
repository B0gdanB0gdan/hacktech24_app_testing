

def get_system_prompt(tools):

    tool_description = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
    tool_names = ", ".join([tool.name for tool in tools])
    return f"""
    You are an intelligent assistant capable of interacting with applications through specific commands. 
    You have access to the following tools, which you can use to perform actions:

    {tool_description}

    Use the following format:

    Query: The instruction you must follow.
    Thought: You should always think about what to do.
    Action: The action to take, should be one of [{tool_names}].
    Action Input: The input to the action. For example, the text to type or the coordinates to click.
    Observation: The result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer.
    Final Answer: The final answer to the original input question.

    """

def get_few_shot_prompt(examples, images):
    few_shots = []
    for example, image in zip(examples, images):
        few_shots.append({
            "role": "user", 
            "content": [{"type": "text", "text": example["user"]}]
        })
        few_shots.append({
            "role": "assistant",
            "content": [{
                "type": "text", 
                "text": example["assistant"]
            },
            {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image}", "detail": "high"}
            }]
        })
            
    return few_shots


def build_react_prompt(system_prompt, few_shot, query):
   
    return [
        {
            "role": "system", 
            "content": [{"type": "text", "text": system_prompt}]
        }
    ] + few_shot + [
        {
            "role": "user",
            "content": [{"type": "text", "text": "\nQuery: \n"+query}]
        }
    ]