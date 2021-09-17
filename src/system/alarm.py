"""Alarm Functions.

The following functions give you access to view and interact with the
Alarm system in Ignition.
"""

from __future__ import print_function

__all__ = [
    "acknowledge",
    "cancel",
    "createRoster",
    "getRosters",
    "getShelvedPaths",
    "listPipelines",
    "queryJournal",
    "queryStatus",
    "shelve",
    "unshelve",
]

import system.date
from com.inductiveautomation.ignition.common.alarming.evaluation import (
    ShelvedPath,
)
from com.inductiveautomation.ignition.common.alarming.query import (
    AlarmQueryResult,
)
from java.util import Date


def acknowledge(alarmIds, notes=None, username=None):
    """Acknowledges any number of alarms, specified by their event ids.

    The event id is generated for an alarm when it becomes active, and
    is used to identify a particular event from other events for the
    same source. The alarms will be acknowledged by the logged in user
    making the call. Additionally, acknowledgement notes may be included
    and will be stored along with the acknowledgement.

    Args:
        alarmIds (list[str]): List of alarm event ids (uuids) to
            acknowledge.
        notes (str): Notes that will be stored on the acknowledged alarm
            events. Optional.
        username (str): The user that acknowledged the alarm. NOTE that
            this parameter is only used when called from a gateway
            scoped script. This parameter should be omitted from any
            client-based scripts. Optional.
    """
    print(alarmIds, notes, username)


def cancel(alarmIds):
    """Cancels any number of alarms, specified by their event ids.

    The event id is generated for an alarm when it becomes active, and
    is used to identify a particular event from other events for the
    same source. The alarm will still be active, but will drop out of
    alarm pipelines.

    Args:
        alarmIds (list[str]): List of alarm event ids (uuids) to cancel.
    """
    print(alarmIds)


def createRoster(name, description=""):
    """This function creates a new roster.

    Users may be added to the roster through the Gateway or the Roster
    Management component.

    Args:
        name (str): The name for the new roster.
        description (str): A description for the new roster. Required,
            but can be blank. Optional.
    """
    print(name, description)


def getRosters():
    """This function returns a mapping of roster names to a list of
    usernames contained in the roster.

    Returns:
         dict: A dictionary that maps roster names to a List of
            usernames in the roster. The List of usernames may be empty
            if no users have been added to the roster.
    """
    return {}


def getShelvedPaths():
    """A list of ShelvedPath objects.

    ShelvedPath objects can be examined with getExpiration, getHitCount,
    getPath, getShelveTime, getUser, and isExpired.

    Returns:
        list[ShelvedPath]: A list of ShelvedPath objects. ShelvedPath
            objects can be examined with getExpiration, getHitCount,
            getPath, getShelveTime, getUser, and isExpired.
    """
    return [ShelvedPath()]


def listPipelines(projectName="alarm-pipelines"):
    """Will return a list of the available Alarm Notification Pipelines.

    Args:
        projectName (str): The project to check alarm pipelines for. If
            omitted, will look for a project named "alarm-pipelines".
            Optional.

    Returns:
        list[str]: A list of pipeline names. The list may be empty if no
            pipelines exist. Unsaved name changes will not be reflected
            in the list.
    """
    print(projectName)
    return []


