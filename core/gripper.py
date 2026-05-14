from config import Config

class Gripper:

    def __init__(self, arm_api) -> None:
        self.arm = arm_api
        self.grip_position = Config.GRIPPER_MAX
    
    def initialize(self) -> None:
        self.arm.set_gripper_enable(True)
        self.arm.set_gripper_mode(0)
        self.arm.set_gripper_speed(3000)
        self.set(self.grip_position, wait=True)

    def set(self, position: int, wait: bool = False) -> None:
        self.grip_position = max(Config.GRIPPER_MIN, min(Config.GRIPPER_MAX, position))
        self.arm.set_gripper_position(self.grip_position, wait=wait)

    def open(self) -> None:
        self.set(Config.GRIPPER_MAX)

    def close(self) -> None:
        self.set(Config.GRIPPER_MIN)

    def step_open(self) -> None:
        self.set(self.grip_position + Config.GRIPPER_STEP)

    def step_close(self) -> None: 
        self.set(self.grip_position - Config.GRIPPER_STEP)
