from ultralytics import YOLO

model = YOLO("yolov8s.pt") # load the model
results = model.train(data="PCB-defect-detection-3/data.yaml", epochs=100)


