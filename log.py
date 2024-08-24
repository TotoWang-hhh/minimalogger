# Minimalogger v0.1.1
# 2024 by rgzz666

from datetime import datetime
import inspect
import os

class LOG_LEVELS:
    # Not implented and undocumented
    # I just left these fxxking unimplented stuff here but I actually don't know what to do with them.
    ALL=-32767
    DEBUG=-1
    INFO=0
    WARNING=1
    ERROR=2
    CRITICAL=3

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

def debug(msg,console_silent=True):
    source=os.path.split(inspect.stack()[1][1])[1]+">"+inspect.stack()[1][3]+("()" if str(inspect.stack()[1][3])!="<module>" else "")+">"+inspect.stack()[1][2]
    print(inspect.stack()[1])
    time_str=str(datetime.now())
    log_str=f"{time_str} [DEBUG] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)

def info(msg,console_silent=False):
    source=os.path.split(inspect.stack()[1][1])[1]+">"+inspect.stack()[1][3]+("()" if str(inspect.stack()[1][3])!="<module>" else "")
    time_str=str(datetime.now())
    log_str=f"{time_str} [INFO] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)

def warn(msg,silent=False,console_silent=False):
    source=os.path.split(inspect.stack()[1][1])[1]+">"+inspect.stack()[1][3]+("()" if str(inspect.stack()[1][3])!="<module>" else "")
    time_str=str(datetime.now())
    log_str=f"{time_str} [WARNING] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if ON_WARNING_LOGGED!=None and (not silent):
        ON_WARNING_LOGGED(msg)

def error(msg,silent=False,console_silent=False):
    source=os.path.split(inspect.stack()[1][1])[1]+">"+inspect.stack()[1][3]+("()" if str(inspect.stack()[1][3])!="<module>" else "")
    time_str=str(datetime.now())
    log_str=f"{time_str} [ERROR] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if ON_ERROR_LOGGED!=None and (not silent):
        ON_ERROR_LOGGED(msg)

def critical(msg,silent=False,console_silent=False):
    source=os.path.split(inspect.stack()[1][1])[1]+">"+inspect.stack()[1][3]+("()" if str(inspect.stack()[1][3])!="<module>" else "")
    time_str=str(datetime.now())
    log_str=f"{time_str} [CRITICAL] {source}: {msg}"
    if not console_silent:
        print(log_str)
    write_string(log_str)
    if ON_CRITICAL_LOGGED!=None and (not silent):
        ON_CRITICAL_LOGGED(msg)

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
