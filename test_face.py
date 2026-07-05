from vision.camera import Camera
from vision.face_tracker import FaceTracker

import cv2

camera = Camera()
tracker = FaceTracker()

while True:

    frame = camera.get_frame()

    result = tracker.detect(frame)

    if result:

        x, y, w, h = result

        cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

    cv2.imshow("Face Tracker", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()