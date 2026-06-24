import cv2

# Read main image
main_image = cv2.imread("C:/Users/shaik/Downloads/MV5BZTNjOWI0ZTAtOGY1OS00ZGU0LWEyOWYtMjhkYjdlYmVjMDk2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")

# Read second image
second_image = cv2.imread("C:/Users/shaik/Downloads/a35145e8fe1ddf12c8c945b2e5bdf3361664333053main-Cropped-d26b98e.png")

if main_image is not None and second_image is not None:

    # Crop a region from second image
    cropped_region = second_image[0:150, 0:150]

    # Resize cropped region if needed
    cropped_region = cv2.resize(cropped_region, (150, 150))

    # Paste into main image at position (50,50)
    main_image[50:200, 50:200] = cropped_region

    cv2.imshow("Result", main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error loading images")
