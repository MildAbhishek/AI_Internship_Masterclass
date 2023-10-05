import cv2

img = cv2.imread('images/Sample.jpg')
rectangleImg = cv2.rectangle(img, (10, 10), (30, 30), (0, 0, 255), 2)
cv2.imwrite('images/rectangleImg.jpg', rectangleImg)
