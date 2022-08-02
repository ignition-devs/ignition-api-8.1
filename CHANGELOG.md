## v8.1.19.post2 (2022-08-02)

### Fix

- **system**: fix args and return type of tag.query (#49)

## v8.1.19.post1 (2022-08-01)

### Fix

- **ia**: make class' properties accessible (#48)

### Refactor

- **java**: move classproperty class (#46)

## v8.1.19 (2022-07-29)

### Feat

- **system**: add new perspective and tag functions (#44)
- **system**: add constants to __all__ (#43)
- improve type hints (#39)
- **ia**: add type hints to all PyUser functions (Sourcery refactored) (#38)
- **system**: add db constants to __all__ (#36)

### Fix

- **java**: rollback change on classproperty (#42)
- improve type hinting (#41)

### Refactor

- improve code quality (#32)
- **org**: add TYPE field to PyObject class (#31)

## v8.1.18.post2 (2022-07-09)

### Refactor

- use java.lang.String (#30)

### Fix

- **java**: add typing to Java code (#29)

## v8.1.18.post1 (2022-07-05)

### Feat

- **ia**: implement all LoggerEx functions (#27)

## v8.1.18 (2022-06-20)

### Feat

- **system**: add `readRaw`, `writeRaw` to `bacnet` module (#23)
- **system**: add fields to Results class (#22)

## v8.1.17 (2022-05-13)

### Fix

- **system**: update type hint for `html` arg (#20)

### Refactor

- **system**: update type hint for payload arg

## v8.1.16.post1 (2022-04-08)

### Feat

- **system**: add perspective.authenticationChallenge (#17)

## v8.1.16 (2022-04-06)

### Feat

- **system**: add version argument to httpClient (#16)

### Refactor

- improve Version comparison logic (#11)
- Sourcery refactored main branch (#1)
- change parent class to Java `Object`

### Fix

- **ci**: fix `ci.yml` (#5)

## v8.1.15 (2022-03-02)

### Feat

- add `system.user.getUserSources` function

## v8.1.14 (2022-01-27)

## v8.1.13.post1 (2022-01-20)

### Feat

- **mypy**: update type hinting on `translate`

## v8.1.13 (2021-12-22)

### Refactor

- move `String` alias to `java.util`
- define ColType as a type alias
- integrate minor changes
- rename argument from pageID to pageId
- change return type to `unicode`

### Feat

- simplify `beep` code

### BREAKING CHANGE

- `system.util.beep()` will print "Beep!" when called
regardless of platform

## v8.1.12.post3 (2021-11-29)

### Feat

- add `String` type

## v8.1.12.post2 (2021-11-26)

## v8.1.12.post1 (2021-11-26)

### Fix

- install now requires `typing`

## v8.1.12 (2021-11-23)

### Feat

- add type hints on all system functions
- improve `date.format`
- add symbols to `format` to cover most cases

### BREAKING CHANGE

- * Python versions below or above 2.7.18 are not supported
* `system.date` and Java's Date are no longer using `datetime` functions
* remove deprecated functions from `system.tag`

## v8.1.11 (2021-10-20)

### Feat

- add AlarmEvent, PyAlarmEvent, and PyAlarmEventImpl
- add org.python.core package
- add Iterable Java interface

## v8.1.10.post7 (2021-10-11)

### Feat

- add PrintStream class to java.io package

## v8.1.10.post6 (2021-10-10)

### Feat

- add Java supporting classes
- add fields and implement more methods
- return instance of BasicDataset

### Refactor

- informal interfaces
- return instance of implementing classes
- switch to informal interfaces
- turn fields into properties

### Fix

- PyUser now returns an instance of User

## v8.1.10.post5 (2021-09-24)

### Fix

- remove builtins import statement

## v8.1.10.post4 (2021-09-22)

### Feat

- make code compatible with Python3

## v8.1.10.post3 (2021-09-21)

### Feat

- make PyDataSet iterable

## v8.1.10.post2 (2021-09-20)

### Feat

- add `com` package to `pip` release
- **setup**: disallow installation on Python 3

### Refactor

- improve code quality
- improve code quality
- add `com` package

### Fix

- move `WindowUtilities` to the correct package

## v8.1.10 (2021-09-09)

### Feat

- 8.1.10
- **setup**: add setup.py

### Refactor

- allow any import level for winsound
- add pylint

## v8.1.9 (2021-08-09)

### Feat

- add new OPC-UA functions

## v8.1.7 (2021-06-05)

### Feat

- **release**: 8.1.7
- **ignition**: bump Ignition 8.1.5 -> 8.1.6

### Refactor

- java.util.Date

## v8.1.6 (2021-05-24)

## v8.1.5-fix (2021-05-11)

### Fix

- add missing parameter to…
- correct typo in docstring

### Feat

- **pre-commit**: update black 21.5b0 -> 21.5b1
- **pre-commit**: update flake8 3.9.1 -> 3.9.2
- **pre-commit**: update black 21.4b2 -> 21.5b0

## v8.1.5 (2021-04-28)

### Feat

- add 8.1.5 changes
- **pre-commit**: update black 21.4b1 -> 21.4b2
- **pre-commit**: update black 21.4b0 -> 21.4b1
- **pre-commit**: update black 20.8b1 -> 21.4b0
- **pre-commit**: bump flake8 to 3.9.1
- add toParseableString implementation
- add build number and update all references

## v8.1.4 (2021-04-02)

### Feat

- **perspective**: add getSessionInfo

## v8.1.3 (2021-03-04)

### Feat

- add new arguments to Perspective functions

## v8.1.2 (2021-02-12)

### Feat

- add flake8 and isort pre-commit hooks

## v8.1.1-fix (2021-01-05)

## v8.1.1 (2020-12-09)

## v8.1.0 (2020-11-15)
