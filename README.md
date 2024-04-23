# Step 1: Label the PCB Images on Roboflow

![Screenshot from 2024-04-23 14-33-41](https://github.com/Duc0509Ngo/PCB-defects-detection/assets/97351010/695850c6-76bc-4a5c-a81d-703d89826aeb)

Dataset:

![Screenshot from 2024-04-23 14-36-08](https://github.com/Duc0509Ngo/PCB-defects-detection/assets/97351010/f2a6acb9-adc0-4993-9278-f3b330add90a)

# Step 2: Download the dataset to train YOLO model
Process of traning model occured on Advantech WISE-PaaS/AIFS (workspace for trainning AI model of Advantech company)

 ![Screenshot from 2024-04-23 14-41-24](https://github.com/Duc0509Ngo/PCB-defects-detection/assets/97351010/4389b26e-49a1-49e1-ae6e-38eb754db4cf)
 
# Step 3: Use Industrial camera Baumer to capture PCB images sent to WISE-PaaS/AIFS to inference

![Screenshot from 2024-04-23 15-28-05](https://github.com/Duc0509Ngo/PCB-defects-detection/assets/97351010/60e8d565-75e1-4c2f-9cac-f11544252fe5)

Using MQTT to tranfer image to the server

# Step 4: Store detections of PCB defects in WISE-PaaS Database

# Step 5: Display the PCB defects on Dashboard Grafana

# Reference:

https://arxiv.org/pdf/1901.08204v1.pdf
