import random
import time

import random
import time


class BlinkBehavior:

    def __init__(self):

        self.next_blink = time.time() + random.uniform(2,5)

        self.closing = False

        self.open_time = 0

    def update(self, robot):

        now = time.time()

        if not self.closing and now > self.next_blink:

            robot.target_eye_open = 0

            self.closing = True

            self.open_time = now + 0.15

        elif self.closing and now > self.open_time:

            robot.target_eye_open = 1

            self.closing = False

            self.next_blink = now + random.uniform(2,5)