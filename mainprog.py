import cv2
import numpy as np
import sys

#takes the image as input
image = cv2.imread(sys.argv[1])

#find the first non-white pixel by iterating through the image's pixels starting from the top left pixel and moving down 
row = 0
col = 0
while True:
    pixel = image[row, col]
    #breaks when it first comes across a blue pixel because that means that we have hit a writing lane
    if (pixel[0] > 100 and pixel[1] > 100 and pixel[2] < 150):
        break
    else:
        row += 1

#calculate the percentage of the page from the top left corner to the first non-white pixel
percentage = (row * 100) / image.shape[0]

width = image.shape[1]
height = image.shape[0]
region_width = width
region_height = int(height * percentage / 100)
print(region_width)
print(region_height)
#crops the image so we can keep the part of the image that we are intrested in 
roi = image[0:region_height, 0:region_width]

#convert the image to HSV so it can be easier to understand colors
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#define the color ranges
red_min = np.array([0, 100, 100])
red_max = np.array([10, 255, 255])
green_min = np.array([50, 100, 100])
green_max = np.array([70, 255, 255])
blue_min = np.array([100, 100, 100])
blue_max = np.array([130, 255, 255])

#create masks for each color
red_mask = cv2.inRange(hsv, red_min, red_max)
green_mask = cv2.inRange(hsv, green_min, green_max)
blue_mask = cv2.inRange(hsv, blue_min, blue_max)

#count the non zero pixels in each mask
red_pixels = cv2.countNonZero(red_mask)
green_pixels = cv2.countNonZero(green_mask)
blue_pixels = cv2.countNonZero(blue_mask)
subject=""
#determine the subject
if red_pixels > green_pixels and red_pixels > blue_pixels:
    subject="Math"
elif blue_pixels > green_pixels and blue_pixels > red_pixels:
    subject="Language"
elif green_pixels > blue_pixels and green_pixels > red_pixels:
    subject="Biology"
