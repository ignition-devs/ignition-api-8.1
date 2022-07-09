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

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common.alarming.evaluation import ShelvedPath
from com.inductiveautomation.ignition.common.alarming.query import AlarmQueryResultImpl
from java.lang import String
from java.util import Date


def acknowledge(alarmIds, notes, username=None):
    # type: (List[String], String, Optional[String]) -> None
    """Acknowledges any number of alarms, specified by their event ids.

    The event id is generated for an alarm when it becomes active, and
    is used to identify a particular event from other events for the
    same source. The alarms will be acknowledged by the logged in user
    making the call. Additionally, acknowledgement notes may be included
    and will be stored along with the acknowledgement.

    Note:
         The `username` parameter is only used when called from a
         gateway scoped script. This parameter should be omitted from
         any client-based scripts.

    Args:
        alarmIds: List of alarm event ids (UUIDs) to acknowledge.
        notes: A string that will be used as the Ack Note on each
            acknowledged alarm event. If set to None, then an Ack Note
            note will not be assigned to the alarm event.
        username: The user that acknowledged the alarm.
    """
    print(alarmIds, notes, username)


def cancel(alarmIds):
    # type: (List[String]) -> None
    """Cancels any number of alarms, specified by their event ids.

    Event ids can be obtained from the system.alarm.queryStatus
    function. Canceling a pipeline will not impact the alarm that
    triggered the pipeline. The alarm will still be active, but will
    drop out of alarm pipelines.

    Args:
        alarmIds: List of alarm event ids (UUIDs) to cancel.
    """
    print(alarmIds)


def createRoster(name, description):
    # type: (String, String) -> None
    """This function creates a new roster.

    Users may be added to the roster through the Gateway or the Roster
    Management component.

    Args:
        name: The name for the new roster.
        description: A description for the new roster. Required, but can
            be blank.
    """
    print(name, description)


def getRosters():
    # type: () -> Dict[String, List[String]]
    """This function returns a mapping of roster names to a list of
    usernames contained in the roster.

    Returns:
        A dictionary that maps roster names to a List of usernames in
        the roster. The list of usernames may be empty if no users have
        been added to the roster.
    """
    return {}


def getShelvedPaths():
    # type: () -> List[ShelvedPath]
    """Returns a list of ShelvedPath objects, which each represent a
    shelved alarm.

    Returns:
        A list of ShelvedPath objects.
    """
    return [ShelvedPath()]


def listPipelines(projectName="alarm-pipelines"):
    # type: (String) -> List[String]
    """Will return a list of the available Alarm Notification Pipelines.

    Args:
        projectName: The project to check alarm pipelines for. If
            omitted, will look for a project named "alarm-pipelines".
            Optional.

    Returns:
        A list of pipeline names. The list may be empty if no pipelines
        exist. Unsaved name changes will not be reflected in the list.
    """
    print(projectName)
    return []


def queryJournal(
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    journalName=None,  # type: Optional[String]
    priority=None,  # type: Optional[List[Union[String, int]]]
    state=None,  # type: Optional[List[Union[String, int]]]
    path=None,  # type: Optional[List[String]]
    source=None,  # type: Optional[List[String]]
    displaypath=None,  # type: Optional[List[String]]
    all_properties=None,  # type: Optional[List[Tuple[String, String, Any]]]
    any_properties=None,  # type: Optional[List[Tuple[String, String, Any]]]
    defined=None,  # type: Optional[List[String]]
    includeData=None,  # type: Optional[bool]
    includeSystem=None,  # type: Optional[bool]
    isSystem=None,  # type: Optional[bool]
):
    # type: (...) -> AlarmQueryResultImpl
    """Queries the specified journal for historical alarm events.

    The result is a list of alarm events, which can be queried for
    individual properties.

    Note:
        Each item in the resulting object is a separate alarm event: an
        alarm becoming active is one item, while the same alarm becoming
        acknowledged is a separate item. This differs from
        `system.alarm.queryStatus()` which groups each event into a
        single item.

    Args:
        startDate: The start of the time range to query. Defaults to 8
            hours previous to now if omitted. Time range is inclusive.
            Optional.
        endDate: The end of the time range to query. Defaults to "now"
            if omitted. Optional.
        journalName: The journal name to query. If only one journal
            exists on the Gateway, can be omitted. Optional.
        priority: A list of possible priorities to match. Priorities can
            be specified by name or number, with the values:
            Diagnostic(0), Low(1), Medium(2), High(3), Critical(4).
            Optional.
        state: A list of the event state types to match. Valid values
            can either be integers or strings, representing a number of
            states. Optional.
        path: A list of possible source paths to search at. The wildcard
            "*" may be used. Optional.
        source: A list of possible source paths to search at. The
            wildcard "*" may be used. Optional.
        displaypath: A list of display paths to search at. Display paths
            are separated by "/", and if a path ends in "/*", everything
            below that path will be searched as well.
        all_properties: A set of property conditions, all of which must
            be met for the condition to pass. This parameter is a list
            of tuples, in the form ("propName", "condition", value).
            Valid condition values: "=", "!=", "<", "<=", ">", ">=".
            String values can only be compared using "=" and "!="
            conditions. Optional.
        any_properties: A set of property conditions, any of which will
            cause the overall condition to pass. This parameter is a
            list of tuples, in the form ("propName", "condition",
            value). Valid condition values: "=", "!=", "<", "<=", ">",
            ">=". String values can only be compared using "=" and "!="
            conditions. Optional.
        defined: A list of string property names, all of which must be
            present on an event for it to pass. Optional.
        includeData: Whether or not event data should be included in the
            return. If True, returns Python dictionaries (or nulls) for
            Active Data, Clear Data, Ack Data, Runtime Data inside of
            the AlarmQueryResult object. Optional.
        includeSystem: Specifies whether system events are included in
            the return. Optional.
        isSystem: Specifies whether the returned event must or must not
            be a system event. Optional.

    Returns:
        The AlarmQueryResult object is functionally a list of AlarmEvent
        objects.
    """
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
    return AlarmQueryResultImpl()


