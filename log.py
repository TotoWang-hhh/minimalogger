# Minimalogger
# 2024 by rgzz666
# GitHub: github.com/TotoWang-hhh/minimalogger
_VERSION = "0.1.2"

from datetime import datetime
import inspect
import os

class LOG_LEVELS:
    # Not implemented and undocumented
    ALL = -32768
    DEBUG = -1
    INFO = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3
    def get_name(level):
        match level:
            case LOG_LEVELS.DEBUG:
                return "debug"
            case LOG_LEVELS.INFO:
                return "info"
            case LOG_LEVELS.WARNING:
                return "warning"
            case LOG_LEVELS.ERROR:
                return "errors"
            case LOG_LEVELS.CRITICAL:
                return "critical"
            case _:
                error("No such log type that matches the given level.")
                return "[UNDEFINED]"
    def get_level(name):
        match name.lower():
            case "debug":
                return LOG_LEVELS.DEBUG
            case "info":
                return LOG_LEVELS.INFO
            case "warning":
                return LOG_LEVELS.WARNING
            case "error":
                return LOG_LEVELS.ERROR
            case "critical":
                return LOG_LEVELS.CRITICAL
            case _: 
                error("No such log type with the given type name.")
                return "[UNDEFINED]"
    def get_if_level_prints(level_name):
        global LOG_LEVEL
        level = LOG_LEVELS.get_level(level_name)
        min_level = LOG_LEVELS.get_level(LOG_LEVEL)
        return level >= min_level

def init_log_file(file_dir="./logs/"):
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

def write_string(string):
    global CURR_LOG_FILE
    if CURR_LOG_FILE.upper() == "[UNDEFINED]":
        init_log_file(file_dir=("./logs/tests/log/" if __name__ == "__main__" else None))
    f = open(CURR_LOG_FILE, "a", encoding="utf-8")
    f.write(str(string)+"\n")
    f.close()

def log(level, msg, tracelevel=1, console_silent=None, silent=False):
    if type(level) == str:
            if not level.lower() in ["debug", "info", "warning", "error", "critical"]:
                error("Invalid log type!")
                return
    else:
        level = LOG_LEVELS.get_name(level)
        if level == "[UNDEFINED]":
            error("Invalid log type!")
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
    if LOG_LEVELS.get_level(level) >= LOG_LEVELS.WARNING:
        if globals()[f"ON_{level.upper()}_LOGGED"] != None and (not silent):
            globals()[f"ON_{level.upper()}_LOGGED"](msg)

def debug(msg, console_silent=None):
    log("debug", msg, console_silent=console_silent, tracelevel=2)

def info(msg, console_silent=None):
    log("info", msg, console_silent=console_silent, tracelevel=2)

def warn(msg, silent=False, console_silent=None):
    log("warning", msg, console_silent=console_silent, silent=silent, tracelevel=2)

def error(msg, silent=False, console_silent=None):
    log("error", msg, console_silent=console_silent, silent=silent, tracelevel=2)

def critical(msg, silent=False, console_silent=None):
    log("critical", msg, console_silent=console_silent, silent=silent, tracelevel=2)

def _test_log(): #This function is only for testing purposes, and will be UNDOCUMENTED. DO NOT USE IT IN YOUR OWN CASE!
    write_string("write_string() succeed.")
    debug("Successfully logged an debug message.")
    info("Successfully logged an info message.")
    warn("Successfully logged an warning message.")
    error("Successfully logged an error message.")
    critical("Successfully logged an critical message.")
    return True

CURR_LOG_FILE = "[UNDEFINED]"
LOG_LEVEL = "info"
ON_ERROR_LOGGED = lambda log: None
ON_WARNING_LOGGED = lambda log: None
ON_CRITICAL_LOGGED = lambda log: None

info(f"Welcome from Minimalogger v{_VERSION}")

if __name__ == "__main__":
    # Prepare tkinter to show dialogs.
    import tkinter
    import tkinter.messagebox as msgbox
    window = tkinter.Tk()
    window.withdraw()
    window.update()
    # Bind things to do when error and warnings are logged.
    ON_WARNING_LOGGED = lambda msg: msgbox.showwarning("Warning triggered by ON_WARNING_LOGGED", msg)
    ON_ERROR_LOGGED = lambda msg: msgbox.showerror("Error triggered by ON_ERROR_LOGGED", msg)
    ON_CRITICAL_LOGGED = lambda msg: msgbox.showerror("Warning triggered by ON_CRITICAL_LOGGED", msg)
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
