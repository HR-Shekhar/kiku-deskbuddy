class Animator:

    def update(self, robot):

        move_speed = 1
        blink_speed = 0.15

        # Eye X
        if robot.eye_offset_x < robot.target_eye_offset_x:
            robot.eye_offset_x += move_speed
        elif robot.eye_offset_x > robot.target_eye_offset_x:
            robot.eye_offset_x -= move_speed

        # Eye Y
        if robot.eye_offset_y < robot.target_eye_offset_y:
            robot.eye_offset_y += move_speed
        elif robot.eye_offset_y > robot.target_eye_offset_y:
            robot.eye_offset_y -= move_speed

        # Blink
        if robot.eye_open < robot.target_eye_open:
            robot.eye_open = min(
                robot.eye_open + blink_speed,
                robot.target_eye_open,
            )

        elif robot.eye_open > robot.target_eye_open:
            robot.eye_open = max(
                robot.eye_open - blink_speed,
                robot.target_eye_open,
            )