# Minimalogger
# 2024 by rgzz666
# GitHub: github.com/TotoWang-hhh/minimalogger
_VERSION = "0.1.4"

from datetime import datetime
import inspect
import os
import typing

class LOG_LEVELS:
    """Stores log levels and ways to convert them between levels and names."""

    ALL = -1
    LIST = ["debug", "info", "warning", "error", "critical"]

    @staticmethod
    def get_name(
        level:int
        ) -> str:
        """Get the name of the log level with given level number. `[undefined]` if the level does not exist."""
        if level < 0 or level > len(LOG_LEVELS.LIST) - 1:
            log("error", "No such log type that matches the given level.")
            return "[UNDEFINED]"
        return LOG_LEVELS.LIST[level]
    
    @staticmethod
    def get_level(
        name:str
        ) -> int:
        """Get the level number of the log level with given name. `[undefined]` if the level does not exist."""
        if name not in LOG_LEVELS.LIST:
            log("error", "No such log type with the given type name.")
            return -1
        return LOG_LEVELS.LIST.index(name)
    
    @staticmethod
    def get_if_level_prints(
        level:str | int
        ) -> bool:
        """Get whether the logs at a given level will be printed out or not."""
        global LOG_LEVEL
        if type(level) is str:
            level = LOG_LEVELS.get_level(level)
            if level == -1:
                return True
        min_level = LOG_LEVELS.get_level(LOG_LEVEL)
        assert type(level) is int
        return level >= min_level

def init_log_file(
        file_dir: typing.Optional[str] = "./logs/"
        ) -> str:
    """Initialize a log file under a given directory, returns the path to the log file."""
    global CURR_LOG_FILE
    # Handle if nothing passed
    if file_dir == None:
        file_dir = "./logs/"
    # Make it a standard path
    file_dir.replace("\\", "/")
    if not file_dir.endswith("/"):
        file_dir += "/"
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    time_str = str(datetime.now().strftime("%y%m%d-%H%M%S"))
    CURR_LOG_FILE = f"{file_dir}{time_str}.txt"
    f = open(CURR_LOG_FILE, "w", encoding="utf-8")
    f.write("")
    f.close()
    return file_dir

def write_string(
        string:str
        ) -> None:
    """Write a string to log file."""
    global CURR_LOG_FILE
    if CURR_LOG_FILE.upper() == "[UNDEFINED]":
        init_log_file(file_dir="./logs/tests/log/" if __name__ == "__main__" else None)
    f = open(CURR_LOG_FILE, "a", encoding="utf-8")
    f.write(str(string)+"\n")
    f.close()
    return

def log(
        level: int | str, 
        msg: str, 
        tracelevel: int=1, 
        console_silent: bool | None=None, 
        silent: bool=False
        ) -> str:
    """Write a log to console and log file, returns the formatted log string."""
    if type(level) is str:
            if not level.lower() in LOG_LEVELS.LIST:
                log("error", "Invalid log type!")
                return ""
    elif type(level) is int:
        level = LOG_LEVELS.get_name(level)
        if level == "[UNDEFINED]":
            log("error", "Invalid log type!")
            return ""
    else:
        log("error", "Invalid value for parameter log type!")
    assert type(level) is str
    if console_silent == None:
        console_silent = not LOG_LEVELS.get_if_level_prints(level)
    source = f"{os.path.split(inspect.stack()[tracelevel][1])[1]} > " # File path
    source += inspect.stack()[tracelevel][3] + '()' if \
              str(inspect.stack()[tracelevel][3]) != '<module>' else 'ROOT' + " > " # Module
    source += f"Line {inspect.stack()[tracelevel][2]}" # Line no.
    time_str = str(datetime.now())
    log_str = f"{time_str} [{level.upper()}] [{source}]: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if ON_LOGGED[level] != None and (not silent):
        ON_LOGGED[level](msg)
    return log_str

def create_quick_log_functions(
        log_types: list = LOG_LEVELS.LIST
        ) -> None:
    """Creates quick log functions. Will be done automatically while the log module initializes."""
    for log_type in log_types:
        if log_type in globals():
            log("error", f"Quick log function log.{log_type}() has already existed as another "
                "function or variable! The quick log function for this log type will not work.")
            continue
        globals()[log_type] = lambda msg, silent=False, \
            console_silent=not LOG_LEVELS.get_if_level_prints(log_type), \
            level=log_type: \
                log(level, msg, silent=silent, console_silent=console_silent, tracelevel=2)

CURR_LOG_FILE = "[UNDEFINED]"
LOG_LEVEL = "info"
ON_LOGGED = {}
for level_name in LOG_LEVELS.LIST:
    ON_LOGGED[level_name] = lambda log: None

create_quick_log_functions()

log("info", f"Welcome from Minimalogger v{_VERSION} (Log initialized now)") # Initial welcome info

with open("log.pyi", "w", encoding="utf-8") as f:
    for level in LOG_LEVELS.LIST:
        f.write(
            f"def {level}(msg: str, silent: bool = False) -> None: ...\n"
        )

if typing.TYPE_CHECKING: # If is type checking, then create quick log functions anyway
    for level_name in LOG_LEVELS.LIST:
        globals()[level_name] = typing.Callable[[str, bool], None]

if __name__ == "__main__":
    log("info", f"Welcome to minimalogger! You may include this module in your big deal.")
