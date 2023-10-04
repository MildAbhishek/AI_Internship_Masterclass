import cv2 # import opencv library

img = cv2.imread('images/PythonLogo.jpg') # read an image
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thersoldImg = cv2.cvtColor(greyImg, 100, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('images/ThersoldImage.png', thersoldImg)
cv2.imshow('Original Image', img) # show an image
cv2.imshow('Grey Image', greyImg)
cv2.imshow('Thersold Image', 'images/ThersoldImage.png')

cv2.waitKey(0)
cv2.destroyAllWindows()
