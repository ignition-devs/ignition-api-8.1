"""EAM Functions.

The following functions give you access to view EAM information from the
Gateway.
"""

from __future__ import print_function, unicode_literals

__all__ = ["getGroups", "queryAgentHistory", "queryAgentStatus", "runTask"]

from typing import List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.messages import UIResponse
from java.util import Date, Locale


def getGroups():
    # type: () -> List[Union[str, unicode]]
    """Returns the names of the defined agent organizational groups in
    the Gateway.

    Returns:
        A string list of group names.
    """
    return [""]


def queryAgentHistory(
    groupIds=None,  # type: Optional[List[Union[str, unicode]]]
    agentIds=None,  # type: Optional[List[Union[str, unicode]]]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    limit=100,  # type: Optional[int]
):
    # type: (...) -> BasicDataset
    """Returns a list of the most recent agent events.

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
    groupIds=None,  # type: Optional[List[Union[str, unicode]]]
    agentIds=None,  # type: Optional[List[Union[str, unicode]]]
    isConnected=True,  # type: Optional[bool]
):
    # type: (...) -> BasicDataset
    """Returns the current state of the matching agents.

    Args:
        groupIds: A list of groups to restrict the results to. If not
            specified, all groups will be included.
        agentIds: A list of agent names to restrict the results to. If
            not specified, all agents will be allowed.
        isConnected: If True, only returns agents that are currently
            connected. If False, only agents that are considered down
            will be returned, and if not specified, all agents will be
            returned.

    Returns:
        A dataset with columns AgentName, NodeRole, AgentGroup,
        LastCommunication, IsConnected, IsRunning, RunningState,
        RunningStateInt, LicenseKey, and Version, where each row is a
        new agent.
    """
    print(groupIds, agentIds, isConnected)
    return BasicDataset()


def runTask(taskname):
    # type: (Union[str, unicode]) -> UIResponse
    """Takes the name of a task as an argument as a string (must be
    configured on the Controller before hand), attempts to execute the
    task.

    To run in the client, the user needs a role-based permission. This
    permission is disabled by default.

    Args:
        taskname: Name of the task to run. If more than one task has
            this name, an error will be returned.

    Returns:
        A UIResponse with a list of infos, errors, and warnings.
    """
    print(taskname)
    return UIResponse(Locale.ENGLISH)
