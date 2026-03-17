import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernel = np.ones((4,4), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img,200,200)
# imgCanny2 = cv2.Canny(img,200,200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

cv2.imshow("gray image", imgGray)
cv2.imshow("blurred image", imgBlurred)
cv2.imshow("cannied image", imgCanny)
cv2.imshow("dilated image", imgDilation)
cv2.imshow("eroded image", imgEroded)
# cv2.imshow("cannied image2", imgCanny2)
cv2.waitKey(0)