import base64
from tools import get_tools, get_tool_by_name
from prompts import *
from few_shot import *
from glob import glob
import litellm
from dotenv import load_dotenv
load_dotenv("../.env")
import re 



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    

def truncate_obs(text, index):
    lines = text.strip().split("\n")
    modified_lines = []
    observation_count = 0
    i = 0

    while i < len(lines):
        if lines[i].startswith("Observation:"):
            if observation_count == index:
                modified_lines.append("Observation: ")
                break
            else:
                # Add the current observation
                modified_lines.append(lines[i])
                # Move to the next observation, skipping lines until an empty line is found
                while i < len(lines) and lines[i].strip():
                    i += 1
            observation_count += 1
        else:
            modified_lines.append(lines[i])
            i += 1
    
    return "\n".join(modified_lines)


class ReActExectutor:
    def __init__(self):
        self.system_prompt = get_system_prompt(get_tools())
        image_paths = glob("frames/*.png")[:4]
        images = [encode_image(image_path) for image_path in image_paths]
        self.few_shot_prompt = get_few_shot_prompt(examples, images)
        self.step = 0 
        self.new_obs_texts = []
        self.next_images = []

    def parse_output(self, output):
        actions = re.findall(r'Action:\s*(.*)', output)
        action_inputs = re.findall(r'Input:\s*(.*)', output)
        action2execute = actions[self.step]
        input2take = action_inputs[self.step]
        tool = get_tool_by_name(action2execute)
        
        next_image = tool.func(input2take)
        new_obs_text = truncate_obs(output, self.step)
        self.new_obs_texts.append(new_obs_text)
        self.next_images.append(next_image)
        self.step += 1

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
        action2execute = actions[self.step]
        return action2execute == "Finish"

    def execute(self, query):
        prompt = build_react_prompt(self.system_prompt, self.few_shot_prompt, query)
        finish = False
        while not finish:
            response = litellm.completion(model="gpt-4-turbo",
                                        messages=prompt,
                                        max_tokens=4096,
                                        temperature=1).choices[0].message.content
            finish = self.is_finished(response)
            prompt += self.parse_output(response)
            break 
        self.new_obs_texts = []
        self.next_images = []
        self.step = 0
        return response



if __name__ == "__main__":
    
    agent = ReActExectutor()
    agent.execute("Scroll up by 3 pages. and type 'Hello World' after clicking at coordinates (100, 200).")

