import cv2 as cv
cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv.imshow("webcame",frame)
    if not ret:
        print("camera open cheyalekapoyanu")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("q"):
        break

