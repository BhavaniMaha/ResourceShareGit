from .utils import MetaSingleton
from enum import Enum

class LevelEnum(Enum):
    info = 'INFO'
    critical = 'CRITICAL'
    error = 'ERROR'
    warning = 'WARNING'
    
    # TODO : Add more options(ERROR; WARN)
    

class Logging(metaclass=MetaSingleton):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def _write_log(self, level, msg: str) -> None:
        """Write to the log file"""
        
        with open(self.file_name, 'a') as log_file:
            log_file.write(f'[{level.name}] {msg}\n') # [CRITICAL] msg goes here..
    
    # create level specific methods     
    def info(self,msg):
        self._write_log(LevelEnum.info, msg)
    
    # TODO: Add more level specific methods     
    # - CRITICAL
    # - ERROR
    # - WARNING
    
    def critical(self, msg):
        self._write_log(LevelEnum.CRITICAL, msg)
        
    def error(self, msg):
        self._write_log(LevelEnum.ERROR, msg)
        
    def warning(self, msg):
        self._write_log(LevelEnum.WARNING, msg)
