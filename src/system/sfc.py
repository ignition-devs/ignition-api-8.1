"""SFC Functions.

The following functions give you access to interact with the SFCs in the
Gateway.
"""

from __future__ import print_function, unicode_literals

__all__ = [
    "cancelChart",
    "getRunningCharts",
    "getVariables",
    "pauseChart",
    "redundantCheckpoint",
    "resumeChart",
    "setVariable",
    "setVariables",
    "startChart",
]

from typing import Any, Dict, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.sfc.api import PyChartScope


def cancelChart(instanceId):
    # type: (Union[str, unicode]) -> None
    """Cancels the execution of a running chart instance.

    Any running steps will be told to stop, and the chart will enter
    Canceling state.

    Args:
        instanceId: The ID of the chart instance to cancel.
    """
    print(instanceId)


def getRunningCharts(charPath=None):
    # type: (Optional[Union[str, unicode]]) -> BasicDataset
    """Retrieves information about running charts.

    Can search all running charts, or be filtered charts at a specific
    path. This function will return charts that are in a Paused state.

    Args:
        charPath: The path to a chart to filter on: i.e.,
            "folder/chartName". If specified, only charts at the path
            will be included in the returned dataset. If omitted, the
            function will return data for all active charts.

    Returns:
        A dataset with information on the active chart.
    """
    print(charPath)
    return BasicDataset()


def getVariables(instanceId):
    # type: (Union[str, unicode]) -> PyChartScope
    """Get the variables in a chart instance's scope.

    Commonly used to check the value of a Chart Parameter, or determine
    how long the chart has been running for.

    Args:
        instanceId: The instance identifier of the chart.

    Returns:
        A python dictionary of variables. Step scopes for active steps
        are found under the "activeSteps" key.
    """
    print(instanceId)
    return PyChartScope()


def pauseChart(instanceId):
    # type: (Union[str, unicode]) -> None
    """Pauses a running chart instance.

    Any running steps will be told to pause, and the chart will enter
    Pausing state.

    Args:
        instanceId: The ID of the chart instance to pause.
    """
    print(instanceId)


def redundantCheckpoint(instanceId):
    # type: (Union[str, unicode]) -> None
    """Synchronizes chart and step variables of the specified chart
    instance across a redundant cluster, allowing the chart instance to
    continue where it left off if a redundant failover occurs.

    Args:
        instanceId: The instance identifier of the chart.
    """
    print(instanceId)


def resumeChart(instanceId):
    # type: (Union[str, unicode]) -> None
    """Resumes a chart that was paused.

    Steps which were previously paused will be resumed, and chart will
    enter Resuming state.

    Args:
        instanceId: The ID of the chart instance to resume.

    Raises:
        KeyError: If the ID does not match any running chart instance.
    """
    if not instanceId:
        raise KeyError("Invalid UUID string: {}".format(instanceId))


def setVariable(
    instanceId,  # type: Union[str, unicode]
    stepId,  # type: Union[str, unicode]
    variableName,  # type: Union[str, unicode]
    variableValue,  # type: Any
):
    # type: (...) -> None
    """Sets a variable inside a currently running chart.

    Args:
        instanceId: The instance identifier of the chart.
        stepId: The id for a step inside of a chart. If omitted the
            function will target a chart scoped variable.
        variableName: The name of the variable to set.
        variableValue: The value for the variable to be set to.
    """
    print(instanceId, stepId, variableName, variableValue)


def setVariables(
    instanceId,  # type: Union[str, unicode]
    stepId,  # type: Union[str, unicode]
    variableMap,  # type: Dict[Union[str, unicode], Any]
):
    # type: (...) -> None
    """Sets any number of variables inside a currently running chart.

    Args:
        instanceId: The instance identifier of the chart.
        stepId: The id for a step inside of a chart. If omitted
            the function will target a chart scoped variable.
        variableMap: A dictionary containing the name:value pairs
            of the variables to set.
    """
    print(instanceId, stepId, variableMap)


def startChart(
    projectName,  # type: Union[str, unicode]
    chartPath,  # type: Union[str, unicode]
    arguments,  # type: Dict[Union[str, unicode], Any]
):
    # type: (...) -> Union[str, unicode]
    """Starts a new instance of a chart.

    The chart must be set to "Callable" execution mode.

    Args:
        projectName: The name of the project that the chart was created
            in.
        chartPath (str): The path to the chart, for example
            "ChartFolder/ChartName"
        arguments: A dictionary of arguments. Each key-value pair in the
            dictionary becomes a variable in the chart scope and will
            override any default.

    Returns:
        str: The unique ID of this chart.
    """
    print(projectName, chartPath, arguments)
    return "UUID"
