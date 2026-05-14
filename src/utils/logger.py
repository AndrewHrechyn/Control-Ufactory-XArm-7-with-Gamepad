import logging
import os
from pathlib import Path

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:
            log_dir = Path(__file__).parent.parent.parent / "log"
            log_dir.mkdir(exist_ok=True)
            
            log_file = log_dir / "robot.log"
            
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message, exc_info=False):
        self.logger.error(message, exc_info=exc_info)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)
        
    def log(self, message):
        self.logger.info(message)
