import cv2  # pip install --prefer-binary opencv-python
import os
import shutil
import numpy as np
import argparse
from pathlib import Path

def extract_frames(video_path, output_folder="frames", frame_skip=5):
    print(f"Extracting frames from: {video_path}")
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(str(video_path))
    frame_count = 0
    saved_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_skip == 0:
            frame_filename = os.path.join(output_folder, f"photo_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1
        frame_count += 1
    cap.release()
    return output_folder

def is_sharp(image_path, threshold=700, contrast_thresh=30):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(image, cv2.CV_64F).var()
    contrast = image.std()
    edges = cv2.Canny(image, 100, 200)
    edge_density = np.mean(edges) / 255
    return laplacian > threshold and contrast > contrast_thresh and edge_density > 0.05

def filter_frames(input_folder, sharp_folder="photo", threshold=700):
    if not os.path.exists(sharp_folder):
        raise FileNotFoundError(f"Output folder '{sharp_folder}/' not found. Please create it manually.")

    files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    sharp_count = 0
    for filename in files:
        filepath = os.path.join(input_folder, filename)
        if is_sharp(filepath, threshold):
            shutil.copy2(filepath, os.path.join(sharp_folder, filename))
            sharp_count += 1
    print(f"Saved {sharp_count} frames to {sharp_folder}/")

def find_video_file(folder="video"):
    supported_ext = (".mp4", ".mov", ".avi", ".mkv")
    video_dir = Path(folder)
    if not video_dir.exists():
        raise FileNotFoundError(f"Video folder '{folder}/' not found.")
    for file in video_dir.iterdir():
        if file.suffix.lower() in supported_ext:
            return file
    raise FileNotFoundError(f"No video file found in '{folder}/' with supported formats.")

def process_video(video_path, threshold=700, frame_skip=5):
    frames_dir = extract_frames(video_path, frame_skip=frame_skip)
    filter_frames(frames_dir, threshold=threshold)
    shutil.rmtree(frames_dir)
    print("Processing completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract sharp frames from video.")
    parser.add_argument("--threshold", type=int, default=700, help="Sharpness threshold (default: 700)")
    parser.add_argument("--skip", type=int, default=5, help="Take every N-th frame (default: 5)")
    args = parser.parse_args()
    video_path = find_video_file("video")
    process_video(video_path, threshold=args.threshold, frame_skip=args.skip)

