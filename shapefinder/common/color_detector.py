import numpy as np
import cv2

class color_detector:
    def __init__(self, image_path, font=cv2.FONT_HERSHEY_DUPLEX, colour=(0,255,0)):
        self.image_path = image_path
        self.font = font
        self.colour = colour

    def read_image(self, cam_port):
        cam = cv2.VideoCapture(cam_port)
        while True:
            ret, image = cam.read()

            if ret == True:
                cv2.imshow("VIDEO INPUT", image)
                input_key = cv2.waitKey(20)
                if input_key == ord("q"):
                    break

        cam.release()
        cv2.destroyAllWindows()
    
    def color_recognition(self):
        #Reads image and applies masks in hsv colorm room, not finished, stupid red end violet

        image = cv2.imread(self.image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Create a blank image with the same dimensions as the original image
        hsv_image = image.copy()

        #Color Definition
        #RED
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        #YELLOW
        lower_yellow = np.array([25, 100, 100])
        upper_yellow = np.array([35, 255, 255])

        #GREEN
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])

        #BLUE
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        #VIOLET
        lower_violet = np.array([135, 50, 50])
        upper_violet = np.array([160, 255, 255])

        #MASKS
        red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
        yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
        green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
        blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        violet_mask = cv2.inRange(hsv_image, lower_violet, upper_violet)

        #BUGFIXXING 
        """cv2.imshow("HSV IMAGE", hsv_image)
        cv2.imshow("Red_mask", red_mask)
        cv2.imshow("violet_mask", violet_mask)
        cv2.imshow("yellow", yellow_mask)
        cv2.imshow("greem_mask", green_mask)
        cv2.imshow("blue_mask", blue_mask)
        cv2.waitKey(0)"""
        
        #CONTOURS
        red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        violet_contours, _ = cv2.findContours(violet_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        """#NOT IN USE YET
        color_contour_array = [red_contours, yellow_contours, green_contours, blue_contours, violet_contours]
        color_names = ["red", "yellow", "green", "blue", "violet"]
        ##

        def put_color_text(image, contours, color, label):
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        put_color_text(image, red_contours, self.colour, "Red")
        put_color_text(image, yellow_contours, self.colour, "Yellow")
        put_color_text(image, green_contours, self.colour, "Green")
        put_color_text(image, blue_contours, self.colour, "Blue")
        put_color_text(image, violet_contours, self.colour, "Violet")

        cv2.imshow("colors", image_with_text)

        return color_contour_array, color_names"""
        

    

