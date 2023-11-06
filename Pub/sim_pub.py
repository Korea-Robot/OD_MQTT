# main.py
import cv2
import json
from detector import ObjectDetector
from mqtt_publisher import MQTTPublisher

def main():
    object_detector = ObjectDetector()
    mqtt_publisher = MQTTPublisher()

    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            detections = object_detector.detect(frame)            
            object_detector.draw_detections(frame, detections)
            mqtt_publisher.publish(json.dumps(detections.messages))
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        mqtt_publisher.stop()

    print("Detection stopped.")

if __name__ == '__main__':
    main()
