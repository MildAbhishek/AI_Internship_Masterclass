import cv2 # import opencv library

img = cv2.imread('images/PythonLogo.jpg') # read an image
greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', img) # show an image
cv2.imshow('Grey Image', greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
