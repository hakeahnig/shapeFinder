import cv2


class Visualize:
    def __init__(self, font, colour):
        self.font = font
        self.colour = colour

    def put_shape_on_image(self, image, contours, shapes, coordinates):
        for i, contour in enumerate(contours):
            cv2.putText(image, shapes[i], coordinates[i], self.font, 3, self.colour, 4)

    def put_color_name_on_image(self, image, colors, coordinates, contours):
        for i, contour in enumerate(contours):
            print("ur coordinates", coordinates[i][0], coordinates[i][1] + 35)
            cv2.putText(image, colors[i], (coordinates[i][0], coordinates[i][1] + 35),
                self.font, 3, self.colour, 4)

    def draw_contours(self, image, contours):
        for i, contour in enumerate(contours):
            cv2.drawContours(image, [contour], 0, (255, 0, 0), 8)

    def combine_images(self, image, contours, shapes, coordinates, colors):
        combined_image = image.copy()
        self.draw_contours(combined_image, contours)
        self.put_shape_on_image(combined_image, contours, shapes, coordinates)
        self.put_color_name_on_image(combined_image, colors, coordinates, contours)

        return combined_image
