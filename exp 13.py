import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.circle(frame, (114,151), 5, (0,0,255), -1)
    cv2.circle(frame, (605,89), 5, (0,0,255), -1)
    cv2.circle(frame, (72,420), 5, (0,0,255), -1)
    cv2.circle(frame, (637,420), 5, (0,0,255), -1)
    imgPts = np.float32([
        [114,151],
        [605,89],
        [72,420],
        [637,420]
    ])
    objPoints = np.float32([
        [0,0],
        [420,0],
        [0,637],
        [420,637]
    ])
    matrix = cv2.getPerspectiveTransform(imgPts, objPoints)
    result = cv2.warpPerspective(frame, matrix, (420,637))
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformation", result)
    key = cv2.waitKey(1)
    if key == 27: 
        break
cap.release()
cv2.destroyAllWindows()
