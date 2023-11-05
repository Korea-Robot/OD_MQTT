# main.py
import cv2
from detector import detect_objects
from mqtt_publisher import publish_to_mqtt, stop_mqtt
import json

def draw_detections(frame, bboxes, classes):
    for cls, bbox in zip(classes, bboxes):
        (x, y, x2, y2) = bbox
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, str(cls), (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

def main():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detections, bboxes, classes = detect_objects(frame)
            draw_detections(frame, bboxes, classes)

            if detections:
                publish_to_mqtt(json.dumps(detections))

            cv2.imshow("Detection", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        stop_mqtt()

    print("Detection stopped.")

if __name__ == '__main__':
    main()
