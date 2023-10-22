import cv2

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