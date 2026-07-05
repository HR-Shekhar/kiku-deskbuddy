from picamera2 import Picamera2


class Camera:

    def __init__(self):

        self.camera = Picamera2()

        config = self.camera.create_preview_configuration(
            main={"size": (640, 480), "format": "RGB888"}
        )

        self.camera.configure(config)
        self.camera.start()

    def get_frame(self):
        return self.camera.capture_array()