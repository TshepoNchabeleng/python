import cv2 as cv

# ESP32-CAM uses HTTP streaming, not RTSP
# Replace with your ESP32's IP address
esp32_url = "http://192.168.18.52:81/stream"  # Common port is 81

cap = cv.VideoCapture(esp32_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    print("Try opening this URL in your browser: " + esp32_url)
    exit()

cv.namedWindow("Live Feed", cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    if not ret: 
        print("Error: Failed to grab frame.")
        break

    # Image processing
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Live Feed", gray_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()