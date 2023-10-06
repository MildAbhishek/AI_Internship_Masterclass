import cv2 # opencv


alg = "haarcascade_frontalface_default.xml" #accessed the algorithm file
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0) #initializing camera

while True:
    _, img = cam.read() # reading the frame from camera
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color to gray scale image

    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Face Detetcted", img)
    key = cv2.waitKey(10)
    if key == 27:
        break;
cam.release()
cv2.destroyAllWindows()
