import cv2

print(cv2.__version__)
# flag=1 Load a color image;flag=0 load image in grayscale mode;flag=-1 Load image as such include 
# alpha channel
img=cv2.imread('H:\Python+DS\Computer_Vision\img.jpg',-1)
# print(img)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('img_copy.jpg',img)
    cv2.destroyAllWindows()