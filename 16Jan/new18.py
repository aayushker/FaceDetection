import cv2
import datetime as dt

# Add your full name
your_name = "Aayushker Singh"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    date_time = str(dt.datetime.now())
    # Concatenate your name with the date_time
    text_to_display = f"{date_time} - {your_name}"

    # Adjusted the position for better visibility
    frame = cv2.putText(frame, text_to_display, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()