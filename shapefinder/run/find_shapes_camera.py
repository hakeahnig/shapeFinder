import sys
import os
import cv2

sys.path.append(os.path.abspath("./shapefinder"))
from common.color_detector import ColorDetector
from common.rt_visualization import Visualize
from common.data_logging import Logger
from common.shape_detector import ShapeDetector


# Loading color ranges
color_ranges = [
        ["red", 0, 41],
        ["yellow", 41, 70],
        ["green", 71, 180],
        ["blue", 181, 280],
        ["purple", 260, 360],
    ]

# create objects
color_det = ColorDetector(color_ranges)
shape = ShapeDetector()
vis = Visualize(cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))
log = Logger()

# open camera
DEVICE_ID = 0
videoBackend = cv2.CAP_ANY
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

    contours = shape.get_contours(frame)
    shapes, coordinates = shape.evaluate_contours(contours)
    colors = color_det.color_recognition(frame, contours)
    log.log_to_csv(colors, shapes)
    combined_frame= vis.combine_images(frame, contours, shapes, coordinates, colors)
    cv2.imshow("Combined Image", combined_frame)
