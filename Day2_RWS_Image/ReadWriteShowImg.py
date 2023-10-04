import cv2 # import opencv library

img = cv2.imread('images/PythonLogo.jpg') # read an image
cv2.imwrite('images/PythonLogoGenerated.png', img) # save an image
cv2.imshow('AI Internship Day 3', img) # show an image
cv2.waitKey(0)
cv2.destroyAllWindows()
 
