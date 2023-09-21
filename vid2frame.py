# a video will be manually selected and it will be converted into frames. then those frames will be 
# manually labelled as accident and non-accident cases. once all is done. the YOLO classification 
# algorithm will be trained.
# during the testing a video will be given, which will be converted into frames. frames will be iterated
# through to assign them the classification predicton ids. or their positions in the array will be noted
# the video will be then generated using the noted position

import cv2
import os

# Path to the video file
path = './'
video_name = ''
format = '.mp4'

# Initialize frame counter
frame_count = 0

video_path = os.path.join(path,video_name + format)

# Output folder for frames
output_folder = os.path.join(path,video_name)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

# following two lines will informa about the total numbers of frames
# frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(f'Total frames in the video: {frame_count}')


# Loop through frames in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if we've reached the end of the video
    if not ret:
        break

    # Save the frame as an image file
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    # Increment frame counter
    frame_count += 1

# Release the video capture object
cap.release()

print(f'{frame_count} frames saved to {output_folder}')