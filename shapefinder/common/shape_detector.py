import cv2

class shape_detector:

    def __init__(self, image_path):
        self.image_path = image_path

    def shape_recognition(self):
        #Reads image and is looking for contours, maybe without return value, self??
        image = cv2.imread(self.image_path)

        #Gray conversion
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #Threshold
        _, threshold_image = cv2.threshold(grayscale_image, 210, 255, 0)

        #Getting contours
        contours, hierachy = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Bug fixing
        #cv2.imshow("grayscale", grayscale_image)
        #cv2.imshow("image", image)
        #cv2.imshow("threshold image", threshold_image)

        return contours


