import cv2 as cv

img = cv.imread("images/malibu.jpg")

cv.imshow("image is", img)

cv.waitKey(0)