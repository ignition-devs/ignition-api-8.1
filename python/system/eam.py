# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""EAM Functions
The following functions give you access to view EAM information from
the Gateway."""

__all__ = [
    'getGroups',
    'queryAgentHistory',
    'queryAgentStatus',
    'runTask'
]

import system.date
from system.dataset import Dataset
from . import UIResponse


def getGroups():
    """Returns the names of the defined agent organizational groups in
    the Gateway.

    Returns:
        list[str]: A string list of group names.
    """
    return ['']


def queryAgentHistory(groupIds=None, agentIds=None,
                      startDate=system.date.addHours(system.date.now(), -8),
                      endDate=system.date.now(), limit=100):
    """Returns a list of the most recent agent events.

    Args:
        groupIds (list[str]): A list of groups to restrict the results
            to. If not specified, all groups will be included.
        agentIds (list[str]): A list of agent names to restrict the
            results to. If not specified, all agents will be allowed.
        startDate (datetime): The starting time for history events. If
            null, defaults to 8 hours previous to now.
        endDate (datetime): The ending time for the query range. If null,
            defaults to "now".
        limit (int): The limit of results to return. Defaults to 100.
            A value of 0 means "no limit".

    Returns:
        Dataset: A dataset with columns id, agent_name, agent_role,
            event_time, event_category, event_type, event_source,
            event_level, event_level_int, and message, where each row
            is a new agent event.
    """
    print(groupIds, agentIds, startDate, endDate, limit)
    return Dataset()


def queryAgentStatus(groupIds=None, agentIds=None, isConnected=True):
    """Returns the current state of the matching agents.

    Args:
        groupIds (list[str]): A list of groups to restrict the results
            to. If not specified, all groups will be included.
        agentIds (list[str]): A list of agent names to restrict the
            results to. If not specified, all agents will be allowed.
        isConnected (bool): If True, only returns agents that are
            currently connected. If False, only agents that are
            considered down will be returned, and if not specified,
            all agents will be returned.

    Returns:
        Dataset: A dataset with columns AgentName, NodeRole,
            AgentGroup, LastCommunication, IsConnected, IsRunning,
            RunningState, RunningStateInt, LicenseKey, and Version,
            where each row is a new agent.
    """
    print(groupIds, agentIds, isConnected)
    return Dataset()


def runTask(taskname):
    """Takes the name of a task as an argument as a string (must be
    configured on the Controller before hand), attempts to execute the
    task.

    To run in the client, the user needs a role-based permission. This
    permission is disabled by default.

    Args:
        taskname (str): Name of the task to run. If more than one task
            has this name, an error will be returned.

    Returns:
        UIResponse: A UIResponse with a list of infos, errors, and
            warnings.
    """
    print taskname
    return UIResponse()
