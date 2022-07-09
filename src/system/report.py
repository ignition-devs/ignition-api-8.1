"""Report Functions.

The following functions give you access to report details and the
ability to run reports.
"""

from __future__ import print_function

__all__ = [
    "executeAndDistribute",
    "executeReport",
    "getReportNamesAsDataset",
    "getReportNamesAsList",
]

from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import IllegalArgumentException, String


def executeAndDistribute(
    path,  # type: String
    project="project",  # type: String
    parameters=None,  # type: Optional[Dict[String, int]]
    action=None,  # type: Optional[String]
    actionSettings=None,  # type: Optional[Dict[String, Any]]
):
    # type: (...) -> None
    """Executes and distributes a report.

    Similar to scheduling a report to execute, except a schedule in not
    required to utilize this function. This is a great way to distribute
    the report on demand from a Client.

    Note:
        The function system.report.executeAndDistribute() does not run
        on its own thread and can get blocked. For example, if a printer
        is backed up and it takes a while to finish the request made by
        this function, the script will block the execution of other
        things on that thread until it finishes. Be sure to keep this in
        mind when using it in a script.

    Args:
        path: The path to the existing report.
        project: The name of the project where the report is located.
            Optional in client scope.
        parameters: An optional dictionary of parameter overrides, in
            the form name:value.
        action: The name of the distribution action to use.
        actionSettings: An optional dictionary of settings particular to
            the action. Missing values will use the default value for
            that action.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist, or a key is not valid.
    """
    if project is None:
        raise IllegalArgumentException()

    print(path, project, parameters, action, actionSettings)


def executeReport(
    path,  # type: String
    project="project",  # type: String
    parameters=None,  # type: Optional[Dict[String, int]]
    fileType="pdf",  # type: String
):
    # type: (...) -> Any
    """Immediately executes an existing report and returns a byte[] of
    the output.

    Args:
        path: The path to the existing report.
        project: The name of the project where the report is located.
            Optional in client scope.
        parameters: An optional dictionary of parameter overrides, in
            the form name:value. Optional.
        fileType: The file type the resulting byte array should
            represent. Defaults to "pdf". Not case-sensitive. Optional.

    Returns:
        A byte array of the resulting report.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist.
    """
    file_types = [
        "csv",
        "html",
        "jpeg",
        "pdf",
        "png",
        "rtf",
        "xls",
        "xlsx",
        "xml",
    ]
    if path is None or project is None or fileType not in file_types:
        raise IllegalArgumentException()
    print(path, project, parameters, fileType)


def getReportNamesAsDataset(project="project", includeReportName=True):
    # type: (Optional[String], Optional[bool]) -> BasicDataset
    """Gets a data of all reports for a project.

    Args:
        project: The name of the project where the reports are located.
            Optional in client scope.
        includeReportName: When set to False, the end of Path does not
            include the report name. Default is True. Optional.

    Returns:
        A dataset of report paths and names for the project. Returns an
        empty dataset if the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()

    print(project, includeReportName)
    return BasicDataset()


def getReportNamesAsList(project="project"):
    # type: (Optional[String]) -> List[String]
    """Gets a list of all reports for a project.

    Args:
        project: The name of the project where the reports are located.
            Optional in client scope.

    Returns:
        A list of report paths for the project. Returns an empty list if
        the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()
    return []
