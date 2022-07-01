import cv2
import os
import random
import numpy as np

location = input("Specify the directory to choose from: ")
images = []
for files in os.listdir(location):
   images.append(files)
random = random.randint(0,len(images)-1)

img = cv2.imread(location + images[random], cv2.IMREAD_ANYCOLOR)

screen_res = 1920, 1080
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)

window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized Window', window_width, window_height)

cv2.imshow('Resized Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()