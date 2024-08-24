# 📜 Minimalogger
A light logging module for Python softwares.

## ✨ Features
### Formatting
Each message are automatically formatted when logged. Time, tracing info and type will be automatically added to your logs.

### Simple
Minimalogger is a really simple way to store and output logs. It only provides basic but enough functions for logging.

### Tracing
As text above has mentioned, tracing info, which contains the name of the file and function that triggers the log, will be automatically added to the formatted log.

## 📘 Basic Use
### Import
To use this log module, just place it under the directory of your program, and simply import it into your program like this:

```python
import log
```

### Setting Up a Log File (Optional)
By default, the logging module automatically creates log file under `./logs/`, and created this directory at the same time when `write_string()`, which is for writing lines to the log file, be triggered for the first time. Normally it happens when you log something for the first time.

To Cusomize the path of the log files, use `log.init_log_file(file_dir="<Directory to store the log files>")`. Then the logging module will automatically generate an empty new log file under the given directory, with the time created as the file name.

### Log Something
Then you may want to add something to the log. Currently we have 5 types of log available, which are:
- 🐞 Debug
- ℹ Info
- ⚠ Warning
- ❌ Error
- 🛑 Critical

#### Debug
Debug is a type of log which doesn't trigger and output anything by default, bug actually adds a log to the log file. This is for some detailed debug info. To add a debug log, use `log.debug(<Some text>)`.

#### Info
Info is a type of log which would be outputted and be written into the log file by default. This is for some normal information which is not too detailed and not too much to show, and doesn't contain any abnormal information. To add an info log, use `log.info("<Some text>")`.

#### Warning
Warning is a type of log which would trigger the function stored in `ON_WARNING_LOGGED` varriable, then be outputted to the console and be stored in the log file by default. This is for some warning messages which is not important enough to stop the program running normally. To add an warning log, use `log.warn("<Some text>")`.

#### Error
Error is a type of log which would trigger the function stored in `ON_ERROR_LOGGED` varriable, then be outputted to the console and be stored in the log file by default. This is for some unrecoverable or unignorable errors that stops the part of the program running normally. To add an error log, use `log.error("<Some text>")`.

#### Critical
Critical is a type of log which would trigger the function stored in `ON_CRITICAL_LOGGED` varriable, whne be outputted to the console and be stored in the log file by default. This is for some unnrecoverable and critical errors which makes the whole program stop working or run into panic. To add a critical log, use `log.critical("<Some text>")`.

### Popup Your Errors (Optional)
As I mentioned before, warning, error, and critical logs will trigger the given functions when they are logged. By default, these functions binded to the logs Just simply returns None, but it can be set to anything.

These options are for showing your errors in UI, maybe in a popup or notification. You can simply modify the binded function by changing the value of `log.ON_XXX_LOGGED` varriables. Function stored in the varriables should require one or additional arguments to run. This is because the logging module will give your log message to the function by the first argument.

For example, if I want to use tkinter.messagebox to show errors in my program, I should do: `log.ON_ERROR_LOGGED = lambda message: tkinter.messagebox.showerror("Error", message)`.
