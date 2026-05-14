import os
import sys 
import time



from xarm.wrapper import XArmAPI


class XArmController:
    def __init__(self, ip_address : str, home_position = None, gripper_position = None) -> None:
        self.ip_address = ip_address
        self.home_position = home_position or [0.0, 15.0, -150.0, 150.0, 0.0, 75.0, 0.0]
        self.arm = None
        self.joystick = None
        self.gripper_position = gripper_position or 850.0

    def initialize_arm(self):
        self.arm = XArmAPI(self.ip_address)
        

    pass