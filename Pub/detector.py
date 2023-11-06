# detector.py
from ultralytics import YOLO
import numpy as np
import cv2
import colorsys
from collections import Counter

class ObjectDetector:
    def __init__(self, model_path="yolov8s.pt", device="mps"):
        self.model = YOLO(model_path)
        self.device = device
        self.colors = self._generate_colors(80)  # Assuming 80 classes in the model

    @staticmethod
    def _generate_colors(num_colors):
        hsv_tuples = [(x / num_colors, 1., 1.) for x in range(num_colors)]
        colors = map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples)
        colors = list(map(lambda x: (int(x[2] * 255), int(x[1] * 255), int(x[0] * 255)), colors))
        return colors

    def detect(self, frame):
        results = self.model(frame, device=self.device)
        names = self.model.names
        result = results[0]
        class_ids = np.array(result.boxes.cls.cpu(), dtype=int)
        bboxes = np.array(result.boxes.xyxy.cpu(), dtype=int)
        counts = Counter(class_ids)
        messages = {names[class_id]: counts[class_id] for class_id in counts}
        class_names = [names[class_id] for class_id in class_ids]
        return DetectionResult(class_ids, bboxes, class_names, messages)

    def draw_detections(self, frame, detection_result):
        for bbox, class_id, class_name in zip(detection_result.bboxes, detection_result.class_ids, detection_result.class_names):
            (x, y, x2, y2) = bbox
            color = self.colors[class_id]  # Index into the generated colors
            cv2.rectangle(frame, (x, y), (x2, y2), color, 2)
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

class DetectionResult:
    def __init__(self, class_ids, bboxes, class_names, messages):
        self.class_ids = class_ids
        self.bboxes = bboxes
        self.class_names = class_names
        self.messages = messages
