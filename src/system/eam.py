# Copyright (C) 2018-2021
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev

"""EAM Functions.

The following functions give you access to view EAM information from the
Gateway.
"""

from __future__ import print_function

__all__ = ["getGroups", "queryAgentHistory", "queryAgentStatus", "runTask"]

import system.date
from java.lang import Object
from java.util import Date, Locale
from system.dataset import Dataset


class UIResponse(Object):
    def __init__(self, locale):
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass


def getGroups():
    """Returns the names of the defined agent organizational groups in
    the Gateway.

    Returns:
        list[str]: A string list of group names.
    """
    return [""]


def queryAgentHistory(
    groupIds=None, agentIds=None, startDate=None, endDate=None, limit=100
):
    """Returns a list of the most recent agent events.

    Args:
        groupIds (list[str]): A list of groups to restrict the results
            to. If not specified, all groups will be included. Optional.
        agentIds (list[str]): A list of agent names to restrict the
            results to. If not specified, all agents will be allowed.
            Optional.
        startDate (Date): The starting time for history events. If
            null, defaults to 8 hours previous to now. Optional.
        endDate (Date): The ending time for the query range. If
            null, defaults to "now". Optional.
        limit (int): The limit of results to return. Defaults to 100. A
            value of 0 means "no limit". Optional.

    Returns:
        Dataset: A dataset with columns id, agent_name, agent_role,
            event_time, event_category, event_type, event_source,
            event_level, event_level_int, and message, where each row is
            a new agent event.
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
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
            considered down will be returned, and if not specified, all
            agents will be returned.

    Returns:
        Dataset: A dataset with columns AgentName, NodeRole, AgentGroup,
            LastCommunication, IsConnected, IsRunning, RunningState,
            RunningStateInt, LicenseKey, and Version, where each row is
            a new agent.
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
    print(taskname)
    return UIResponse(Locale.ENGLISH)
