from gamepad import Gamepad
from config import Config

def test_gamepad_connection():
    gamepad = Gamepad()
    try:
        gamepad.connect()
        assert gamepad.joystick is not None, "Joystick should be initialized"
    finally:
        gamepad.disconnect()

def test_gamepad_axes():
    
    gamepad = Gamepad()
    try:
        gamepad.connect()
        for axis in [Config.AXIS_X, Config.AXIS_Y, Config.AXIS_RIGHT_X, Config.AXIS_RIGHT_Y, Config.AXIS_L2, Config.AXIS_R2]:
            value = gamepad.joystick.get_axis(axis)
            assert -1.0 <= value <= 1.0, f"Axis {axis} value {value} out of range"
    finally:
        gamepad.disconnect()

test_gamepad_axes()