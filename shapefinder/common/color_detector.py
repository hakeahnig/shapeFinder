import colorsys
import cv2


class ColorDetector:
    """Detects colors in shape middle
    """

    def __init__(self, color_ranges):
        # Name, lower range, upper range
        self.color_ranges = color_ranges

    def color_recognition(self, image, contours):
        """Detects color in middle of shape

        Args:
            image: Image to detect colors in
            contours: Contours of the already detected shapes

        Returns:
            _type_: Names of the colors, for which there were given contours
        """
        color_names = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            coords = (int(x + w / 2), int(y + h / 2)) #take middle of shape
            color = image[coords[1], coords[0]]
            color = colorsys.rgb_to_hsv(color[2] / 255, color[1] / 255, color[0] / 255)
            color_name = "empty"

            for i in range(len(self.color_ranges)):
                if self.color_ranges[i][1] <= color[0] * 360 <= self.color_ranges[i][2]:
                    color_name = self.color_ranges[i][0]

            color_names.append(color_name)

        return color_names
