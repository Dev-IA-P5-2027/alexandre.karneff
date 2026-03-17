import cv2
print("Package Imported")


# img = cv2.imread("resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Create a resizable window
cv2.namedWindow("My Window", cv2.WINDOW_NORMAL)

# Resize the window to 800x600 pixels
cv2.resizeWindow("My Window", 800, 600)

cap = cv2.VideoCapture("resources/test_video.mp4")
# cap.set(3,640) webcam
# cap.set(4,480)
while True :
    success, img = cap.read()
    cv2.imshow("My Window", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    