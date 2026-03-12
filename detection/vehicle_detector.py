from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

VEHICLE_CLASSES = ["car", "bus", "truck", "motorbike"]

def detect_vehicles(frame):

    results = model(frame)

    vehicle_count = 0
    labels = []

    for r in results:

        boxes = r.boxes.xyxy
        classes = r.boxes.cls

        for box, cls in zip(boxes, classes):

            x1, y1, x2, y2 = map(int, box)

            label = model.names[int(cls)]

            labels.append(label)

            if label in VEHICLE_CLASSES:
                vehicle_count += 1

                # draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

                # label text
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0,255,0),
                    2
                )

    return vehicle_count, labels, frame