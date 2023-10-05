import cv2 # import opencv library
import imutils

img = cv2.imread('images/Sample.jpg') # read an image
resizeImg = imutils.resize(img, width=50) #resize an image

cv2.imwrite('images/resizedImage.jpg',resizeImg) # save the image
