# detector.py
from ultralytics import YOLO
import numpy as np

# Initialize the YOLO model
model = YOLO("yolov8s.pt")

def detect_objects(frame):
    results = model(frame, device="mps")
    result = results[0]
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    classes = np.array(result.boxes.cls.cpu(), dtype="int")

    detections = [{'class': int(cls), 'box': bbox.tolist()} for cls, bbox in zip(classes, bboxes)]
    return detections, bboxes, classes
