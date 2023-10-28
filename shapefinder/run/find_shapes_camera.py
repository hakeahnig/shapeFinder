import sys
import os
import cv2

sys.path.append(os.path.abspath("./shapefinder"))

from common.color_detector import ColorDetector
from common.rt_visualization import Visualize
from common.data_logging import Logger
from common.shape_detector import ShapeDetector


# Camera settings
DEVICE_ID = 0
videoBackend = cv2.CAP_ANY

color_det = ColorDetector()
shape = ShapeDetector()
vis = Visualize(cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))
log = Logger()

# open camera
cap = cv2.VideoCapture(DEVICE_ID, videoBackend)
if not cap.isOpened():
    print("Error, could not open camera")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera Error")
        break

    input_key = cv2.waitKey(20)
    if input_key == ord("q"):
        break
    cv2.imshow("Original frame", frame)

    color_det = ColorDetector(frame)
    shape = ShapeDetector(frame)
    vis = Visualize(frame, cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))

    # Calling Class Functions
    contours = shape.get_contours()
    shapes, coordinates = shape.evaluate_contours(contours)
    colors = color_det.color_recognition(contours)
    log.log_to_csv(colors, shapes)
    vis.combine_images(contours, shapes, coordinates, colors)
