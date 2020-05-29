import cv2
import os
import numpy as np
from PIL import Image

str_p = "C:\\Users\\vinoo\Desktop\\testing\\images"
BASE_DIR = os.path.dirname(os.path.abspath(str_p))
# print(BASE_DIR)
image_dir = os.path.join(BASE_DIR, "images")
face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)
            # y_labels.append(label) #number
            # x_train.append(path) # verify this image, turn into a Numpy array,
            pil_image = Image.open(path).convert("L")  # grayscale
            image_array = np.array(pil_image, "uint8")
            print(image_array)

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)
# print(x_train)