import cv2 # opencv

vs = cv2.VideoCapture(0) #initialize the camera

while True:
    _, img = vs.read() # reading the frame from camera

    cv2.imshow("Video Stream", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break;

vs.release() #releasing the camera
cv2.destroyAllWindows() #close aqll windows
