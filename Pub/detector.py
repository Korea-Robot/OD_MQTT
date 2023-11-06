# detector.py
from ultralytics import YOLO
import numpy as np
import cv2
import colorsys
from collections import Counter
# Initialize the YOLO model
model = YOLO("yolov8s.pt")

def generate_colors(num_colors):
    # Generate colors in HSV space and convert them to BGR.
    hsv_tuples = [(x / num_colors, 1., 1.) for x in range(num_colors)]
    colors = map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples)
    colors = list(map(lambda x: (int(x[2] * 255), int(x[1] * 255), int(x[0] * 255)), colors))
    return colors

def detect_objects(frame):
    results = model(frame, device="mps")
    names = model.names
    result = results[0] 
    class_ids = np.array(result.boxes.cls.cpu(), dtype= int)
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype= int)
    counts = Counter(class_ids)
    # Initialize messages with counts of detections for each class name
    messages = {names[class_id]: counts[class_id] for class_id in counts}

    # Get the list of class names corresponding to the detected class IDs
    class_names = [names[class_id] for class_id in class_ids]
    return class_ids, bboxes, class_names, messages

def draw_detection(frame, bboxes, class_ids, class_names, class_colors):
    for bbox, class_id, class_name in zip(bboxes, class_ids, class_names):
        (x, y, x2, y2) = bbox
        color = class_colors[class_id]  # Index into the generated colors
        cv2.rectangle(frame, (x, y), (x2, y2), color, 2)
        cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

