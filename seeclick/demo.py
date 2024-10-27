import argparse
import cv2
import json
import re
import os
import time

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig


def get_image_resolution(image_path):
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    return width, height


def main():
    parser = argparse.ArgumentParser(description="AI application")

    parser.add_argument("--logfile", type=str, help="Path to logfile output from the first AI applicatio")
    parser.add_argument("--images", type=str, help="Path to screenshots taken during application testing replication")

    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("cckevinn/SeeClick", device_map="cuda:1", trust_remote_code=True, bf16=True).eval()
    model.generation_config = GenerationConfig.from_pretrained("Qwen/Qwen-VL-Chat", trust_remote_code=True)

    with open(args.logfile, 'r') as file:
        data = json.load(file)
        
    actions = data['actions']
    existing_image_files = set(os.listdir(args.images))
    
    i = 0
    while True:
        current_image_files = set(os.listdir(args.images))
        new_file = current_image_files - existing_image_files

        if new_file:
            new_file = os.path.join(args.images, new_file.pop())

            action = actions[i]
            i = i + 1

            # if action['type'] == 'type':
            #     prompt = f" Element: {action['element']}, action type: {action['type']}, value: {action['value']}."
            # else:
            #     prompt = f" Element: {action['element']}, action type: {action['type']}."

            prompt = action['description']
            
            query = tokenizer.from_list_format([
                {'image': new_file},
                {'text': prompt},
            ])
            response, _ = model.chat(tokenizer, query=query, history=None)

            match = re.findall(r'-?\d+\.\d+|-?\d+', response)
            point_coordinates_norm = list(map(float, match))

            width, height = get_image_resolution(new_file)

            x_center, y_center = int(point_coordinates_norm[0] * width), int(point_coordinates_norm[1] * height)

            img = cv2.imread(new_file)
            cv2.circle(img, (x_center, y_center), 10, (0, 0, 255), -1)

            cv2.imwrite(f'Screenshot_{i}.jpg', img)

            existing_image_files = current_image_files

            if i == len(actions):
                break
        time.sleep(2)


if __name__=="__main__":
    main()