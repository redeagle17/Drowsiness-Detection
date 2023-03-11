import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Testing the model on a image
# img = 'https://media.wired.com/photos/593256b42a990b06268a9e21/master/pass/traffic-jam-getty.jpg'
#
# result = model(img)
#
# cv2.imshow('Result', np.squeeze(result.render()))
# cv2.waitKey(0)


# Realtime detection
# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#
#     result = model(img)
#     cv2.imshow('Result', np.squeeze(result.render()))
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break