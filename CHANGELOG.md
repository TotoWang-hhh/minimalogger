# Changelog

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
- The secondary confirmation of writing files at the start of the tests

**Full Changelog**: https://github.com/TotoWang-hhh/minimalogger/commits/v0.1.1.

## v0.1.0
**The very first version**
