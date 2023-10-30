import sys
import os
import cv2

sys.path.append(os.path.abspath("./shapefinder"))

from common.color_detector import ColorDetector
from common.rt_visualization import Visualize
from common.data_logging import Logger
from common.shape_detector import ShapeDetector


# Loading color ranges
COLOR_RANGES = [
        ["red", 0, 41],
        ["yellow", 41, 70],
        ["green", 71, 180],
        ["blue", 181, 280],
        ["purple", 260, 360],
    ]

# Creating Class Object
IMAGE_PATH = "shapefinder/common/sample_image.JPG"
LOG_PATH = "logs/logdata.csv"
image = cv2.imread(IMAGE_PATH)
color_det = ColorDetector(COLOR_RANGES)
shape = ShapeDetector()
vis = Visualize(cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))
log = Logger(LOG_PATH)

# Calling Class Functions
contours = shape.get_contours(image)
shapes, coordinates = shape.evaluate_contours(contours)
colors = color_det.color_recognition(image, contours)
log.log_to_csv(colors, shapes)
combined_image = vis.combine_images(image, contours, shapes, coordinates, colors)
cv2.imshow("Combined Image", combined_image)
cv2.waitKey()
