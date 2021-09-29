# Ignition

<!--- Badges --->
![GitHub last commit (main)](https://img.shields.io/github/last-commit/thecesrom/Ignition/main)
[![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/Ignition)](https://github.com/thecesrom/Ignition/graphs/contributors)
[![GitHub downloads](https://img.shields.io/github/downloads/thecesrom/Ignition/total)](https://github.com/thecesrom/Ignition/releases)
[![time tracker](https://wakatime.com/badge/github/thecesrom/Ignition.svg)](https://wakatime.com/badge/github/thecesrom/Ignition)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Imports: flake8](https://img.shields.io/badge/%20imports-flake8-%231674b1?style=flat&labelColor=ef8336)](https://flake8.pycqa.org/en/latest/)
[![Imports: pydocstyle](https://img.shields.io/badge/%20imports-pydocstyle-%231674b1?style=flat&labelColor=ef8336)](https://www.pydocstyle.org/en/stable/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/thecesrom/Ignition/main.svg)](https://results.pre-commit.ci/latest/github/thecesrom/Ignition/main)

Ignition is a set of packages and modules that allows developers to get code completion for Ignition Scripting API scripting functions in their IDE of choice.

## Table of contents

- [Releases](#releases)
- [Branches](#branches)
  - [Cloning a single branch](#cloning-a-single-branch)
- [Prerequisites](#prerequisites)
- [Packages](#packages)
- [Installation and usage](#installation-and-usage)
  - [Installing with pip](#installing-with-pip)
  - [Downloading from releases](#downloading-from-releases)
    - [PyCharm installation](#pycharm-installation)
- [Contributing to Ignition](#contributing-to-ignition)
- [Discussions](#discussions)
- [Contributors](#contributors)
- [License](#license)
- [Code of conduct](#code-of-conduct)

## Releases

Check the [releases page](https://github.com/thecesrom/Ignition/releases) and download the one for your current version.

If you can't find it, feel free to submit your request on our [Discussions](https://github.com/thecesrom/Ignition/discussions).

## Branches

This repository consists of the following branches:

### [main](https://github.com/thecesrom/Ignition/tree/main)

This branch will contain all Scripting Functions from the latest Ignition Release requiring only Python

### [7.9](https://github.com/thecesrom/Ignition/tree/7.9)

This branch will contain all Scripting Functions from the latest Ignition Release for the 7.9 version requiring only Python

### [8.0](https://github.com/thecesrom/Ignition/tree/8.0)

This branch will contain all Scripting Functions from the latest Ignition Release for the 8.0 version requiring only Python

### [jython](https://github.com/thecesrom/Ignition/tree/jython)

This branch will contain all Scripting Functions from the latest Ignition Release requiring Jython (see [jython prerequisites](https://github.com/thecesrom/Ignition/tree/jython#prerequisites))

### Cloning a single branch

If you wish to clone just one branch in particular, use any of the following commands:

- HTTPS

    ```bash
    git clone --single-branch --branch <name> https://github.com/thecesrom/Ignition.git [<directory>]
    ```

- SSH

    ```bash
    git clone --single-branch --branch <name> git@github.com:thecesrom/Ignition.git [<directory>]
    ```

- GitHub CLI

    ```bash
    gh repo clone thecesrom/Ignition [<directory>] -- --single-branch --branch <name>
    ```

#### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 2.7.18 ([download here](https://www.python.org/downloads/release/python-2718/))
- You are familiar with [Ignition 8.1 System Functions](https://docs.inductiveautomation.com/display/DOC81/System+Functions)

#### Packages

Ignition consists of the following packages:

- com
- java/javax
- system

##### com

These are libraries for some of Inductive Automation's Java packages and functions that are imported in `system` packages.

##### java/javax

These are libraries for some Java packages and functions that are imported in `system` packages meant to be used on development environments where no JDK can be installed, and the project interpreter is Python 2.7.

##### system

Is a package that includes all Ignition Scripting Functions.

#### Installation and usage

To use Ignition, you may install it by doing any of the following.

##### Installing with `pip`

The preferred method is to install it by running `pip`. It requires Python 2.7 (we recommend version 2.7.18), or Python 3.

```bash
python -m pip install ignition-api
```

This will install it as package to your Python installation, which will allow you to call Ignition Scripting functions from Python's REPL, and get code completion using an IDE (we recommend PyCharm).

```bash
$ python
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
python -m pip uninstall ignition-api
```

##### Downloading from releases

You may also download the code targeted to your desired version from the [releases page](https://github.com/thecesrom/Ignition/releases) and add it as a dependency to your scripting project.

######## PyCharm Installation

To use Ignition in PyCharm, you will need to attach it to your project.

1. With your project open that you want to use with Ignition, navigate to `File > Open` and select the `Ignition` project folder.
2. Choose `Attach` when you're prompted on how to open the project.
3. Under the new `Ignition` project folder, right-click on the `src/` folder and choose `Mark Directory as > Sources Root`.

#### Contributing to Ignition

To contribute to Ignition, follow these steps:

1. Fork this repository
2. Create a local copy on your machine
3. Create a branch
4. Make your changes and commit them
5. Push to the `main` branch
6. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

#### Discussions

Feel free to post your questions and/or ideas at [Discussions](https://github.com/thecesrom/incendium/discussions).

#### Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/Ignition/graphs/contributors).

#### License

See the [LICENSE](https://github.com/thecesrom/Ignition/blob/HEAD/LICENSE).

#### Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
