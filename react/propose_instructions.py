import litellm
from utils import encode_image
from glob import glob


def get_instruction_set(frame_dir):
    context = ""
    for frame_path in glob(frame_dir):
        base64_image = encode_image(frame_path)
        prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": "You are a helpful assistant that describes how a user operates an application. You will be provided a recording frame by frame."}]},
            {"role": "user",
                "content": [{"type": "text", "text": "Describe shortly with what elements the user interacts with in the next frame:"}, 
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "high"},}]},
        ]
        response = litellm.completion(model="gpt-4-turbo",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=1).choices[0].message.content
        context += response

    prompt_input = [
            {"role": "system", 
                "content": [{"type": "text", "text": "You are a helpful assistant that describes operates an application. You will be provided a recording frame by frame."}]},
            {"role": "user",
                "content": [{"type": "text", "text": f"Summarize the elements the user interacted with using an instruction list based on the following context: \n {context} \n Start:\n"}]},
        ]
    response = litellm.completion(model="gpt-4-turbo",
                                    messages=prompt_input,
                                    max_tokens=4096,
                                    temperature=1).choices[0].message.content
    return response
       