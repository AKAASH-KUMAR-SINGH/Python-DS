import cv2
import numpy as np

# Create a VideoCapture object
WEBCAM_IDX=0
cam=cv2.VideoCapture(WEBCAM_IDX)

cv2.namedWindow('image')    #window
cv2.createTrackbar('min','image',0,1000,lambda x: x)
cv2.createTrackbar('max','image',0,1000,lambda x: x)
cv2.createTrackbar('xpos','image',0,640,lambda x: x)
cv2.createTrackbar('ypos','image',0,480,lambda x: x)


while cam.isOpened():
    # capture image from camera
    state,image=cam.read()
    if not state: break #if state is none then break

    minVAl = cv2.getTrackbarPos('min','image')
    maxVal = cv2.getTrackbarPos('max','image')
    filter = cv2.Canny(image,minVAl,maxVal)
    xp=cv2.getTrackbarPos('xpos','image')
    yp=cv2.getTrackbarPos('ypos','image')
    image=cv2.putText(image,"Computer Vision",(xp,yp),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))

    #show image
    cv2.imshow('filter',filter)
    cv2.imshow('image',image)

    # wait for key press
    cv2.waitKey(10)
    if key == 27: break

# release camera
cam.release()
cv2.destroyAllWindows()