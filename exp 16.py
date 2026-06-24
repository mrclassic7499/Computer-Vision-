import cv2
import numpy as np
image = cv2.imread("C:/Users/shaik/Downloads/a35145e8fe1ddf12c8c945b2e5bdf3361664333053main-Cropped-d26b98e.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 100, 200)  
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imwrite('edges_detected.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
