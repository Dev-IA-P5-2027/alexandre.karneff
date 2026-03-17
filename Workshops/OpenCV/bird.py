import cv2 as cv    
import numpy as np

image = cv.imread("images/bird.jpg", 0)

print(image.shape)


cv.imshow("image Test", image)
k = cv.waitKey(0)

if k == ord("s") :
    cv.imwrite("images/bird_ingrey_png.png", image)
    print("image sauvegardée")
else :
    cv.destroyAllWindows()
    print("les fenêtres ont été détruites")