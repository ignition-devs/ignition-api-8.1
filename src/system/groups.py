"""Transaction Group Functions.

The following functions give you access to import and remove Transaction
Groups.
"""

from __future__ import print_function

__all__ = ["loadFromFile", "removeGroups"]


def loadFromFile(filePath, projectName, mode):
    """Loads a transaction group configuration from an xml export, into
    the specified project (creating the project if necessary). The mode
    parameter dictates how overwrites occur.

    Args:
        filePath (str): The path to a valid transaction group xml or csv
            file.
        projectName (str): The name of the project to load into.
        mode (int): How duplicates will be handled. 0 = Overwrite,
            1 = Ignore, 2 = Replace the existing project with this one.
    """
    print(filePath, projectName, mode)


def removeGroups(projectName, paths):
    """Removes the specified groups from the project. The group paths
    are "Folder/Path/To/GroupName", separated by forward slashes.

    Args:
        projectName (str): The project to remove from. If the project
            does not exist, throws an IllegalArgumentException.
        paths (list[str]): A collection of paths to remove. The group
            paths are "Folder/Path/To/GroupName", separated by forward
            slashes.
    """
    print(projectName, paths)
