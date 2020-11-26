# Copyright (C) 2020
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev
"""Report Functions
The following functions give you access to report details and the
ability to run reports.
"""

__all__ = [
    'executeAndDistribute', 'executeReport', 'getReportNamesAsDataset',
    'getReportNamesAsList'
]

from java.lang import IllegalArgumentException
from system.dataset import Dataset


def executeAndDistribute(path,
                         project='project',
                         parameters=None,
                         action=None,
                         actionSettings=None):
    """Executes and distributes a report. Similar to scheduling a report
    to execute, except a schedule in not required to utilize this
    function. This is a great way to distribute the report on demand
    from a client.

    Args:
        path (str): The path to the existing report.
        project (str): The name of the project where the report is
            located. Optional in client scope.
        parameters (dict): An optional dictionary of parameter
            overrides, in the form name:value.
        action (str): The name of the distribution action to use.
        actionSettings (dict): An optional dictionary of settings
            particular to the action. Missing values will use the
            default value for that action.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist, or a key is not valid.
    """
    if project is None:
        raise IllegalArgumentException()
    else:
        print(path, project, parameters, action, actionSettings)


def executeReport(path, project='project', parameters=None, fileType='pdf'):
    """Immediately executes an existing report and returns a byte[] of
    the output.

    Args:
        path (str): The path to the existing report.
        project (str): The name of the project where the report is
            located. Optional in client scope.
        parameters (dict): An optional dictionary of parameter
            overrides, in the form name:value. Optional.
        fileType (str): The file type the resulting byte array should
            represent. Defaults to "pdf". Not case-sensitive. Optional.

    Returns:
        object: A byte array of the resulting report.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist.
    """
    _fileTypes = ['pdf', 'html', 'csv', 'rtf', 'jpeg', 'png', 'xml']
    if path is None or project is None or fileType not in _fileTypes:
        raise IllegalArgumentException()
    print(path, project, parameters, fileType)
    return None


def getReportNamesAsDataset(project='project'):
    """Gets a data of all reports for a project. This dataset is
    particularly suited for display in a Tree View component.

    Args:
        project (str):  The name of the project where the reports are
            located. Optional in client scope.

    Returns:
        Dataset: A dataset of report paths and names for the project.
            Returns an empty dataset if the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()
    else:
        return Dataset()


def getReportNamesAsList(project='project'):
    """Gets a list of all reports for a project.

    Args:
        project (str):  The name of the project where the reports are
            located. Optional in client scope.

    Returns:
        list[str]: A list of report paths for the project. Returns an
            empty list if the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()
    else:
        return []
