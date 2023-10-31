# this file will convert the frames to video in the number sequence that was given to the stored frames

import cv2
import os

image_folder = '/path/to/your/image_folder'
video_name = '.avi'

# sorted frames list
image_folder_list = os.listdir(image_folder)
image_folder_list = sorted(image_folder_list) # sorted all the frames as per their given title
# print(f'{image_folder_list[0]}')

# taking only one frame to calculate the width and height of the video
frame = cv2.imread(os.path.join(image_folder, image_folder_list[0]))
h, w, l = frame.shape

# initializing the video maker object
video = cv2.VideoWriter(video_name, 0, 15, (w,h)) #(video_name>>video_name, 0>>turn-off some codec, 15>>framerate, (w,h)>>shape)

for frame in image_folder_list:
    video.write(cv2.imread(os.path.join(image_folder, frame)))

cv2.destroyAllWindows()
video.release()