# It takes the robot's current state and draws a face.
from luma.core.render import canvas


class Renderer:
    def __init__(self, device):
        self.device = device

    def draw_eye(
        self,
        draw,
        center_x,
        center_y,
        radius,
        eye_open,
        offset_x,
        offset_y,
    ):

        x = center_x + offset_x
        y = center_y + offset_y

        vertical_radius = max(1, int(radius * eye_open))

        draw.ellipse(
            (
                x - radius,
                y - vertical_radius,
                x + radius,
                y + vertical_radius,
            ),
            outline="white",
            fill="white",
        )

    def render(self, state):

        with canvas(self.device) as draw:

            self.draw_eye(
                draw,
                state.left_eye_x,
                state.eye_y,
                state.eye_radius,
                state.eye_open,
                state.eye_offset_x,
                state.eye_offset_y,
            )

            self.draw_eye(
                draw,
                state.right_eye_x,
                state.eye_y,
                state.eye_radius,
                state.eye_open,
                state.eye_offset_x,
                state.eye_offset_y,
            )