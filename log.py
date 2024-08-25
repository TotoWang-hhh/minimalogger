# Minimalogger
# 2024 by rgzz666
_VERSION="0.1.2"

from datetime import datetime
import inspect
import os

class LOG_LEVELS:
    # Not implemented and undocumented
    # I just left these fxxking unimplemented stuff here but I actually don't know what to do with them.
    ALL=-32767
    DEBUG=-1
    INFO=0
    WARNING=1
    ERROR=2
    CRITICAL=3
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
                log.warn("Invalid log level!")
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
                log.error("Invalid log type name!")
                return "[UNDEFINED]"

def init_log_file(file_dir="./logs/"):
    global CURR_LOG_FILE
    if file_dir in [None,"",0,False]:
        file_dir="./logs/"
    file_dir.replace("\\","/")
    if not file_dir.endswith("/"):
        file_dir+="/"
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    time_str=str(datetime.now().strftime("%y%m%d-%H%M%S"))
    CURR_LOG_FILE=f"{file_dir}{time_str}.txt"
    f=open(CURR_LOG_FILE,"w",encoding="utf-8")
    f.write("")
    f.close()

def write_string(string):
    global CURR_LOG_FILE
    if CURR_LOG_FILE.upper()=="[UNDEFINED]":
        init_log_file(file_dir=("./logs/tests/log/" if __name__=="__main__" else None))
    f=open(CURR_LOG_FILE,"a",encoding="utf-8")
    f.write(str(string)+"\n")
    f.close()

def log(level,msg,tracelevel=1,console_silent=False,silent=False):
    if type(level) == str:
            if not level.lower() in ["debug","info","warning","error","critical"]:
                log.error("Invalid log type!")
                return
    else:
        level=LOG_LEVELS.get_name(level)
        if level=="[UNDEFINED]":
            log.error("Invalid log type!")
            return
    source=os.path.split(inspect.stack()[tracelevel][1])[1]+">"+inspect.stack()[tracelevel][3]+\
           ("()" if str(inspect.stack()[tracelevel][3])!="<module>" else "")+">"+"Line "+str(inspect.stack()[tracelevel][2])
    time_str=str(datetime.now())
    log_str=f"{time_str} [{level.upper()}] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if LOG_LEVELS.get_level(level)>=LOG_LEVELS.WARNING:
        if globals()[f"ON_{level.upper()}_LOGGED"]!=None and (not silent):
            globals()[f"ON_{level.upper()}_LOGGED"](msg)

def debug(msg,console_silent=True):
    log("debug",msg,console_silent=console_silent,tracelevel=2)

def info(msg,console_silent=False):
    log("info",msg,console_silent=console_silent,tracelevel=2)

def warn(msg,silent=False,console_silent=False):
    log("warning",msg,console_silent=console_silent,silent=silent,tracelevel=2)

def error(msg,silent=False,console_silent=False):
    log("error",msg,console_silent=console_silent,silent=silent,tracelevel=2)

def critical(msg,silent=False,console_silent=False):
    log("critical",msg,console_silent=console_silent,silent=silent,tracelevel=2)

def _test_log(): #This function is only for testing purposes, and will be UNDOCUMENTED. DO NOT USE IT IN YOUR OWN PROJECT!
    write_string("write_string() succeed.")
    debug("Successfully logged an debug message.")
    info("Successfully logged an info message.")
    warn("Successfully logged an warning message.")
    error("Successfully logged an error message.")
    critical("Successfully logged an critical message.")
    return True

CURR_LOG_FILE="[UNDEFINED]"
ON_ERROR_LOGGED=lambda log: None
ON_WARNING_LOGGED=lambda log: None
ON_CRITICAL_LOGGED=lambda log: None

info(f"Welcome from Minimalogger v{_VERSION}")

if __name__=="__main__":
    # Use tkinter to show dialogs.
    import tkinter
    import tkinter.messagebox as msgbox
    window=tkinter.Tk()
    window.withdraw()
    window.update()
    # Bind things to do when error and warnings are logged.
    ON_WARNING_LOGGED=lambda msg: msgbox.showwarning("Warning triggered by ON_WARNING_LOGGED",msg)
    ON_ERROR_LOGGED=lambda msg: msgbox.showerror("Error triggered by ON_ERROR_LOGGED",msg)
    ON_CRITICAL_LOGGED=lambda msg: msgbox.showerror("Warning triggered by ON_CRITICAL_LOGGED",msg)
    # Run tests
    test_result=_test_log()
    if test_result:
        print("=== DONE ===")
    else:
        print("=== Failed ===")
        if test_result!=False:
            print("Reason(s): "+str(test_result))
        else:
            print("Reason(s): <Unknown>")
