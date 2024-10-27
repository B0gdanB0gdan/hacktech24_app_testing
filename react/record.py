import cv2
import numpy as np
import pyautogui
from PIL import Image
import time
import os


def record_screen(output_file, duration, fps=20):
    # Screen resolution
    screen_size = pyautogui.size()
    
    # Video Writer
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, fps, (screen_size.width, screen_size.height))
    frame_interval = 1.0 / fps
    # Capture screen
    start_time = time.time()
    while True:
        # Take screenshot
        img = pyautogui.screenshot()
        
        # Convert screenshot to a numpy array
        frame = np.array(img)
        
        # Convert color from RGB to BGR (for OpenCV compatibility)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Write frame to video
        out.write(frame)
        
        # Break if the duration has passed
        if time.time() - start_time > duration:
            print(time.time() - start_time)
            break

        time.sleep(frame_interval)

    # Release everything
    out.release()
    cv2.destroyAllWindows()

def extract_frames_from_video(video_file, output_folder, skip_factor=1):
    os.makedirs(output_folder, exist_ok=True)
    # Open video file
    cap = cv2.VideoCapture(video_file)
    
    frame_index = 0
    saved_frame_index = 0
    
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save the frame if it's in the skip factor
        if frame_index % skip_factor == 0:
            # Save frame as an image
            frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frame_image.save(f"{output_folder}/frame_{saved_frame_index}.png")
            saved_frame_index += 1

        # Increment frame index
        frame_index += 1
    
    # Release the video capture
    cap.release()

# Usage example
if __name__ == "__main__":
    video_filename = "recorded_screen.avi"
    record_duration = 10  # Record for 10 seconds
    record_fps = 1  # Frames per second
    record_screen(video_filename, record_duration, record_fps)
    os.makedirs("frames", exist_ok=True)
    extract_frames_from_video(video_filename, "frames")