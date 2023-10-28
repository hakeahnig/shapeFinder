import cv2


class ShapeDetector:
    def __init__(self):
        pass

    def get_contours(self, image):
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(grayscale_image, 210, 255, 0)
        contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[1:]
        return contours

    def evaluate_contours(self, contours):
        shapes = []
        coordinates = []

        for i, contour in enumerate(contours):
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            x, y, w, h = cv2.boundingRect(contour)
            coords = [int(x), int(y)]

            if len(approx) == 3:
                shape = "Triangle"

            elif len(approx) == 4:
                aspect_ratio = float(w) / h
                if aspect_ratio > 1.1:
                    shape = "Rectangle"
                else:
                    shape = "Square"

            else:
                shape = "Circle"

            shapes.append(shape)
            coordinates.append(coords)

        # print("urgodman shapes: ", shapes)
        return shapes, coordinates
