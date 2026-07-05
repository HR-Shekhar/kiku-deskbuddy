from vision.camera import Camera
import cv2

camera = Camera()

while True:

    frame = camera.get_frame()

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()