# This file just stores the robot's current state.
class RobotState:

    def __init__(self):

        self.left_eye_x = 40
        self.right_eye_x = 88

        self.eye_y = 32
        self.eye_radius = 12

        self.eye_offset_x = 0
        self.eye_offset_y = 0

        self.target_eye_offset_x = 0
        self.target_eye_offset_y = 0

        self.eye_open = 1.0
        self.target_eye_open = 1.0

        self.emotion = "neutral"