import cv2

img=cv2.imread('H:\Python+DS\Computer_Vision\img.jpg',1)
cv2.imshow('Window',img)
cv2.line(img,(0,0),(350,350),(0,0,255),5)
cv2.waitKey(0)
# cv2.release()
cv2.destroyAllWindows()