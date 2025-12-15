# 📜 Minimalogger
A light logging module for Python softwares.

**2024 By rgzz666** | version: v0.1.3

## ✨ Features
### Formatting
Each message is automatically formatted when logged. Time, tracing info and type will be automatically added to your logs.

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
Then you may want to add something to the log. Currently we have 5 types of log available by default, which are:
- 🐞 Debug
- ℹ️ Info
- ⚠️ Warning
- ❌ Error
- 🛑 Critical

With the new features added in recent updates, you can now add your own log level. As these operations are not tested and not stable, they will not be documented for now.

Each of the log types will trigger function stored in `ON_LOGGED["<Name of the log type>"]`. If the log type has a level higher than the value set in `LOG_LEVEL`, it will be printed out. All logs will be written to log files.

#### Quick Log Functions
Starting from v0.1.3, these functions are created dynamically during the initialization of the log module. For each type of log, use `log.<Name of the log type>("<Your message>")` to log something. For instance, `log.info("Hello world")` for a hello world info message.

##### IDE Workarounds for Quick Log Functions
The quick log functions are usually automatically dynamically generated while the module running. Starting from v0.1.4, the logging module will create a `.pyi` file to make functions like highlights, type hints, auto-completion... to work correctly. **Due to the mechanisms behind this feature, the logging module needs to be ran once (either by running directly or being imported by other programs) everytime you change the list of log levels, to make your code looks right in IDE.**

In a more technically precise way: `Changing the list of log levels > Run the logging module once > A .pyi file generated > IDE use the .pyi file for highlights > Following IDE highlights works correctly`

### Popup or Report Your Errors (Optional)
As I mentioned before, warning, error, and critical logs will trigger the given functions when they are logged. By default, these functions binded to the logs Just simply returns None, but it can be set to anything.

These options are for showing your errors in UI, maybe in a popup or notification. You can simply modify the binded function by changing the value of `log.ON_LOGGED` dictionary, e.g. `log.ON_LOGGED["error"] = lambda message: some_function(message)`. Function stored in the varriables should require one or additional arguments to run. This is because the logging module will give your log message to the function by the first argument.

For example, if I want to use tkinter.messagebox to show errors in my program, I should do: `log.ON_LOGGED["error"] = lambda message: tkinter.messagebox.showerror("Error", message)`.

## 🧪 Testing
Hey! Are you running this module directly? This should trigger the things under `if __name__ == "__main__":`, which is for testing purposes. These code will test every single function of this module, but may produce addtional files you may don't need. The `_test_log()` function is also a part of the testing function. You should not use `_test_log()` in your own code.
