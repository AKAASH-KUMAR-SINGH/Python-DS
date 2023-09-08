import cv2
import numpy as np

# Create a VideoCapture object
WEBCAM_IDX=0
cam=cv2.VideoCapture(WEBCAM_IDX)
while cam.isOpened():
    # capture image from camera
    state,image=cam.read()
    if not state: break #if state is none then break
    #show image
    key=cv2.imshow('image',image)

    # wait for key press
    cv2.waitKey(10)
    if key == 27: break

# release camera
cam.release()
cv2.destroyAllWindows()