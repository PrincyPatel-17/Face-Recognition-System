import cv2
import os

path = "faces/Princy/1.jpg"

print("File exists:", os.path.exists(path))

image = cv2.imread(path)

if image is None:
    print("ERROR: OpenCV could not read the image.")
else:
    print("Image loaded successfully.")
    print("Width :", image.shape[1])
    print("Height:", image.shape[0])
    print("Channels:", image.shape[2])