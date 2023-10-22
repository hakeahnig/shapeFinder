import cv2
import colorsys
class color_detector:
    #Name, lower range, upper range
    """    
    color_ranges = [['red', 0, 30],
                    ['yellow', 30, 60],
                    ['green', 60, 150],
                    ['blue', 150, 240],
                    ['purple', 240, 350]]
     """

      
    color_ranges = [['red', 0, 41],
                    ['yellow', 41, 70],
                    ['green', 71, 180],
                    ['blue', 181, 280],
                    ['purple', 260, 360]]

    """    color_ranges = [['red', 0, 30],
                    ['yellow', 31, 60],
                    ['green', 61, 90],
                    ['blue', 91, 150],
                    ['purple', 151, 180]]"""

    def __init__(self, image, font=cv2.FONT_HERSHEY_DUPLEX, color=(0,255,0)):
        self.image = image
        self.font = font
        self.colour = color

    
    def color_recognition(self, contours):
        # Extract colors from middle of shapes
        cv2.imshow("self image", self.image)
        color_names = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)

            coords = (int(x+w/2), int(y+h/2))

            color = self.image[coords[1], coords[0]]

            color = colorsys.rgb_to_hsv(color[2]/255, color[1]/255, color[0]/255)
            print("color", color)
            color_name = 'no color found'
          
            for i in range(len(self.color_ranges)):
                if self.color_ranges[i][1] <= color[0]*360 <= self.color_ranges[i][2]:
                    color_name = self.color_ranges[i][0]

            color_names.append(color_name)
            
        return color_names
    
