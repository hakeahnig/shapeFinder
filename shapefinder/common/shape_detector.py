import cv2

class shape_detector:

    def __init__(self, image_path):
        self.image_path = image_path

    def get_contours(self):
        image = cv2.imread(self.image_path)
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(grayscale_image, 210, 255, 0)
        contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if False:
            cv2.imshow("grayscale", grayscale_image)
            cv2.imshow("image", image)
            cv2.imshow("threshold image", threshold_image)

        return contours
    
    def evaluate_contours(self, contours):
        shape_list = 0
        shape = 0
        
        for i, contour in enumerate(contours):
            if i == 0:
                continue
            
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            x, y, w, h = cv2.boundingRect(contour)

            coords = (int(x + w/3), int(y + h/1.5)) 

            if len(approx) == 3:
                shape = 'Triangle'

            elif len(approx) == 4:
                print(w)
                print(h)
                aspect_ratio = float(w)/h
                print(aspect_ratio)
                if aspect_ratio > 1.1:
                    shape = 'Rectangle'
                else:
                    shape = 'Square'

            else:
                shape = 'circle'
                
            shape_list[i][0] = shape
            shape_list[i][1] = contour[i]
            
        return shape_list
