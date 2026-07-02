from display.oled import OLEDDisplay
from display.renderer import Renderer
from state.robot_state import RobotState
from animations.animator import Animator
from animations.idle import IdleBehavior

import time


def main():
    oled = OLEDDisplay()

    renderer = Renderer(oled.get_device())

    idle = IdleBehavior()

    robot = RobotState()
   
    animator = Animator()

    while True:
        idle.update(robot)
        animator.update(robot)
        renderer.render(robot)

        time.sleep(0.03)


if __name__ == "__main__":
    main()