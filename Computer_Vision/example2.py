import cv2
img=cv2.imread('H:\Python+DS\Computer_Vision\img.jpg',-1)
# Draw a line on the image
# syntax:(img, (initial coordinate),(final coordinate),(color in RGB--> 'BGR'),thickness)
cv2.line(img,(0,0),(255,255),(255,245,255),10)
# arrowedLine(img,(initial coordinate),(final coordinate),(RGB color),thickness)
cv2.arrowedLine(img,(0,0),(210,230),(0,0,253),20)
# rectangle
cv2.rectangle(img,(240,120),(210,20),(200,243,56),10)
# circle
cv2.circle(img,(222,123),43,(234,43,123),0)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'AKASH',(10,500),font,4,(234,255,255),3,cv2.LINE_AA)

cv2.imshow('Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()