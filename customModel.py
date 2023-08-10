import cv2
from ultralytics import YOLO

# Loading the custom model 'best.pt'
custom_model = YOLO("custom_model/best.pt")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Make detections
    results = custom_model(frame, show=True)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)