import cv2 # opencv
import time # delay
import imutils #resize

cam = cv2.VideoCapture(0) #cam id
time.sleep(1)

firstFrame = None
area = 500

while True:
    _, img = cam.read() # reading the frame from camera
    cv2.imshow("Video Stream", img)
    text = "Normal"
    img = imutils.resize(img, width=300) # resize

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color to gray scale image
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21),0) # smoothened

    if firstFrame is None:
        firstFrame = gaussianImg # capturing first frame on 1st iteration
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg) # absolute diff b/w
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] # binary

    threshImg = cv2.dilate(threshImg, None, iterations=2)

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < 50:
            continue
        
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text = "Moving object detected"
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break;
    
cam.release();
cv2.destroyAllWindows()
    