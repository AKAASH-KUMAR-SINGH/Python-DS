import numpy as np
import cv2

img=cv2.imread('H:\Python+DS\Computer_Vision\img.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

flower=img[2800:340,330:390]
# img[273:333,100:140]=flower

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindow()