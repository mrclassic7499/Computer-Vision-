import cv2

def play_video(speed=0.5):
    cap = cv2.VideoCapture(r"C:/Users/shaik/Downloads/146064-788138380_medium.mp4")

    if not cap.isOpened():
        print("Error: Could not open video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        delay = int(1000 / (fps * speed))

        if cv2.waitKey(delay) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

play_video(speed=0.5)
