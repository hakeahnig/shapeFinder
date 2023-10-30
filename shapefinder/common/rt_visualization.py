import cv2


class Visualize:
    """Visualization class

    Visualization for shape contours, detected colors
    and detected shapes

    Attributes:
        font: Font to be used when displaying text overlay
        color: Color of overlay

    """

    def __init__(self, font, color):
        self.font = font
        self.color = color

    def put_shape_name_on_image(self, image, shapes, coordinates):
        """Renders shape name on image

        Args:
            image: Original image to overlay onto
            shapes: array of shape names
            coordinates: coordinates of shapes on image
        """
        for i, shape in enumerate(shapes):
            cv2.putText(image, shape, coordinates[i], self.font, 3, self.color, 4)

    def put_color_name_on_image(self, image, colors, coordinates):
        """Renders colors on image

        Args:
            image: Original image to overlay onto
            colors: array of color names
            coordinates: coordinates of shapes on image
        """
        for i, color in enumerate(colors):
            print("ur coordinates", coordinates[i][0], coordinates[i][1] + 35)
            cv2.putText(
                image,
                color,
                (coordinates[i][0], coordinates[i][1] + 35),
                self.font,
                3,
                self.color,
                4,
            )

    def draw_contours(self, image, contours):
        """Renders contours of shapes onto image

        Args:
            image: Original image to overlay onto
            contours: array containing shape contours, one shape per element
        """
        for i, contour in enumerate(contours):
            cv2.drawContours(image, [contour], 0, self.color, 8)

    def combine_images(self, image, contours, shapes, coordinates, colors):
        """Renders all the names and shapes onto image

        Args:
            image Image to overlay onto
            contours: Array containing shape contours, one shape per element
            shapes: array of all the shape names
            coordinates: array of all the shape origins
            colors: array of all the color names

        Returns:
            combined_image: image with overlay
        """
        combined_image = image.copy()
        self.draw_contours(combined_image, contours)
        self.put_shape_name_on_image(combined_image, shapes, coordinates)
        self.put_color_name_on_image(combined_image, colors, coordinates)

        return combined_image
