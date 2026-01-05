import cv2
from ultralytics import YOLO
model_yolo = YOLO("models/60_epochs_denoised.pt")
results = model_yolo(["image_test.jpg"])
coord=[]
print(results)
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    for box in boxes:
        x1,y1,x2,y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        coord.append((x1,y1,x2,y2))
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen