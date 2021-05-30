import cv2 as cv
cap = cv.VideoCapture("images/video.mp4")

while cap.isOpened():
    ret,frame = cap.read()
    cv.imshow("webcame",frame)
    if not ret:
        print("vide error")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("q"):
        break
