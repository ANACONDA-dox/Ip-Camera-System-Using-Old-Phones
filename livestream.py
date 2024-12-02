import cv2

# List of camera URLs
camera_urls = [
    "https://IPHERE:PORTHERE/video",
    "",
    ""
]

captures = []

for url in camera_urls:
    capture = cv2.VideoCapture(url)
    if not capture.isOpened():
        print(f"Error: Could not open camera feed {url}")
    else:
        captures.append(capture)

# change this to whatever you want!
window_width = 620
window_height = 340

while True:
    frames = []
    for idx, capture in enumerate(captures):
        ret, frame = capture.read()
        if ret:
            frame = cv2.resize(frame, (window_width, window_height))
            frames.append(frame)
            cv2.imshow(f"Camera {idx + 1}", frame)
        else:
            print(f"Error: Could not read frame from camera {idx + 1}")

    if cv2.waitKey(1) == ord('q'):
        break

for capture in captures:
    capture.release()
cv2.destroyAllWindows()
