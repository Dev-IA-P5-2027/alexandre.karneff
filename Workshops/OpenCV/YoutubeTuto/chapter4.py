import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# img[:] = 255,0,0
# print(img)
print(img.shape)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),thickness=2)
cv2.rectangle(img, (0,0), (250,350), (0,0,255),thickness=3)
cv2.circle(img, (400,50), 30,(255,255,0),thickness=cv2.FILLED)
cv2.putText(img, "OPENCV", (300,200),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,50,200),1)


cv2.imshow("image", img)
cv2.waitKey(0)