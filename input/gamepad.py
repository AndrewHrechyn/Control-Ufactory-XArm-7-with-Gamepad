import sys
import pygame
from config import Config

class Gamepad:
    
    def __init__(self) -> None:
        self.joystick = None

    def connect(self) -> None:
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print("No joystick controller found!")
            sys.exit()

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print(f"Joystick controller: {self.joystick.get_name()}")

    def disconnect(self) -> None:
        pygame.quit()
        print("Joystick is disconnected!")
