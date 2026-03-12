from ultralytics import YOLO

class YOLOv8Model:

    def __init__(self, model_path="yolov8n.pt"):
        """
        Initialize YOLOv8 model
        """
        self.model = YOLO(model_path)

    def detect(self, frame):
        """
        Run object detection on a frame
        """
        results = self.model(frame)

        detections = []

        for r in results:

            boxes = r.boxes.xyxy
            classes = r.boxes.cls

            for box, cls in zip(boxes, classes):

                x1, y1, x2, y2 = map(int, box)

                label = self.model.names[int(cls)]

                detections.append({
                    "label": label,
                    "box": (x1, y1, x2, y2)
                })

        return detections