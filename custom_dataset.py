import cv2
import uuid
import os
import time
import torch

# Creating custom dataset for training
IMAGES_PATH = os.path.join('data', 'images')
labels = ['awake', 'drowsy']
number_imgs = 20

cap = cv2.VideoCapture(0)
for label in labels:
    print("Collecting images of {}".format(label))
    time.sleep(5)
    for img_nums in range(number_imgs):
        print("Collecting image of {},and count is {}".format(label,img_nums))
        success, img = cap.read()

        # Naming the image path
        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')

        # Writes out image to file
        cv2.imwrite(imgname, img)
        cv2.imshow("Image collection", img)

        # 2 second delay
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break



