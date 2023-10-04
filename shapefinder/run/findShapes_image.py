import sys
import os

sys.path.append(os.path.abspath('.'))

#Importing Classes
from common.color_detector import color_detector
from common.rtVisualization import visualize
from common.dataLogging import logger
from common.shape_detector import shape_detector

#Import libraries
import cv2

#Creating Class Object
image_path = '/home/madame/Documents/Semester 5/SOFENG/Project_1/shapeFinder/shapefinder/common/sample_image.JPG'
base = color_detector(image_path)
shape = shape_detector(image_path)
vis = visualize(image_path, cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))

#Calling Class Functions
base.color_recognition()
contours = shape.get_contours()
shapes, coordinates = shape.evaluate_contours(contours)
vis.combine_images(contours, shapes, coordinates)

