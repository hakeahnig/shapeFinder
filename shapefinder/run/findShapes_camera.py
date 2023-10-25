import sys
import os
import cv2

sys.path.append(os.path.abspath('./shapefinder'))

from common.color_detector import color_detector
from common.rtVisualization import visualize
from common.dataLogging import logger
from common.shape_detector import shape_detector


# Camera settings
DEVICE_ID = 0
videoBackend = cv2.CAP_ANY

log = logger()
time = log.__init__()

# open camera
cap = cv2.VideoCapture(DEVICE_ID, videoBackend)
if not cap.isOpened():
    print('Error, could not open camera')
    
while True:
    ret, frame = cap.read()
    if not ret:
        print('Camera Error')
        break
    
    input_key = cv2.waitKey(20)
    if input_key == ord("q"):
        break   
    cv2.imshow("Original frame", frame)
    
    color_det = color_detector(frame)
    shape = shape_detector(frame)
    vis = visualize(frame, cv2.FONT_HERSHEY_PLAIN, (0, 0, 0))
    
    #Calling Class Functions
    contours = shape.get_contours()
    shapes, coordinates = shape.evaluate_contours(contours)
    colors = color_det.color_recognition(contours)
    log.log_to_csv(colors, shapes)
    vis.combine_images(contours, shapes, coordinates, colors)