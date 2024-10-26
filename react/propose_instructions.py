import litellm
from utils import encode_image
from glob import glob
from dotenv import load_dotenv
load_dotenv("../.env")

def get_instruction_set(frame_dir):
    context = ""
    for frame_path in glob(frame_dir):
        print(frame_path)
        base64_image = encode_image(frame_path)
        prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": "You are a helpful assistant that describes how a user operates an application. You will be provided a recording frame by frame. The only allowed actions are: click, type text and scroll.\n"}]},
            {"role": "user",
                "content": [{"type": "text", "text": "Describe shortly with what elements the user interacts with in the next frame:"}, 
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "high"}}]},
        ]
        response = litellm.completion(model="gpt-4-turbo",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=0.7).choices[0].message.content
        context += response

    prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": "You are a helpful assistant that describes how a user operates an application. You will be provided a recording frame by frame. The only allowed actions are: click, type text and scroll. Try not to make any extra actions than showed in the frames. A specific choice has to be made for each frame.\n"}]},
            {"role": "user",
                "content": [{"type": "text", "text": f"Summarize the elements the user interacted with using an instruction list based on the following context: \n {context} \n Start:\n"}]},
        ]
    response = litellm.completion(model="gpt-4-turbo",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=0.7).choices[0].message.content
    return response
       

if __name__ == '__main__':
    p = fr"../data/vscode_mic_rare/*"
    print(get_instruction_set(p))