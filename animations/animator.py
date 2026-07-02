class Animator:

    def update(self, robot):

        speed = 1

        # X movement
        if robot.pupil_offset_x < robot.target_pupil_offset_x:
            robot.pupil_offset_x += speed
        elif robot.pupil_offset_x > robot.target_pupil_offset_x:
            robot.pupil_offset_x -= speed

        # Y movement
        if robot.pupil_offset_y < robot.target_pupil_offset_y:
            robot.pupil_offset_y += speed
        elif robot.pupil_offset_y > robot.target_pupil_offset_y:
            robot.pupil_offset_y -= speed