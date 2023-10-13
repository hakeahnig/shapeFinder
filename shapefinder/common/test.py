#Importing Classes
from shapeColorDetector import detector
from rtVisualization import visualize
from dataLogging import logger

#Importing libraries
import cv2


#Creating Class Object
base = detector('shapefinder/common/sample_image.JPG')

#Calling Class Functions
base.color_recognition()
contours = base.shape_recognition()
vis = visualize('shapefinder/common/sample_image.JPG', cv2.FONT_HERSHEY_PLAIN, (0, 255, 0))
vis.combine_images(contours)
