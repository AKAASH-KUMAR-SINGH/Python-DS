import cv2
import numpy as np

img1=np.zeros((500,500,3),np.uint8)
img1=cv2.rectangle(img1,(150,100),(450,400),(255,255,255),-1)
img=cv2.imread('H:\Python+DS\Computer_Vision\img1.jpg')


img=cv2.resize(img,(500,500))
img1=cv2.resize(img1,(500,500))


bitAnd=cv2.bitwise_and(img,img1)
bitOr=cv2.bitwise_or(img,img1)
bitXor=cv2.bitwise_xor(img,img1)
bitNot=cv2.bitwise_not(img)
bitNot=cv2.bitwise_not(img1)


cv2.imshow('img1',img1)
cv2.imshow("img",img)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOr',bitOr)
cv2.imshow('bitXor',bitXor)
cv2.imshow('bitNot',bitNot)
cv2.imshow('bitNot',bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()