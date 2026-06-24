import cv2
image = cv2.imread("C:/Users/shaik/Downloads/MV5BZTNjOWI0ZTAtOGY1OS00ZGU0LWEyOWYtMjhkYjdlYmVjMDk2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
edges = cv2.Canny(image,threshold1=30,threshold2=100)
cv2.imshow('Original Image',image)
cv2.imshow('Canny Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
