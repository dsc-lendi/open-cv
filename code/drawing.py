import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#line
cv.line(img,(0,0),(511,511),(111,123,255),5)
#rectangle
cv.rectangle(img,(384,0),(510,128),(1,13,67),5)
#circle
cv.circle(img,(256,256),100,(255,0,0),5)
#filled circle
cv.circle(img,(100,100),100,(255,0,0),-1)
#text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"OpenCV is good",(15,200),font,4,(120,120,120),3,cv.LINE_AA)




#image show
cv.imshow("image",img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("images/mydrawing.png",img)
#quit = q

