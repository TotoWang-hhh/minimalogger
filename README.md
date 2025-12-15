# 📜 Minimalogger
A light logging module for Python softwares.

**2024 By rgzz666** | version: v0.1.4

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
Then you may want to add something to the log. By default, 5 log levels / types are available, which are:
- 🐞 Debug
- ℹ️ Info
- ⚠️ Warning
- ❌ Error
- 🛑 Critical

#### Customizing Log Levels
With the new features added in v0.1.3, you can now customize the log levels.

To edit it, change content of `LOG_LEVELS.LIST`. Each log level has a name and a level number. The names are stored in order of priority (low to high, and has a level number same as the index of their names in the list.

Currently, it is not suggested to change log levels during runtime, as this has not been tested yet. However, this is not disallowed, so you may still try it at your own risk.

#### Binding Events to Logs
Each of the log types will trigger function stored in `ON_LOGGED["<Name of the log type>"]`.

This allows a certain function or lambda expression be triggered when a certain type of log is logged (log is logged... hmm🤔).

See the [Popup or Report Your Errors](#popup-or-report-your-errors-optional) section for more.

#### Keeping Silent
If the log type has a level higher than the value set in `LOG_LEVEL`, it will be printed out. All logs will be written to log files.

#### Quick Log Functions
Starting from v0.1.3, these functions are created dynamically during the initialization of the log module. For each type of log, use `log.<Name of the log type>("<Your message>")` to log something. For instance, `log.info("Hello world")` for a hello world info message.

##### IDE Workarounds for Quick Log Functions
The quick log functions are usually automatically dynamically generated at runtime during module initialization. Starting from v0.1.4, the logging module will create a `.pyi` file to make functions like highlights, type hints, auto-completion... to work correctly. **Due to the mechanisms behind this feature, the logging module needs to be run once (either by running directly or being imported by other programs) everytime you change the list of log levels, to make your code looks right in IDE.**

In a more technically precise way: `Changing the list of log levels > Run the logging module once > A .pyi file generated > IDE uses the .pyi file for highlighting > Following IDE highlights works correctly`

### Popup or Report Your Errors (Optional)
As mentioned before, logs can trigger some certain functions when they are logged. By default, these functions binded to the logs simply returns None, but it can be set to anything.

These options are for showing your errors in UI, maybe in a popup or notification. You can simply modify the binded function by changing the value of `log.ON_LOGGED` dictionary, e.g. `log.ON_LOGGED["error"] = lambda message: some_function(message)`. Function stored in the varriables should require one or additional arguments to run. This is because the logging module will give your log message to the function by the first argument.

For example, the following code shows how to use `tkinter.messagebox` to popup errors in an actual program:
```python
log.ON_LOGGED["error"] = \
    lambda message: \
        tkinter.messagebox.showerror("Error", message)
```

After setting these values, all new log after this point will immediately take effect.

## 🧪 Testing
Since version v0.1.4, built-in testing contents are removed. For older versions of this module, you may read older versions of the document. The matching version of a document can be found right below the top heading.