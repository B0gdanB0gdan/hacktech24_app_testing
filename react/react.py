from tools import get_tools, get_tool_by_name, make_screenshot
from prompts import *
from few_shot import *
from propose_instructions import get_instruction_set

import litellm
from dotenv import load_dotenv
load_dotenv("../.env")
import re 
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import json
from record import extract_frames_from_video


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
    def __init__(self, max_depth=10, phase2_fp="phase2"):
        self.system_prompt = get_system_prompt(get_tools())
        self.few_shot_prompt = get_few_shot_prompt(get_examples())
        self.new_obs_texts = []
        self.next_images = []
        self.max_depth = max_depth
        self.prev_lookup = None
        self.phase2_fp = phase2_fp

    def parse_output(self, output):
        actions = re.findall(r'Action:\s*(.*)', output)
        action_inputs = re.findall(r'Input:\s*(.*)', output)
        labels = re.findall(r'Label:\s*(.*)', output)
        label = labels[0]
        action2execute = actions[0]
        input2take = action_inputs[0]
        tool = get_tool_by_name(action2execute)
        next_image, lookup = tool.func(label, input2take, self.prev_lookup)
        self.prev_lookup = lookup
        new_obs_text = truncate_obs(output, 0)
        
        self.new_obs_texts.append(new_obs_text)
        self.next_images.append(next_image)

        with open("phase2/steps.txt", "a") as p2s:
            p2s.write(new_obs_text)

        print(new_obs_text)

        new_response = []
        assistant_content = []
        for new_obs_text, next_image in zip(self.new_obs_texts, self.next_images):
            assistant_content.extend([
                {
                    "type": "text",
                    "text": new_obs_text
                },
                {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{next_image}", "detail": "high"}
                }
            ])
        new_response = [{
            "role": "assistant",
            "content": assistant_content
        }]
        return new_response

    def is_finished(self, output):
        
        actions = re.findall(r'Action:\s*(.*)', output)
        action2execute = actions[0]
        return action2execute.strip() == "Finish" 
   
    def reset(self):
        self.step = 0
        self.new_obs_texts = []
        self.next_images = []

    def execute(self, query):
        start_point, lookup = make_screenshot()
        self.prev_lookup = lookup
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
            if not finish:
                prompt = initial_prompt + self.parse_output(response)
                with open("prompt.json", "w") as f:
                    json.dump(prompt, f, indent=4)
            i += 1 
        self.reset()
        return response



if __name__ == "__main__":
    # extract_frames_from_video("examples/rec_wordpad/wordpad_3.mkv", "examples/rec_wordpad_frames", skip_factor=60)

    logs = get_instruction_set("examples/rec_wordpad_frames/*")
    with open("phase1.txt", "w") as p1:
        p1.write(logs)

    agent = ReActExectutor(phase2_fp="phase2")
    agent.execute(logs)