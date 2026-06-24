import cv2
import numpy as np
image = cv2.imread("C:/Users/shaik/Downloads/a35145e8fe1ddf12c8c945b2e5bdf3361664333053main-Cropped-d26b98e.png", cv2.IMREAD_GRAYSCALE)
if image is not None:
    kernel = np.ones((5, 5), np.uint8)  
    erosion_result = cv2.erode(image, kernel, iterations=1)
    cv2.imshow("Original Image", image)
    cv2.imshow("Erosion Result", erosion_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")

