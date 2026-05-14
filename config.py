

class Config:
    ARM_IP = "192.168.1.XXX"
    HOME_POSITION = [0.0, 15.0, -150.0, 150.0, 0.0, 75.0, 0.0]

    # Gamepad configuration
    AXIS_X = 0  # Left stick horizontal
    AXIS_Y = 1  # Left stick vertical
    AXIS_RIGHT_X = 3  # Right stick horizontal
    AXIS_RIGHT_Y = 4  # Right stick vertical
    AXIS_L2 = 2
    AXIS_R2 = 5

    # Buttons
    BUTTON_A = 0
    BUTTON_B = 1
    BUTTON_Y = 3
    BUTTON_LB = 4
    BUTTON_RB = 5

    # Motion 
    DEFAULT_VELOCITY = 100.0
    DEFAULT_INCREMENT = 5.0
    GRIPPER_STEP = 50.0
    GRIPPER_MAX = 850 
    GRIPPER_MIN = -10
    DEADZONE = 0.2

    POSITION_FILE = "assets/positions.xlsx"