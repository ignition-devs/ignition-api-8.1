"""SFC Functions.

The following functions give you access to interact with the SFCs in the
Gateway.
"""

from __future__ import print_function

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

from system.dataset import Dataset


class PyChartScope(object):
    """This class represents any "scope" in the SFC system, and is
    fundamentally just an observable dictionary.

    Despite its name, it is not limited to chart scope. This class
    notifies listeners when values are changed, and wraps any
    dictionaries assigned to it as PyChartScopes as well.
    """

    def __set__(self, instance, value):
        pass

    def __setattr__(self, key, value):
        pass

    def __setitem__(self, key, value):
        pass


def cancelChart(instanceId):
    """Cancels the execution of a running chart instance.

    Any running steps will be told to stop, and the chart will enter
    Canceling state.

    Args:
        instanceId (str): The ID of the chart instance to cancel.
    """
    print(instanceId)


def getRunningCharts(charPath=None):
    """Retrieves information about running charts.

    Can search all running charts, or be filtered charts at a specific
    path. This function will return charts that are in a Paused state.

    Args:
        charPath (str): The path to a chart to filter on: i.e.,
            "folder/chartName". If specified, only charts at the path
            will be included in the returned dataset. If omitted, the
            function will return data for all active charts.

    Returns:
        Dataset: A dataset with information on the active chart.
    """
    print(charPath)
    return Dataset()


def getVariables(instanceId):
    """Get the variables in a chart instance's scope.

    Commonly used to check the value of a Chart Parameter, or determine
    how long the chart has been running for.

    Args:
        instanceId (str): The instance identifier of the chart.

    Returns:
        PyChartScope: A python dictionary of variables. Step scopes for
            active steps are found under the "activeSteps" key.
    """
    print(instanceId)
    return PyChartScope()


def pauseChart(instanceId):
    """Pauses a running chart instance.

    Any running steps will be told to pause, and the chart will enter
    Pausing state.

    Args:
        instanceId (str): The ID of the chart instance to pause.
    """
    print(instanceId)


def redundantCheckpoint(instanceId):
    """Synchronizes chart and step variables of the specified chart
    instance across a redundant cluster, allowing the chart instance to
    continue where it left off if a redundant failover occurs.

    Args:
        instanceId (str): The instance identifier of the chart.
    """
    print(instanceId)


def resumeChart(instanceId):
    """Resumes a chart that was paused.

    Steps which were previously paused will be resumed, and chart will
    enter Resuming state.

    Args:
        instanceId (str): The ID of the chart instance to resume.

    Raises:
        KeyError: If the ID does not match any running chart instance.
    """
    if not instanceId:
        raise KeyError("Invalid UUID string: {}".format(instanceId))


def setVariable(instanceId, stepId, variableName, variableValue):
    """Sets a variable inside a currently running chart.

    Args:
        instanceId (str): The instance identifier of the chart.
        stepId (str): The id for a step inside of a chart. If omitted
            the function will target a chart scoped variable.
        variableName (str): The name of the variable to set.
        variableValue (object): The value for the variable to be set to.
    """
    print(instanceId, stepId, variableName, variableValue)


def setVariables(instanceId, stepId, variableMap):
    """Sets any number of variables inside a currently running chart.

    Args:
        instanceId (str): The instance identifier of the chart.
        stepId (str): The id for a step inside of a chart. If omitted
            the function will target a chart scoped variable.
        variableMap (dict): A dictionary containing the name:value pairs
            of the variables to set.
    """
    print(instanceId, stepId, variableMap)


def startChart(path, chartPath, arguments):
    """Starts a new instance of a chart.

    The chart must be set to "Callable" execution mode.

    Args:
        path (str): The path to the chart, for example:
            "ChartFolder/ChartName".
        chartPath (str): The path to the chart, for example
            "ChartFolder/ChartName"
        arguments (dict): A dictionary of arguments. Each key-value pair
            in the dictionary becomes a variable in the chart scope and
            will override any default.

    Returns:
        str: The unique ID of this chart.
    """
    print(path, chartPath, arguments)
    return "UUID"
