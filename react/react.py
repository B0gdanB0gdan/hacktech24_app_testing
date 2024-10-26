from tools import get_tools, get_tool_by_name, make_screenshot
from prompts import *
from few_shot import *
import litellm
from dotenv import load_dotenv
load_dotenv("../.env")
import re 


def truncate_obs(text, index):
    lines = text.strip().split("\n")
    modified_lines = []
    i, observation_count = 0, 0

    while i < len(lines):
        if lines[i].startswith("Observation:"):
            if observation_count == index:
                modified_lines.append("Observation: ")
                break
            else:
                modified_lines.append(lines[i])
                while i < len(lines) and lines[i].strip():
                    i += 1
            observation_count += 1
        else:
            modified_lines.append(lines[i])
            i += 1
    
    return "\n".join(modified_lines)


class ReActExectutor:
    def __init__(self, max_depth=3):
        self.system_prompt = get_system_prompt(get_tools())
        self.few_shot_prompt = get_few_shot_prompt(get_examples())
        self.new_obs_texts = []
        self.next_images = []
        self.max_depth = max_depth

    def parse_output(self, output):
        actions = re.findall(r'Action:\s*(.*)', output)
        action_inputs = re.findall(r'Input:\s*(.*)', output)
        action2execute = actions[0]
        input2take = action_inputs[0]
        tool = get_tool_by_name(action2execute)
        next_image = tool.func(input2take)
        new_obs_text = truncate_obs(output, 0)
        self.new_obs_texts.append(new_obs_text)
        self.next_images.append(next_image)

        new_response = []
        for new_obs_text, next_image in zip(self.new_obs_texts, self.next_images):
            new_response.append(
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": new_obs_text
                    },
                    {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{next_image}", "detail": "high"}
                    }
                ]
            })
        return new_response

    def is_finished(self, output):
        
        actions = re.findall(r'Action:\s*(.*)', output)
        action2execute = actions[0]
        return action2execute == "Finish" 
   
    def reset(self):
        self.step = 0
        self.new_obs_texts = []
        self.next_images = []

    def execute(self, query):
        start_point = make_screenshot()
        initial_prompt = build_react_prompt(self.system_prompt, self.few_shot_prompt, query, start_point)
        finish = False
        i = 0
        prompt = initial_prompt
        while not finish and i < self.max_depth:
            response = litellm.completion(model="gpt-4-turbo",
                                        messages=prompt,
                                        max_tokens=4096,
                                        temperature=1).choices[0].message.content
            
            finish = self.is_finished(response)
            prompt = initial_prompt + self.parse_output(response)
            i += 1 
        self.reset()
        return response



if __name__ == "__main__":
    
    agent = ReActExectutor()
    agent.execute("Notepad")