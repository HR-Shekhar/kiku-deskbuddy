import cv2


class FaceTracker:

    def __init__(self):

        self.face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        faces = self.face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80),
        )

        if len(faces) == 0:
            return None

        x, y, w, h = faces[0]

        center_x = x + w // 2
        center_y = y + h // 2

        return center_x, center_y, frame.shape[1], frame.shape[0]