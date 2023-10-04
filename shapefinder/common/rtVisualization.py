import cv2
from datetime import datetime


class visualize:
    def __init__(self, image_path, font, colour):
        self.image_path = image_path
        self.font = font
        self.colour = colour
        self.time  = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def put_shape_on_image(self, image, contours, shapes, coordinates):
        for i, contour in enumerate(contours):

            cv2.putText(image, shapes[i], coordinates[i], self.font, 3, self.colour, 4 )

            """if len(approx) == 3:
                cv2.putText(image, "Triangle", coords, self.font, 2, self.colour, 2)

            elif len(approx) == 4:
                aspect_ratio = float(w)/h
                if aspect_ratio > 1.1:
                    cv2.putText(image, "Rectangle", coords, self.font, 2, self.colour, 2)
                    
                else:
                    cv2.putText(image, "Square", coords, self.font, 2, self.colour, 2)

            else:
                cv2.putText(image, "Circle", coords, self.font, 2, self.colour, 2)"""

        #cv2.imshow("shapes_detected", image)

    def draw_contours(self, image, contours):
        for i, contour in enumerate(contours):
            
            cv2.drawContours(image, [contour], 0, (255, 0, 0), 8)

        #cv2.imshow("Contours", image)
  
    """def put_color_text(self, contours, color, label):
        image = cv2.imread(self.image_path)

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
         """
           
    def combine_images(self, contours, shapes, coordinates):
        #Combines images, maybe do logging here

        # Load the original image
        image = cv2.imread(self.image_path)

        # Create a blank image with the dimensions as the original image
        combined_image = image.copy()

        # Call the two functions to overlay their results on the same combined_image
        self.draw_contours(combined_image, contours)
        self.put_shape_on_image(combined_image, contours, shapes, coordinates)

        # Show the combined image
        cv2.imshow("Combined Image", combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

