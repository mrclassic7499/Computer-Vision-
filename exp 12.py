import cv2
import numpy as np

image = cv2.imread(r"C:\Users\shaik\OneDrive\Pictures\sololeveling.jpg")

# Resize image for better display
image = cv2.resize(image, (600, 600))

rows, cols = image.shape[:2]

# Source points (corners of the original image)
pts1 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

# Destination points (changed positions)
pts2 = np.float32([
    [50, 50],
    [cols - 100, 0],
    [100, rows - 100],
    [cols - 50, rows - 50]
])

# Compute Perspective Transformation Matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
output = cv2.warpPerspective(image, matrix, (cols, rows))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()