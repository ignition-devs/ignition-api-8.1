"""Project Functions.

The following functions allow you to list projects on the Gateway
through scripting.
"""

from __future__ import print_function

__all__ = ["getProjectName", "getProjectNames", "requestScan"]

from typing import List

from dev.thecesrom.helper.types import AnyStr


def getProjectName():
    # type: () -> AnyStr
    """Returns the name of the project where the function was called
    from.

    When called from the Gateway scope from a resource that originates
    from a singular project (reports, SFCs, etc.), will return that
    resources project.

    Resources that run in the Gateway scope, but are configured in a
    singular project (such as a report), will use that project's name.

    When called from a scope that does not have an associated project
    (a Tag Event Script), the function will return the name of the
    Gateway scripting project. If a Gateway scripting project has not
    been configured, then returns an empty string.

    Returns:
         The name of the currently running project.
    """
    return "MyProject"


def getProjectNames():
    # type: () -> List[AnyStr]
    """Returns an unsorted collection of strings, where each string
    represents the name of a project on the Gateway.

    If no projects exist, returns an empty list.

    This function only ever returns project names, ignoring project
    titles. The function also ignores the "enabled" property, including
    disabled projects in the results.

    Returns:
         A list containing string representations of project names on
         the Gateway.
    """
    return ["MyProject", "DisabledProject"]


def requestScan(timeout=10):
    # type: (int) -> None
    """Requests a manual scan of the projects directory in order to
    refresh projects and their resources. If a scan is currently
    running, this method has no effect and will return when the in-
    progress scan has finished. This function blocks the current thread
    until a scan has completed.

    Args:
        timeout: The amount of time, in seconds, to block the current
            thread before timing out. Default is 10 seconds. Optional.
    """
    print(timeout)
