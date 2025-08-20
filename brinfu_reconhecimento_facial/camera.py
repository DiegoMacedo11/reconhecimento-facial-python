import cv2 

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    if ret == False:
        break

    cv2.imshow("Video muito legal", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.realese()
cv2.destroyAllWindows()