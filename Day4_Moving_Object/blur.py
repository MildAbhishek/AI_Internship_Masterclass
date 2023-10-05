import cv2
import imutils

img = cv2.imread('images/Sample.jpg')
guassianBlurImg = cv2.GaussianBlur(img, (25, 25), 0)
cv2.imwrite('images/blurredImg.jpg', guassianBlurImg)