def queryStatus(
    priority=None,  # type: Optional[List[Union[String, int]]]
    state=None,  # type: Optional[List[Union[String, int]]]
    path=None,  # type: Optional[List[String]]
    source=None,  # type: Optional[List[String]]
    displaypath=None,  # type: Optional[List[String]]
    all_properties=None,  # type: Optional[List[Tuple[String, String, Any]]]
    any_properties=None,  # type: Optional[List[Tuple[String, String, Any]]]
    defined=None,  # type: Optional[List[String]]
    includeShelved=False,  # type: bool
):
    # type: (...) -> AlarmQueryResultImpl
    """Queries the current state of alarms.

    The result is a list of alarm events, which can be queried for
    individual properties. The results provided by this function
    represent the current state of alarms, in contrast to the historical
    alarm events retrieved by the `system.alarm.queryJournal` function.

    Note:
        Depending on the number of alarm events in the system, this
        function can be fairly intensive and take a while to finish
        executing. This can be problematic if the application is
        attempting to show the results on a component (such as using
        this function to retrieve a count of alarms). In these cases
        it's preferred to call this function in a gateway script of some
        sort (such as a timer script), and store the results in a tag.

    Args:
        priority: A list of possible priorities to match. Priorities can
            be specified by name or number, with the values:
            Diagnostic(0), Low(1), Medium(2), High(3), Critical(4).
            Optional.
        state: A list of states to allow. Optional.
        path: A list of possible source paths to search at. The
            wildcard "*" may be used. Works the same as the source
            argument, and either can be used. Optional.
        source: A list of possible source paths to search at. The
            wildcard "*" may be used. Works the same as the path
            argument, and either can be used. Optional.
        displaypath: A list of display paths to search at. Display paths
            are separated by "/", and if a path ends in "/*", everything
            below that path will be searched as well. Optional.
        all_properties: A set of property conditions, all of which must
            be met for the condition to pass. This parameter is a list
            of tuples, in the form ("propName", "condition", value).
            Valid condition values: "=", "!=", "<", "<=", ">", ">=".
            String values can only be compared using "=" and "!="
            conditions. Optional.
        any_properties: A set of property conditions, any of which will
            cause the overall the condition to pass. This parameter is a
            list of tuples, in the form ("propName", "condition",
            value). Valid condition values: "=", "!=", "<", "<=", ">",
            ">=". String values can only be compared using "=" and "!="
            conditions. Optional.
        defined: A list of string property names, all of which must be
            present on an event for it to pass. Optional.
        includeShelved: A flag indicating whether shelved events should
            be included in the results. Defaults to False. Optional.

    Returns:
        The AlarmQueryResult object is functionally a list of AlarmEvent
        objects with some additional helper methods.
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
    return AlarmQueryResultImpl()


def shelve(path, timeoutSeconds=0, timeoutMinutes=15):
    # type: (List[String], int, int) -> None
    """This function shelves the specified alarms for the specified
    amount of time.

    The time can be specified in minutes (timeoutMinutes) or seconds
    (timeoutSeconds). If an alarm is already shelved, this will
    overwrite the remaining time. If no timeout is specified, will
    default to 15 minutes.

    Args:
        path: A list of possible source paths to search at. If a path
            ends in "/*", the results will include anything below that
            path.
        timeoutSeconds: The amount of time to shelve the matching alarms
            for, specified in seconds. Setting this to 0 will unshelve
            the alarms. Optional.
        timeoutMinutes: The amount of time to shelve the matching alarms
            for, specified in minutes. Setting this to 0 will unshelve
            the alarms. Optional.
    """
    print(path, timeoutSeconds, timeoutMinutes)


def unshelve(path):
    # type: (List[String]) -> None
    """Unshelves a list of alarms based on the source paths provided.

    Args:
        path: A list of possible source paths to search at. If a path
            ends in "/*", the results will include anything below that
            path.
    """
    print(path)
