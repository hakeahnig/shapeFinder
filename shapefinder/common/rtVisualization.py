import cv2
from dataLogging import logger
from datetime import datetime


class visualize:
    def __init__(self, image_path, font, colour):
        self.image_path = image_path
        self.font = font
        self.colour = colour
        self.time  = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def put_shape_on_image(self, image, contours):
        log = logger()
        for i, contour in enumerate(contours):
            if i == 0:
                continue
            
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            x, y, w, h = cv2.boundingRect(contour)

            coords = (int(x + w/3), int(y + h/1.5)) 

            if len(approx) == 3:
                cv2.putText(image, "Triangle", coords, self.font, 2, self.colour, 2)
                log.log_to_csv(self.time, None, "Triangle")

            elif len(approx) == 4:
                print(w)
                print(h)
                aspect_ratio = float(w)/h
                print(aspect_ratio)
                if aspect_ratio > 1.1:
                    cv2.putText(image, "Rectangle", coords, self.font, 2, self.colour, 2)
                    log.log_to_csv(self.time, None, "Rectangle")
                else:
                    cv2.putText(image, "Square", coords, self.font, 2, self.colour, 2)
                    log.log_to_csv(self.time, None, "Square")

            else:
                cv2.putText(image, "Circle", coords, self.font, 2, self.colour, 2)
                log.log_to_csv(self.time, None, "CIRCLE")

        #cv2.imshow("shapes_detected", image)

    def draw_contours(self, image, contours):
        for i, contour in enumerate(contours):
            if i == 0:
                continue
            
            cv2.drawContours(image, [contour], 0, (255, 0, 0), 8)

        #cv2.imshow("Contours", image)
  
    """def put_color_text(self, contours, color, label):
        image = cv2.imread(self.image_path)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
         """
           
    def combine_images(self, contours):
        #Combines images, maybe do logging here

        # Load the original image
        image = cv2.imread(self.image_path)

        # Create a blank image with the dimensions as the original image
        combined_image = image.copy()

        # Call the two functions to overlay their results on the same combined_image
        self.draw_contours(combined_image, contours)
        self.put_shape_on_image(combined_image, contours)

        # Show the combined image
        cv2.imshow("Combined Image", combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

