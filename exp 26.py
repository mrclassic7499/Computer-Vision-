import cv2

logo = cv2.imread("C:/Users/shaik/OneDrive/Pictures/sololeveling.jpg")
img = cv2.imread("C:/Users/shaik/Downloads/a35145e8fe1ddf12c8c945b2e5bdf3361664333053main-Cropped-d26b98e.png")

# Resize logo
logo = cv2.resize(logo, (200, 200))

h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

center_y = h_img // 2
center_x = w_img // 2

top_y = center_y - h_logo // 2
left_x = center_x - w_logo // 2

destination = img[top_y:top_y+h_logo, left_x:left_x+w_logo]

result = cv2.addWeighted(destination, 1, logo, 0.5, 0)

img[top_y:top_y+h_logo, left_x:left_x+w_logo] = result

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
