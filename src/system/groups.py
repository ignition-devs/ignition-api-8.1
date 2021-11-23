"""Transaction Group Functions.

The following functions give you access to import and remove Transaction
Groups.
"""

from __future__ import print_function, unicode_literals

__all__ = ["loadFromFile", "removeGroups"]

from typing import List, Union


def loadFromFile(filePath, projectName, mode):
    # type: (Union[str, unicode], Union[str, unicode], int) -> None
    """Loads a transaction group configuration from an xml export, into
    the specified project (creating the project if necessary).

    The mode parameter dictates how overwrites occur.

    Args:
        filePath: The path to a valid transaction group xml or csv file.
        projectName: The name of the project to load into.
        mode: How duplicates will be handled. 0 = Overwrite, 1 = Ignore,
            2 = Replace the existing project with this one.
    """
    print(filePath, projectName, mode)


def removeGroups(projectName, paths):
    # type: (Union[str, unicode], List[Union[str, unicode]]) -> None
    """Removes the specified groups from the project.

    The group paths are "Folder/Path/To/GroupName", separated by forward
    slashes.

    Args:
        projectName: The project to remove from. If the project does not
            exist, throws an IllegalArgumentException.
        paths: A collection of paths to remove. The group paths are
            "Folder/Path/To/GroupName", separated by forward slashes.
    """
    print(projectName, paths)
