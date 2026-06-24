import cv2
import numpy as np
img = cv2.imread("C:/Users/shaik/Downloads/images.jpg")
if img is None:
    print("Error: Image not found")
    exit()
pts_src = np.float32([
    [141, 131],
    [480, 159],
    [493, 630],
    [64, 601]
])
pts_dst = np.float32([
    [0, 0],
    [400, 0],
    [400, 600],
    [0, 600]
])
H, status = cv2.findHomography(pts_src, pts_dst)
result = cv2.warpPerspective(img, H, (400, 600))
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
