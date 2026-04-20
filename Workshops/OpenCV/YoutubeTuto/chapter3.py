import cv2
import numpy as np


img = cv2.imread("resources/lambo.png")
print(img.shape)

imgresize = cv2.resize(img, (300,200))
print(imgresize.shape)

imgresize2 = cv2.resize(img, (1000,500))
print(imgresize2.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("lambo", img)
cv2.imshow("lambo resized", imgresize)
cv2.imshow("lambo resized2", imgresize2)
cv2.imshow("lambo cropped", imgCropped)
cv2.waitKey(0)