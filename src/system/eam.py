"""EAM Functions.

The following functions give you access to view EAM information from the
Gateway.
"""

from __future__ import print_function

__all__ = ["getGroups", "queryAgentHistory", "queryAgentStatus", "runTask"]

from typing import List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.messages import UIResponse
from java.lang import String
from java.util import Date, Locale


def getGroups():
    # type: () -> List[String]
    """Returns the names of the defined agent organizational groups in
    the Gateway.

    This function should only be called from the Controller.

    Note:
        If called from an Agent on 8.1.11+, this function will return an
        exception.

    Returns:
        A string list of group names.
    """
    return [""]


def queryAgentHistory(
    groupIds=None,  # type: Optional[List[String]]
    agentIds=None,  # type: Optional[List[String]]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    limit=100,  # type: int
):
    # type: (...) -> BasicDataset
    """Returns a list of the most recent agent events.

    This function should only be called from the Controller.

    Note:
        If called from an Agent on 8.1.11+, this function will return an
        exception.

    Args:
        groupIds: A list of groups to restrict the results to. If not
            specified, all groups will be included. Optional.
        agentIds: A list of agent names to restrict the results to. If
            not specified, all agents will be allowed. Optional.
        startDate: The starting time for history events. If null,
            defaults to 8 hours previous to now. Optional.
        endDate: The ending time for the query range. If null, defaults
            to "now". Optional.
        limit: The limit of results to return. Defaults to 100. A value
            of 0 means "no limit". Optional.

    Returns:
        A dataset with columns id, agent_name, agent_role, event_time,
        event_category, event_type, event_source, event_level,
        event_level_int, and message, where each row is a new agent
        event.
    """
    print(groupIds, agentIds, startDate, endDate, limit)
    return BasicDataset()


def queryAgentStatus(
    groupIds=None,  # type: Optional[List[String]]
    agentIds=None,  # type: Optional[List[String]]
    isConnected=True,  # type: bool
):
    # type: (...) -> BasicDataset
    """Returns the current state of the matching agents.

    This function should only be called from the Controller.

    Note:
        If called from an Agent on 8.1.11+, this function will return an
        exception.

    Args:
        groupIds: A list of groups to restrict the results to. If not
            specified, all groups will be included. Optional.
        agentIds: A list of agent names to restrict the results to. If
            not specified, all agents will be allowed. Optional.
        isConnected: If True, only returns agents that are currently
            connected. If False, only agents that are considered down
            will be returned, and if not specified, all agents will be
            returned. Optional.

    Returns:
        A dataset with columns AgentName, NodeRole, AgentGroup,
        LastCommunication, IsConnected, IsRunning, RunningState,
        RunningStateInt, LicenseKey, and Version, where each row is a
        new agent.

        Possible values for RunningState and RunningStateInt are:
        0 = Disconnected, 1 = Running, 2 = Warned, 3 = Errored.
    """
    print(groupIds, agentIds, isConnected)
    return BasicDataset()


def runTask(taskname):
    # type: (String) -> UIResponse
    """Takes the name of a task as an argument as a string (must be
    configured on the Controller before hand), attempts to execute the
    task.

    This function should only be called from the Controller.

    To run in the client, the user needs a role-based permission. This
    permission is disabled by default.

    Note:
        If called from an Agent on 8.1.11+, this function will return an
        exception.

    Args:
        taskname: Name of the task to run. If more than one task has
            this name, an error will be returned.

    Returns:
        A UIResponse with a list of infos, errors, and warnings.
    """
    print(taskname)
    return UIResponse(Locale.ENGLISH)
