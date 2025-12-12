# ignition-api 8.1

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ignition-api)](https://pypi.org/project/ignition-api/)
[![PyPI - Version](https://img.shields.io/pypi/v/ignition-api)](https://pypi.org/project/ignition-api/)
[![PyPI - Downloads](https://static.pepy.tech/badge/ignition-api)](https://pepy.tech/projects/ignition-api)
[![ignition-api](https://snyk.io//advisor/python/ignition-api/badge.svg)](https://snyk.io//advisor/python/ignition-api)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ignition-devs/ignition-api-8.1/main.svg)](https://results.pre-commit.ci/latest/github/ignition-devs/ignition-api-8.1/main)
[![ci](https://github.com/ignition-devs/ignition-api-8.1/actions/workflows/ci.yml/badge.svg)](https://github.com/ignition-devs/ignition-api-8.1/actions/workflows/ci.yml)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/orgs/ignition-devs/discussions)

ignition-api is a Python package that allows developers to get code completion
for Ignition Scripting API scripting functions in their IDE of choice.

## Table of contents

- [Prerequisites](#prerequisites)
- [Installation and usage](#installation-and-usage)
  - [Installing with pip](#installing-with-pip)
  - [Downloading from releases](#downloading-from-releases)
    - [Using as a dependency in PyCharm](#using-as-a-dependency-in-pycharm)
  - [Stubs](#stubs)
- [Project structure](#project-structure)
  - [Packages](#packages)
- [Contributing](#contributing)
- [Discussions](#discussions)
- [Contributors](#contributors)
- [License](#license)
- [Code of conduct](#code-of-conduct)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Python 2.7.18]
- You are familiar with [Ignition System Functions]

## Installation and usage

To use ignition-api, you may install it by doing any of the following.

### Installing with `pip`

The preferred method is to install it by running `pip`. It requires Python
2.7.18.

```bash
python2 -m pip install ignition-api
```

This will install it as package to your Python installation, which will allow
you to call Ignition Scripting functions from Python's REPL, and get code
completion using an IDE such as PyCharm and Visual Studio Code.

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

You may also download the code targeted to your desired version from [releases]
and add it as a dependency to your scripting project.

#### Using as a dependency in PyCharm

To include ignition-api as a dependency in PyCharm, you will need to attach it
to your project.

1. Clone the repo or download from [releases]
1. With your project open where you want to include `ignition-api`, navigate to
   `File > Open` and select the `ignition-api` project folder
1. Choose `Attach` when prompted
1. Under the `ignitition-api` project folder, right-click on the `src/` folder
   and choose `Mark Directory as > Sources Root`

### Stubs

[`ignition-api-stubs`] is a companion package that provides Python type stubs
(`.pyi` files) for the Ignition Scripting API. Type stubs enable static type
checking and enhanced IDE support for code that depends on `ignition-api`.

The recommended use of `ignition-api-stubs` is to enable type checking of your
Ignition scripting code using [`mypy`]. This allows you to catch type-related
errors during development before deploying to your Ignition gateway.

## Project structure

### Packages

This project consists of the following packages:

- com
  - codahale
  - [google](#comgoogle)
  - [inductiveautomation](#cominductiveautomation)
  - palantir
- org
  - [apache](#orgapache)
  - [bson](#orgbson)
  - [json](#orgjson)
  - [python](#orgpython)
  - [slf4j](#orgslf4j)
- [system](#system)

#### com.google

This package includes supporting classes and interfaces from Guava: Google Core
Libraries for Java 32.0.1-jre API. For more information, see documentation here:
<https://javadoc.io/doc/com.google.guava/guava/32.0.1-jre/index.html>

#### com.inductiveautomation

This package includes supporting Inductive Automation's classes and interfaces.
For more information, see documentation here:
<https://files.inductiveautomation.com/sdk/javadoc/ignition81/8.1.50/index.html>.

#### org.apache

##### org.apache.commons.lang3

This package includes supporting classes and interfaces from Apache Commons Lang
3.11 API. For more information, see documentation here:
<https://javadoc.io/doc/org.apache.commons/commons-lang3/3.11/index.html>

##### org.apache.commons.math3

This package includes supporting classes and interfaces from Apache Commons Math
3.6.1 API. For more information, see documentation here:
<https://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/index.html>

##### org.apache.commons.poi

This package includes supporting classes and interfaces from Apache POI 4.1.2
API. For more information, see documentation here:
<https://www.javadoc.io/doc/org.apache.poi/poi/4.1.2/index.html>

#### org.bson

This package includes supporting classes and interfaces from Mongo Java driver
4.8.1, see documentation here:
<https://javadoc.io/doc/org.mongodb/bson/4.8.1/index.html>

#### org.json

This package includes supporting classes and interfaces from the Inductive
Automation's `org.json` package, see documentation here:
<https://files.inductiveautomation.com/sdk/javadoc/ignition81/8.1.50/org/json/package-summary.html>

#### org.python

This package includes supporting Jython classes and interfaces. For more
information, see documentation here:
<https://www.javadoc.io/doc/org.python/jython-standalone/2.7.3/index.html>.

#### org.slf4j

This package includes supporting classes and interfaces from SLF4J API Module.
For more information, see documentation here:
<https://www.javadoc.io/doc/org.slf4j/slf4j-api/2.0.12/index.html>.

#### system

This package includes all Ignition Scripting Functions. For more information,
see documentation here:
<https://docs.inductiveautomation.com/docs/8.1/appendix/scripting-functions>.

## Contributing

See [CONTRIBUTING.md].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found here: [CONTRIBUTORS].

## License

See the [LICENSE].

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct].

<!-- Links -->
[CONTRIBUTING.md]: https://github.com/ignition-devs/ignition-api-8.1/blob/main/CONTRIBUTING.md#contributing-to-ignition-api
[CONTRIBUTORS]: https://github.com/ignition-devs/ignition-api-8.1/graphs/contributors
[Discussions]: https://github.com/orgs/ignition-devs/discussions
[`ignition-api-stubs`]: https://pypi.org/project/ignition-api-stubs
[Ignition System Functions]: https://docs.inductiveautomation.com/docs/8.1/appendix/scripting-functions
[LICENSE]: https://github.com/ignition-devs/ignition-api-8.1/blob/main/LICENSE
[Microsoft Open Source Code of Conduct]: https://opensource.microsoft.com/codeofconduct/
[`mypy`]: https://coatl-mypy.readthedocs.io/en/v0.971/
[Python 2.7.18]: https://www.python.org/downloads/release/python-2718/
[releases]: https://github.com/ignition-devs/ignition-api-8.1/releases
