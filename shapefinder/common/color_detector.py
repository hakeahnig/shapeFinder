import colorsys
import cv2


class ColorDetector:
    # Name, lower range, upper range
    color_ranges = [
        ["red", 0, 41],
        ["yellow", 41, 70],
        ["green", 71, 180],
        ["blue", 181, 280],
        ["purple", 260, 360],
    ]

    def __init__(self, font=cv2.FONT_HERSHEY_DUPLEX, color=(0, 255, 0)):
        self.font = font
        self.colour = color

    def color_recognition(self, image, contours):
        # Extract colors from middle of shapes
        color_names = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            coords = (int(x + w / 2), int(y + h / 2))
            color = image[coords[1], coords[0]]
            color = colorsys.rgb_to_hsv(color[2] / 255, color[1] / 255, color[0] / 255)
            color_name = "empty"

            for i in range(len(self.color_ranges)):
                if self.color_ranges[i][1] <= color[0] * 360 <= self.color_ranges[i][2]:
                    color_name = self.color_ranges[i][0]

            color_names.append(color_name)

        return color_names
