# Minimalogger
# 2024 by rgzz666
# GitHub: github.com/TotoWang-hhh/minimalogger
_VERSION = "0.1.3"

from datetime import datetime
import inspect
import os
from typing import Union

class LOG_LEVELS:
    """Stores log levels and ways to convert them between levels and names."""
    ALL = -1
    LIST = ["debug", "info", "warning", "error", "critical"]
    def get_name(level:int) -> str:
        """Get the name of the log level with given level number. `[undefined]` if the level does not exist."""
        if level < 0 or level > len(LOG_LEVELS.LIST) - 1:
            log("error", "No such log type that matches the given level.")
            return "[UNDEFINED]"
        return LOG_LEVELS.LIST[level]
    def get_level(name:str) -> int:
        """Get the level number of the log level with given name. `[undefined]` if the level does not exist."""
        if name not in LOG_LEVELS.LIST:
            log("error", "No such log type with the given type name.")
            return "[UNDEFINED]"
        return LOG_LEVELS.LIST.index(name)
    def get_if_level_prints(level:Union[str, int]) -> bool:
        """Get whether the logs at a given level will be printed out or not."""
        global LOG_LEVEL
        if type(level) == str:
            level = LOG_LEVELS.get_level(level)
            if type(level) == str:
                return True
        min_level = LOG_LEVELS.get_level(LOG_LEVEL)
        return level >= min_level

def init_log_file(file_dir:str="./logs/") -> str:
    """Initialize a log file under a given directory, returns the path to the log file."""
    global CURR_LOG_FILE
    if file_dir in [None, "", 0, False]:
        file_dir = "./logs/"
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

def write_string(string:str) -> None:
    """Write a string to log file."""
    global CURR_LOG_FILE
    if CURR_LOG_FILE.upper() == "[UNDEFINED]":
        init_log_file(file_dir=("./logs/tests/log/" if __name__ == "__main__" else None))
    f = open(CURR_LOG_FILE, "a", encoding="utf-8")
    f.write(str(string)+"\n")
    f.close()
    return

def log(level:Union[int, str], msg:str, tracelevel:int=1, console_silent:Union[bool, None]=None, silent:bool=False) -> str:
    """Write a log to console and log file, returns the formatted log string."""
    if type(level) == str:
            if not level.lower() in ["debug", "info", "warning", "error", "critical"]:
                log("error", "Invalid log type!")
                return
    else:
        level = LOG_LEVELS.get_name(level)
        if level == "[UNDEFINED]":
            log("error", "Invalid log type!")
            return
    if console_silent == None:
        console_silent = not LOG_LEVELS.get_if_level_prints(level)
    source = f"{os.path.split(inspect.stack()[tracelevel][1])[1]} > " + \
             f"{inspect.stack()[tracelevel][3] + "()" if str(inspect.stack()[tracelevel][3]) != "<module>" else "ROOT"} > " + \
             f"Line {inspect.stack()[tracelevel][2]}"
    time_str = str(datetime.now())
    log_str = f"{time_str} [{level.upper()}] [{source}]: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if ON_LOGGED[level] != None and (not silent):
        ON_LOGGED[level](msg)
    return log_str

def create_quick_log_functions(log_types:list = LOG_LEVELS.LIST) -> None:
    """Creates quick log functions. Will be done automatically while the log module initializes."""
    for log_type in log_types:
        if log_type in globals():
            log("error", f"Quick log function log.{log_type}() has already existed as another function or variable! " + \
                "The quick log function for this log type will not work.")
            continue
        globals()[log_type] = lambda msg, silent=False, console_silent=not LOG_LEVELS.get_if_level_prints(log_type), \
            level=log_type: log(level, msg, silent=silent, console_silent=console_silent, tracelevel=2)

def _test_log() -> None:
    """This function is only for testing purposes, and will be UNDOCUMENTED. DO NOT USE IT IN YOUR OWN CASE!"""
    write_string("write_string() succeed.")
    log("debug", "Successfully logged an debug message.")
    log("info", "Successfully logged an info message.")
    log("warning", "Successfully logged an warning message.")
    log("error", "Successfully logged an error message.")
    log("critical", "Successfully logged an critical message.")
    info("Successfully logged an info message with quick log function.")
    return True

CURR_LOG_FILE = "[UNDEFINED]"
LOG_LEVEL = "info"
ON_LOGGED = {}
for level_name in LOG_LEVELS.LIST:
    ON_LOGGED[level_name] = lambda log: None

create_quick_log_functions()

log("info", f"Welcome from Minimalogger v{_VERSION} (Log initialized now)")

if __name__ == "__main__":
    # Prepare tkinter to show dialogs.
    import tkinter
    import tkinter.messagebox as msgbox
    window = tkinter.Tk()
    window.withdraw()
    window.update()
    # Bind things to do when error and warnings are logged.
    ON_LOGGED["warning"] = lambda msg: msgbox.showwarning("Warning triggered by ON_WARNING_LOGGED", msg)
    ON_LOGGED["error"] = lambda msg: msgbox.showerror("Error triggered by ON_ERROR_LOGGED", msg)
    ON_LOGGED["critical"] = lambda msg: msgbox.showerror("Warning triggered by ON_CRITICAL_LOGGED", msg)
    # Run tests
    test_result = _test_log()
    if test_result:
        print("=== DONE ===")
    else:
        print("=== Failed ===")
        if test_result != False:
            print("Reason(s): " + str(test_result))
        else:
            print("Reason(s): <Unknown>")
