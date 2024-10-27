from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
from pathlib import Path

def main():
    model_name = "Qwen/Qwen2-VL-7B-Instruct"
    video_path = "step1_qwen\video\wordpad_interaction.mp4"
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, device_map="auto"
    )

    with open('step1_qwen\prompts\system_prompt.txt', 'r') as file:
        system_prompt = file.read()
    processor = AutoProcessor.from_pretrained(model_name)
    messages = [
        {
            "role": "system",
            "content": f'{system_prompt}'
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "video",
                    "video": video_path,
                    "max_pixels": 480 * 360,
                    "fps": 2.0,
                },
                {"type": "text", "text": "Analyze the video and tell me what the user interacted with in the interface."},
            ],
        }
    ]
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")
    generated_ids = model.generate(**inputs, max_new_tokens=512)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    log_path = f'output/log_{Path(video_path).stem}.json'
    with open(log_path, 'w+') as file:
        file.write(str(output_text[0]).strip().replace('```json\n', '').replace('```', ''))
        file.close()


if __name__ == "__main__":
    main()