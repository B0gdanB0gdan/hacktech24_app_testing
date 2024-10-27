import os
import glob
import shutil
import subprocess


def split_into_frames(path_to_video, output_dir):
    # os.makedirs(output_dir,exist_ok=True)
    # subprocess.run(["ffmpeg", "-i", path_to_video, os.path.join(output_dir, '%05d.jpg')]) 
    less_frames_dir = output_dir + '_less'
    os.makedirs(less_frames_dir, exist_ok=True)
    for i,p in enumerate(glob.glob(fr'{output_dir}\*jpg')):
        if i%20==0:
            shutil.copy(p, os.path.join(less_frames_dir,os.path.basename(p)))

if __name__ == "__main__":
    split_into_frames(r'..\data\vlc.mp4', r'..\data\vlc')