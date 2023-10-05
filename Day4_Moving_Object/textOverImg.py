import cv2

img = cv2.imread('images/Sample.jpg')
textOverImg = cv2.putText(img, 'Text Over Image',(10, 50), 1, 22, (0, 0, 255), 2)
cv2.imwrite('images/textOverImg.jpg', textOverImg)

# Find Contours

# dst = cv2.findContours(img, contourRetrievalMode, contourApproximationMethod)
