# runs segmentation script on video

# !ffmpeg -i ppt_b.mp4 ppt_b/'%05d.jpg'

import os
import subprocess

from segment_anything import sam_model_registry
import torch
import numpy as np
from torchvision import transforms
from seg_utils import Visualizer
from typing import Tuple
from PIL import Image
from detectron2.data import MetadataCatalog
import matplotlib.pyplot as plt
import cv2
import io
from segment_anything import SamAutomaticMaskGenerator

metadata = MetadataCatalog.get('coco_2017_train_panoptic')


def inference_sam_m2m_auto(model, image, dest_path, text_size=1080, label_mode='1', alpha=0.2, anno_mode=['Mask',], save=True):
    t = []
    t.append(transforms.Resize(int(text_size), interpolation=Image.BICUBIC))
    transform1 = transforms.Compose(t)
    image_ori = transform1(image)
    image_ori = np.asarray(image_ori)

    mask_generator = SamAutomaticMaskGenerator(model,pred_iou_thresh=0.75, points_per_side=64, stability_score_thresh = 0.8, crop_n_layers = 1)
    outputs = mask_generator.generate(image_ori)

    visual = Visualizer(image_ori, metadata=metadata)
    sorted_anns = sorted(outputs, key=(lambda x: x['area']), reverse=True)
    label = 1

    coords = {}
    mask_map = np.zeros(image_ori.shape, dtype=np.uint8)    
    for i, ann in enumerate(sorted_anns):
        mask = ann['segmentation']
        color_mask = np.random.random((1, 3)).tolist()[0]
        # color_mask = [int(c*255) for c in color_mask]
        demo, x, y = visual.draw_binary_mask_with_number(mask, text=str(label), label_mode=label_mode, alpha=alpha, anno_mode=anno_mode)
        coords[i+1] = [x,y]
        # assign the mask to the mask_map
        mask_map[mask == 1] = label
        label += 1
    im = demo.get_image()   
    pil_image = Image.fromarray(im)
    if save:
        pil_image.save(dest_path)
    return im, coords, pil_image

def highlight(alpha, label_mode, anno_mode, history_texts):
    res = history_texts[0]
    # find the seperate numbers in sentence res
    res = res.split(' ')
    res = [r.replace('.','').replace(',','').replace(')','').replace('"','') for r in res]
    # find all numbers in '[]'
    res = [r for r in res if '[' in r]
    res = [r.split('[')[1] for r in res]
    res = [r.split(']')[0] for r in res]
    res = [r for r in res if r.isdigit()]
    res = list(set(res))
    sections = []
    for i, r in enumerate(res):
        mask_i = history_masks[0][int(r)-1]['segmentation']
        sections.append((mask_i, r))
    return (history_images[0], sections)

def split_into_frames(path_to_video, output_dir):
    os.makedirs(output_dir,exist_ok=True)
    subprocess.run(["ffmpeg", "-i", path_to_video, os.path.join(output_dir, '%05d.jpg')]) 

def images_reader(directory):
    """
    Generator function that yields each JPEG image in a given directory.

    Parameters:
    directory (str): The path to the directory containing JPEG images.

    Yields:
    Image: An opened PIL Image object for each JPEG file.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
            file_path = os.path.join(directory, filename)
            try:
                with Image.open(file_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    yield (img.copy(), file_path)  # yield a copy to avoid closed file issues
            except IOError:
                print(f"Unable to open image {filename}. It may not be a valid JPEG.")

def run_on_single_frame(image, model_sam):
    # dest_path = os.path.join(image_path.split('.')[0] + '_som' + image_path.split('.')[1])
    _, _, np_image = inference_sam_m2m_auto(model_sam, image, dest_path='', anno_mode=['Mask','Mark'], save=False)
    return np_image

if __name__ == "__main__":
    path_to_video = r'C:\Users\V9CMCLC\Downloads\vscode_type.mp4'
    frames_dir = r'..\data\vscode_type'
    split_into_frames(path_to_video, frames_dir)
    
    # path_to_model = r'C:\Users\V9CMCLC\Desktop\hackatons\HackTech_Oradea_2024\hacktech24_app_testing\segmentation\SoM\sam_vit_h_4b8939.pth'
    # model_sam = sam_model_registry["vit_h"](checkpoint=path_to_model).eval().cuda()

    # history_masks = []
    # history_images = []
    # dest_dir = os.path.join(frames_dir, os.pardir, os.path.basename(frames_dir)+'_som')
    # os.makedirs(dest_dir, exist_ok=True)

    # for (image, fp) in images_reader(frames_dir):
    #     dest_path = os.path.join(dest_dir, os.path.basename(fp))
    #     inference_sam_m2m_auto(model_sam, image, dest_path=dest_path, anno_mode=['Mask','Mark'])
