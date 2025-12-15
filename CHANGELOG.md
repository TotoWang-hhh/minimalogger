# Changelog

## v0.1.4
### Added
- Workarounds for IDEs of quick logging functions (auto generation of a .pyi file).
- Clearer code comments.

### Changed
- Improved typing of minimalogger's internal code.

### Removed
- Testing functions.

## v0.1.3
### Added
- Added explanation for functions and classes.
- Added the support to dynamically add quick log functions, such as info(), warning(), etc. These functions will be created dynamically. afterwards.
- Added typing info.
- Log level setting support, which allows users to set a level and make logs below it silent.

### Changes
- Changed ON_XXX_LOGGED to a ON_LOGGED dictionary.
- Changed the way LOG_LEVELS works, now based on a list.
- Due to the previous change (dynamically creating quick log function), log.warn() is now renamed to log.warning().
- Slightly changed return value of some functions.
- Bug fixes.
- Small changes on trace info format.
- Code comment improvements

## v0.1.2
### Added
- `log()` function which requires log level and message and other paragram. It adds any types of log.
- `LOG_LEVELS.get_name()` and `LOG_LEVELS.get_level()` functions, which converts log levels to its names or converts them back.
- A welcome message at start or at import.

### Changed
- `debug()`, `info()`, `warn()`, `error()`, `critical()` now simply use `log()` to add logs.
- Some typo. :)
- Moved version from code comment to a global varriable.

## v0.1.1
### Added
- Critical log type.
- Documents in `README.md`.

### Removed
- The secondary confirmation of writing files at the start of the tests.

**Full Changelog**: https://github.com/TotoWang-hhh/minimalogger/commits/v0.1.1.

## v0.1.0
### Added
- Minimalogger itself.

**The very first version**
