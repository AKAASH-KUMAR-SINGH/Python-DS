import cv2
import numpy as np


#file path
file=r''
vid=cv2.VideoCapture(file)

while True:
    state,image=vid.read()
    if not state:break
    # resize to 500 x 500
    sm_image_1=cv2.resize(image,(500,500))
    sm_image_2=cv2.resize(image,None,fx=.25,fy=.25) #scaledown by 25%
    #filter
    bw_image=cv2.cv
    cv2.imshow('video 1',sm_image_1)
    cv2.imshow('video 2',sm_image_2)
    if key==27:break
cv2.destroyAllWindows()
vid.release()  