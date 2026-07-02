import random
import time


class IdleBehavior:
    def __init__(self):
        self.next_change = time.time()

    def update(self, robot):
        now = time.time()

        if now < self.next_change:
            return

        robot.target_pupil_offset_x = random.randint(-6, 6)
        robot.target_pupil_offset_y = random.randint(-4, 4)

        self.next_change = now + random.uniform(1.5, 3.0)