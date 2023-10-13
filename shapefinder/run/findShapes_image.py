import sys
import os

sys.path.append(os.path.abspath('./shapefinder'))

#Importing Classes
from common.color_detector import color_detector
from common.rtVisualization import visualize
from common.dataLogging import logger
from common.shape_detector import shape_detector

#Import libraries
import cv2

#Creating Class Object
image_path = 'shapefinder/common/sample_image.JPG'
image = cv2.imread(image_path)
color_det = color_detector(image)
shape = shape_detector(image)
vis = visualize(image, cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))

#Calling Class Functions
contours = shape.get_contours()
shapes, coordinates = shape.evaluate_contours(contours)
colors = color_det.color_recognition(contours)
print(colors)
print(shapes)
vis.combine_images(contours, shapes, coordinates)
