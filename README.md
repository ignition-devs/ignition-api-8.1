# ignition-api 8.1

<!--- Badges --->
![GitHub last commit (8.1)](https://img.shields.io/github/last-commit/ignition-api/8.1/main)
[![GitHub contributors](https://img.shields.io/github/contributors/ignition-api/8.1)](https://github.com/ignition-api/8.1/graphs/contributors)
[![Downloads](https://static.pepy.tech/badge/ignition-api)](https://pepy.tech/project/ignition-api)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Imports: flake8](https://img.shields.io/badge/%20imports-flake8-%231674b1?style=flat&labelColor=ef8336)](https://flake8.pycqa.org/en/latest/)
[![Imports: pydocstyle](https://img.shields.io/badge/%20imports-pydocstyle-%231674b1?style=flat&labelColor=ef8336)](https://www.pydocstyle.org/en/stable/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/ignition-api/8.1/discussions)

ignition-api is a Python package that allows developers to get code completion for Ignition Scripting API scripting functions in their IDE of choice.

## Table of contents

- [Prerequisites](#prerequisites)
- [Installation and usage](#installation-and-usage)
  - [Installing with pip](#installing-with-pip)
  - [Downloading from releases](#downloading-from-releases)
    - [Using as a dependency in PyCharm](#using-as-a-dependency-in-pycharm)
- [Project structure](#project-structure)
  - [Packages](#packages)
- [Contributing](#contributing)
- [Discussions](#discussions)
- [Contributors](#contributors)
- [License](#license)
- [Code of conduct](#code-of-conduct)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 2.7.18 ([download here](https://www.python.org/downloads/release/python-2718/))
- You are familiar with [Ignition 8.1 System Functions](https://docs.inductiveautomation.com/display/DOC81/System+Functions)

## Installation and usage

To use ignition-api, you may install it by doing any of the following.

### Installing with `pip`

The preferred method is to install it by running `pip`. It requires Python 2.7.18.

```bash
python2 -m pip install ignition-api
```

This will install it as package to your Python installation, which will allow you to call Ignition Scripting functions from Python's REPL, and get code completion using an IDE such as PyCharm and Visual Studio Code.

```bash
$ python2
Python 2.7.18 (default, Nov  9 2020, 16:23:15)
[GCC Apple LLVM 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import print_function
>>> import system.util
>>> print(system.util.__doc__)
Utility Functions.

The following functions give you access to view various Gateway and
Client data, as well as interact with other various systems.

>>> system.util.beep()
>>> quit()
```

And to uninstall:

```bash
python2 -m pip uninstall ignition-api
```

### Downloading from releases

You may also download the code targeted to your desired version from the [releases page](https://github.com/ignition-api/8.1/releases) and add it as a dependency to your scripting project.

#### Using as a dependency in PyCharm

To include ignition-api as a dependency in PyCharm, you will need to attach it to your project.

1. Clone the repo or download from [releases](https://github.com/ignition-api/8.1/releases)
2. With your project open where you want to include `ignition-api`, navigate to `File > Open` and select the `ignition-api` project folder
3. Choose `Attach` when prompted
4. Under the `ignitition-api` project folder, right-click on the `src/` folder and choose `Mark Directory as > Sources Root`

## Project structure

### Packages

This project consists of the following packages:

- com.inductiveautomation
- java
- javax
- org
- system

#### com.inductiveautomation

This package includes supporting Inductive Automation's classes and interfaces. For more information, see documentation here: <https://files.inductiveautomation.com/sdk/javadoc/ignition81/8.1.33/index.html>.

#### java/javax

These packages include supporting Java classes and interfaces. For more information, see documentation here: <https://docs.oracle.com/en/java/javase/17/docs/api/index.html>.

#### org.apache

This package includes supporting classes and interfaces from Apache Commons Math API. For more information, see documentation here: <https://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/index.html>

#### org.json

This package includes supporting classes and interfaces from the Inductive Automation's `org.json` package, see documentation here: <https://files.inductiveautomation.com/sdk/javadoc/ignition81/8.1.33/org/json/package-summary.html>

#### org.python

This package includes supporting Jython classes and interfaces. For more information, see documentation here: <https://www.javadoc.io/doc/org.python/jython-standalone/2.7.2/index.html>.

#### org.slf4j

This package includes supporting classes and interfaces from SLF4J API Module. For more information, see documentation here: <https://www.javadoc.io/doc/org.slf4j/slf4j-api/1.7.26/overview-summary.html>.

#### system

This package includes all Ignition Scripting Functions. For more information, see documentation here: <https://docs.inductiveautomation.com/display/DOC81/System+Functions>.

## Contributing

See [CONTRIBUTING.md](https://github.com/ignition-api/.github/blob/main/CONTRIBUTING.md#contributing-to-ignition-api).

## Discussions

Feel free to post your questions and/or ideas at [Discussions](https://github.com/ignition-api/discussions/discussions).

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/ignition-api/8.1/graphs/contributors).

## License

See the [LICENSE](https://github.com/ignition-api/8.1/blob/HEAD/LICENSE).

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
