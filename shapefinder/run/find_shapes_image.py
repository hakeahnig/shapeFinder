import sys
import os
import cv2

sys.path.append(os.path.abspath("./shapefinder"))

from common.color_detector import ColorDetector
from common.rt_visualization import Visualize
from common.data_logging import Logger
from common.shape_detector import ShapeDetector

# Creating Class Object
IMAGE_PATH = "shapefinder/common/sample_image.JPG"
image = cv2.imread(IMAGE_PATH)
color_det = ColorDetector()
shape = ShapeDetector()
vis = Visualize(cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))
log = Logger()

# Calling Class Functions
contours = shape.get_contours(image)
shapes, coordinates = shape.evaluate_contours(contours)
colors = color_det.color_recognition(image, contours)
log.log_to_csv(colors, shapes)
combined_image = vis.combine_images(image, contours, shapes, coordinates, colors)
cv2.imshow("Combined Image", combined_image)
cv2.waitKey()