def queryJournal(
    startDate=None,
    endDate=None,
    journalName=None,
    priority=None,
    state=None,
    path=None,
    source=None,
    displaypath=None,
    all_properties=None,
    any_properties=None,
    defined=None,
    includeData=None,
    includeSystem=None,
    isSystem=None,
):
    """Queries the specified journal for historical alarm events.

    The result is a list of alarm events, which can be queried for
    individual properties. The result object also has a getDataset()
    function that can be used to convert the query results into a normal
    dataset, with the columns: EventId, Source, DisplayPath, EventTime,
    EventState, Priority, IsSystemEvent.

    Args:
        startDate (Date): The start of the time range to query.
            Defaults to 8 hours previous to now if omitted. Time range
            is inclusive.
        endDate (Date): The end of the time range to query. Defaults
            to "now" if omitted.
        journalName (str): The journal name to query.
        priority (list[str]): A list of possible priorities to match.
            Priorities can be specified by name or number, with the
            values: Diagnostic(0), Low(1), Medium(2), High(3),
            Critical(4).
        state (list[str]): A list of the event state types to match.
            Valid values are "ClearUnacked", "ClearAcked",
            "ActiveUnacked", and "ActiveAcked".
        path (list[str]): A list of possible source paths to search at.
            The wildcard "*" may be used.
        source (list[str]): A list of possible source paths to search
            at. The wildcard "*" may be used.
        displaypath (list[str]): A list of display paths to search at.
            Display paths are separated by "/", and if a path ends in
            "/*", everything below that path will be searched as well.
        all_properties (list[object]): A set of property conditions, all
            of which must be met for the condition to pass. This
            parameter is a list of tuples, in the form ("propName",
            "condition", value). Valid condition values: "=", "!=", "<",
            "<=", ">", ">=". Only the first two conditions may be used
            for string values.
        any_properties (list[object]): A set of property conditions, any
            of which will cause the overall the condition to pass. This
            parameter is a list of tuples, in the form ("propName",
            "condition", value). Valid condition values: "=", "!=", "<",
            "<=", ">", ">=". Only the first two conditions may be used
            for string values.
        defined (list[str]): A list of string property names, all of
            which must be present on an event for it to pass.
        includeData (bool): Whether or not event data should be included
            in the return. If this parameter is False, and if there are
            no conditions specified on associated data, the properties
            table will not be queried.
        includeSystem (bool): Specifies whether system events are
            included in the return.
        isSystem (bool): Specifies whether the returned event must or
            must not be a system event.

    Returns:
        AlarmQueryResult: The AlarmQueryResult object is functionally a
            list of AlarmEvent objects. The AlarmQueryResult object has
            a built-in getDataset() function that will return a Standard
            Dataset containing the Event Id (UUID of the alarm), Source
            Path, Display Path, Event Time, State (as an integer), and
            Priority (as an integer).
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
    print(
        startDate,
        endDate,
        journalName,
        priority,
        state,
        path,
        source,
        displaypath,
        all_properties,
        any_properties,
        defined,
        includeData,
        includeSystem,
        isSystem,
    )
    return AlarmQueryResult()


def queryStatus(
    priority=None,
    state=None,
    path=None,
    source=None,
    displaypath=None,
    all_properties=None,
    any_properties=None,
    defined=None,
    includeShelved=False,
):
    """Queries the current state of alarms.

    The result is a list of alarm events, which can be queried for
    individual properties. The result object also has a getDataset()
    function that can be used to convert the query results into a normal
    dataset, with the columns: EventId, Source, DisplayPath, EventTime,
    State, Priority.

    Args:
        priority (list[str]): A list of possible priorities to match.
            Priorities can be specified by name or number, with the
            values: Diagnostic(0), Low(1), Medium(2), High(3),
            Critical(4). Optional.
        state (list[str]): A list of states to allow. Valid values:
            "ClearUnacked", "ClearAcked", "ActiveUnacked",
            "ActiveAcked". Optional.
        path (list[str]): A list of possible source paths to search at.
            The wildcard "*" may be used. Works the same as the source
            argument, and either can be used. Optional.
        source (list[str]): A list of possible source paths to search
            at. The wildcard "*" may be used. Works the same as the path
            argument, and either can be used. Optional.
        displaypath (list[str]): A list of display paths to search at.
            Display paths are separated by "/", and if a path ends in
            "/*", everything below that path will be searched as well.
            Optional.
        all_properties (list[object]): A set of property conditions, all
            of which must be met for the condition to pass. This
            parameter is a list of tuples, in the form ("propName",
            "condition", value). Valid condition values: "=", "!=", "<",
            "<=", ">", ">=". Only the first two conditions may be used
            for string values. Optional.
        any_properties (list[object]): A set of property conditions, any
            of which will cause the overall the condition to pass. This
            parameter is a list of tuples, in the form ("propName",
            "condition", value). Valid condition values: "=", "!=", "<",
            "<=", ">", ">=". Only the first two conditions may be used
            for string values. Optional.
        defined (list[str]): A list of string property names, all of
            which must be present on an event for it to pass. Optional.
        includeShelved (bool): A flag indicating whether shelved events
            should be included in the results. Defaults to "False".
            Optional.

    Returns:
        AlarmQueryResult: The AlarmQueryResult object is functionally a
            list of AlarmEvent objects. The AlarmQueryResult object has
            a built-in getDataset() function that will return a Standard
            Dataset containing the Event Id (UUID of the alarm), Source
            Path, Display Path, Event Time, State (as an integer), and
            Priority (as an integer).
    """
    print(
        priority,
        state,
        path,
        source,
        displaypath,
        all_properties,
        any_properties,
        defined,
        includeShelved,
    )
    return AlarmQueryResult()


def shelve(path, timeoutSeconds=None, timeoutMinutes=None):
    """This function shelves the specified alarms for the specified
    amount of time.

    The paths may be either source paths, or display paths. The time can
    be specified in minutes (timeoutMinutes) or seconds
    (timeoutSeconds). If an alarm is already shelved, this will
    overwrite the remaining time. To unshelve alarms, this function may
    be used with a time of "0".

    Args:
        path (list[str]): A list of possible source paths to search at.
            If a path ends in "/*", the results will include anything
            below that path.
        timeoutSeconds (int): The amount of time to shelve the matching
            alarms for, specified in seconds. 0 indicates that matching
            alarm events should now be allowed to pass. Optional.
        timeoutMinutes (int): The amount of time to shelve the matching
            alarms for, specified in minutes. 0 indicates that matching
            alarm events should now be allowed to pass. Optional.
    """
    print(path, timeoutSeconds, timeoutMinutes)


def unshelve(path):
    """Unshelves alarms in accordance with the path parameter.

    Args:
        path (list[str]): A list of possible source paths to search at.
            If a path ends in "/*", the results will include anything
            below that path.
    """
    print(path)
