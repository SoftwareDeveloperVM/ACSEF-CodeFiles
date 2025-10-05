import cv2
import torch

# Load YOLO model (YOLOv5 pretrained model)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'yolov5s' for faster but slightly less accurate model

# Open webcam or video
cap = cv2.VideoCapture(0)  # Change to a video file if needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection (YOLO)
    results = model(frame)

    # Parse the results
    detections = results.pandas().xywh[0]  # Pandas dataframe with detection results

    # Loop through detections and draw bounding boxes
    for i, row in detections.iterrows():
        if row['name'] == 'fish':  # Assuming 'fish' is in the model's label
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw bounding box

            # Display label
            label = f"Fish {int(i) + 1}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the resulting frame
    cv2.imshow('Fish Tracking', frame)

    # Break on pressing 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

