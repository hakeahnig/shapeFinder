import cv2

class color_detector:
    #Name, lower range, upper range
    color_ranges = [['red', 0, 30],
                    ['yellow', 30, 60],
                    ['green', 60, 150],
                    ['blue', 150, 240],
                    ['purple', 240, 350]]
     
    def __init__(self, image, font=cv2.FONT_HERSHEY_DUPLEX, color=(0,255,0)):
        self.image = image
        self.font = font
        self.colour = color

    
    def color_recognition(self, contours):
        # Extract colors from middle of shapes
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)
        color_names = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            coords = (int(x+w/2), int(y+h/2))
            color = image_hsv[coords[1], coords[0]]
            
            color_name = 'no color found'
            for i in range(len(self.color_ranges)):
                print(self.color_ranges[i][1])
                print(self.color_ranges[i][2])
                print(color[0])
                print('\n')
                if self.color_ranges[i][1] <= color[0] <= self.color_ranges[i][2]:
                    color_name = self.color_ranges[i][0]
                
            color_names.append(color_name)
            
        return color_names
    