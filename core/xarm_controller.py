import time
from config import Config
from xarm.wrapper import XArmAPI

class XArmController:
    def __init__(self, ip_address : str) -> None:
        self.ip_address = ip_address
        self.arm : XArmAPI = None

    def connect(self) -> bool:
        try:
            self.arm = XArmAPI(self.ip_address)
            self.arm.set_collision_sensitivity(3)
            self.arm.clean_error()
            self.arm.motion_enable(enable=True)
            self.arm.set_mode(0)
            self.arm.set_state(0)
            time.sleep(1)  # Allow time for the arm to initialize
            print(f"Connected to XArm at {self.ip_address}")
            return True
        except Exception as e:
            print(f"Failed to connect to XArm at {self.ip_address}: {e}")
            return False
        
    def disconnect(self) -> None:
        if self.arm: 
            self.stop()
            self.arm.disconnect()

    def get_home(self) -> None:
        self.arm.set_mode(0)
        self.arm.set_state(0)
        self.arm.set_servo_angle(
            angle=Config.HOME_POSITION, 
            speed=Config.DEFAULT_VELOCITY,
            is_radian=False,
            wait=True
        )
        print(f"Moved to initial home position: {(Config.HOME_POSITION).join(', ')}")

    def set_velocity(self, vx, vy, vz, vroll, vpitch, vyaw) -> None:
        self.arm.set_mode(5)
        self.arm.set_state(0)
        self.arm.vc_set_cartesian_velocity(
            [vx, vy, vz, vroll, vpitch, vyaw]
        )
    
    def stop(self) -> None:
        self.arm.vc_set_cartesian_velocity([0, 0, 0, 0, 0, 0])
        self.arm.set_state(0)

    def move_arc_lines(self, positions, speed=Config.DEFAULT_VELOCITY) -> None:
        self.arm.set_mode(0)
        self.arm.set_state(0)
        self.arm.move_arc_lines(
            positions=positions,
            speed=speed,
            is_radian=False,
            wait=True
        )

    @property
    def position(self) -> list:
        return self.arm.get_position() if self.arm else None
    
    @property
    def has_error(self) -> bool:
        return self.arm.get_err_code() != 0 if self.arm else True
    