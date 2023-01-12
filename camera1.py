import cv2
import numpy as npimport
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
vcap = cv2.VideoCapture("rtsp://homeassistant.local:8554/cmera", cv2.CAP_FFMPEG)
while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break;
    else:
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)

print('oi2');