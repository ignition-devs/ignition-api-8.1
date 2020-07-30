# Description
This repository consists of the following projects:
* python

## python
The python project consists of the following packages:
* incendium
* java
* javax
* system

### incendium
Is a package that extends and wraps some functions from Ignition's scripting API.  For more information, please refer to
the [Wiki](https://github.com/thecesrom/Ignition/wiki/incendium)

### java/javax
These are libraries for some Java packages and functions that are imported on `incendium` and `system` packages meant to be used on systems where no JDK can be installed, and the project interpreter is Python 2.7.

### system (a.k.a. Ignition mock scripts)
Is a library of Inductive Automation Ignition's API (mock) scripting functions meant to be included as a dependency on your
own projects when developing on a Python/Jython IDE. This allows you to get code completion (a.k.a. IntelliSense).

For more information, please refer to:
* [Igntion 7.9 Scripting Functions](https://docs.inductiveautomation.com/display/DOC79/Scripting+Functions).
* [Ignition 8 Scripting Functions](https://docs.inductiveautomation.com/display/DOC80/Scripting+Functions).
