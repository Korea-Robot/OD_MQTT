# main.py
import cv2
from detector import detect_objects, draw_detection, generate_colors
from mqtt_publisher import publish_to_mqtt, stop_mqtt
import json

class_colors = generate_colors(80)

def main():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            class_ids, bboxes, class_name, message = detect_objects(frame)            
            draw_detection(frame, bboxes, class_ids, class_name, class_colors)
            message_json = json.dumps(message)
            publish_to_mqtt(message_json)
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        stop_mqtt()

    print("Detection stopped.")


if __name__ == '__main__':
    main()
