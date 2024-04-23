from roboflow import Roboflow

rf = Roboflow(api_key="0p9H8vAqaSdCN1RlTVRz")
project = rf.workspace("c-ng").project("pcb-defect-detection-zb6x4")
version = project.version(3)
dataset = version.download("yolov8")