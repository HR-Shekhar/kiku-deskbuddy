# This file just stores the robot's current state.

class RobotState:
    def __init__(self):
        self.left_eye_x = 40
        self.right_eye_x = 88
        self.eye_y = 32
        self.eye_radius = 12

        # Current position
        self.pupil_offset_x = 0
        self.pupil_offset_y = 0

        # Desired position
        self.target_pupil_offset_x = 0
        self.target_pupil_offset_y = 0

        self.eye_open = 1.0
        self.emotion = "neutral"