# It takes the robot's current state and draws a face.

from luma.core.render import canvas


class Renderer:
    def __init__(self, device):
        self.device = device

    def draw_eye(self, draw, center_x, center_y, radius):
        draw.ellipse(
            (
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
            ),
            outline="white",
            fill="black",
        )

    def draw_pupil(self, draw, center_x, center_y, offset_x, offset_y):
        pupil_radius = 3

        draw.ellipse(
            (
                center_x + offset_x - pupil_radius,
                center_y + offset_y - pupil_radius,
                center_x + offset_x + pupil_radius,
                center_y + offset_y + pupil_radius,
            ),
            outline="white",
            fill="white",
        )

    def render(self, state):
        with canvas(self.device) as draw:

            # Left Eye
            self.draw_eye(
                draw,
                state.left_eye_x,
                state.eye_y,
                state.eye_radius,
            )

            self.draw_pupil(
                draw,
                state.left_eye_x,
                state.eye_y,
                state.pupil_offset_x,
                state.pupil_offset_y,
            )

            # Right Eye
            self.draw_eye(
                draw,
                state.right_eye_x,
                state.eye_y,
                state.eye_radius,
            )

            self.draw_pupil(
                draw,
                state.right_eye_x,
                state.eye_y,
                state.pupil_offset_x,
                state.pupil_offset_y,
            )