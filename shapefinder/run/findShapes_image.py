import sys
#sys.path.insert(0,"/home/madame/Documents/Semester 5/SOFENG/Project_1/shapeFinder/shapefinder/common")

#Importing Classes
from color_detector import color_detector
from rtVisualization import visualize
from dataLogging import logger
from shape_detector import shape_detector

#Import libraries
import cv2

#Creating Class Object
image_path = '/home/madame/Documents/Semester 5/SOFENG/Project_1/shapeFinder/shapefinder/common/sample_image.JPG'
base = color_detector(image_path)
shape = shape_detector(image_path)
vis = visualize(image_path, cv2.FONT_HERSHEY_PLAIN, (0, 255, 0))

#Calling Class Functions
base.color_recognition()
contours = shape.shape_recognition()
vis.combine_images(contours)

