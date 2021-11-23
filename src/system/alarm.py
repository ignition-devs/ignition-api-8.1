"""Alarm Functions.

The following functions give you access to view and interact with the
Alarm system in Ignition.
"""

from __future__ import print_function, unicode_literals

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
from java.util import Date


def acknowledge(
    alarmIds,  # type: List[Union[str, unicode]]
    notes=None,  # type: Optional[Union[str, unicode]]
    username=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> None
    """Acknowledges any number of alarms, specified by their event ids.

    The event id is generated for an alarm when it becomes active, and
    is used to identify a particular event from other events for the
    same source. The alarms will be acknowledged by the logged in user
    making the call. Additionally, acknowledgement notes may be included
    and will be stored along with the acknowledgement.

    Args:
        alarmIds: List of alarm event ids (uuids) to acknowledge.
        notes: Notes that will be stored on the acknowledged alarm
            events. Optional.
        username: The user that acknowledged the alarm. NOTE that this
            parameter is only used when called from a gateway scoped
            script. This parameter should be omitted from any
            client-based scripts. Optional.
    """
    print(alarmIds, notes, username)


def cancel(alarmIds):
    # type: (List[Union[str, unicode]]) -> None
    """Cancels any number of alarms, specified by their event ids.

    The event id is generated for an alarm when it becomes active, and
    is used to identify a particular event from other events for the
    same source. The alarm will still be active, but will drop out of
    alarm pipelines.

    Args:
        alarmIds: List of alarm event ids (uuids) to cancel.
    """
    print(alarmIds)


def createRoster(name, description):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """This function creates a new roster. Users may be added to the
    roster through the Gateway or the Roster Management component.

    Args:
        name: The name for the new roster.
        description: A description for the new roster. Required, but can
            be blank.
    """
    print(name, description)


def getRosters():
    # type: () -> Dict[Union[str, unicode], List[Union[str, unicode]]]
    """This function returns a mapping of roster names to a list of
    usernames contained in the roster.

    Returns:
        A dictionary that maps roster names to a List of usernames in
        the roster. The List of usernames may be empty if no users have
        been added to the roster.
    """
    return {}


def getShelvedPaths():
    # type: () -> List[ShelvedPath]
    """A list of ShelvedPath objects.

    ShelvedPath objects can be examined with getExpiration, getHitCount,
    getPath, getShelveTime, getUser, and isExpired.

    Returns:
        A list of ShelvedPath objects. ShelvedPath objects can be
        examined with getExpiration, getHitCount, getPath,
        getShelveTime, getUser, and isExpired.
    """
    return [ShelvedPath()]


def listPipelines(projectName="alarm-pipelines"):
    # type: (Optional[Union[str, unicode]]) -> List[Union[str, unicode]]
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
    journalName=None,  # type: Optional[Union[str, unicode]]
    priority=None,  # type: Optional[List[Union[str, unicode]]]
    state=None,  # type: Optional[List[Union[str, unicode]]]
    path=None,  # type: Optional[List[Union[str, unicode]]]
    source=None,  # type: Optional[List[Union[str, unicode]]]
    displaypath=None,  # type: Optional[List[Union[str, unicode]]]
    all_properties=None,  # type: Optional[List[Tuple[Union[str, unicode], Union[str, unicode], Any]]]
    any_properties=None,  # type: Optional[List[Tuple[Union[str, unicode], Union[str, unicode], Any]]]
    defined=None,  # type: Optional[List[Union[str, unicode]]]
    includeData=None,  # type: Optional[bool]
    includeSystem=None,  # type: Optional[bool]
    isSystem=None,  # type: Optional[bool]
):
    # type: (...) -> AlarmQueryResultImpl
    """Queries the specified journal for historical alarm events.

    The result is a list of alarm events, which can be queried for
    individual properties. The result object also has a getDataset()
    function that can be used to convert the query results into a normal
    dataset, with the columns: EventId, Source, DisplayPath, EventTime,
    EventState, Priority, IsSystemEvent.

    Args:
        startDate: The start of the time range to query. Defaults to 8
            hours previous to now if omitted. Time range is inclusive.
        endDate: The end of the time range to query. Defaults to "now"
            if omitted.
        journalName: The journal name to query.
        priority: A list of possible priorities to match. Priorities can
            be specified by name or number, with the values:
            Diagnostic(0), Low(1), Medium(2), High(3), Critical(4).
        state: A list of the event state types to match. Valid values
            are "ClearUnacked", "ClearAcked", "ActiveUnacked", and
            "ActiveAcked".
        path: A list of possible source paths to search at. The wildcard
            "*" may be used.
        source: A list of possible source paths to search at. The
            wildcard "*" may be used.
        displaypath: A list of display paths to search at. Display paths
            are separated by "/", and if a path ends in "/*", everything
            below that path will be searched as well.
        all_properties: A set of property conditions, all of which must
            be met for the condition to pass. This parameter is a list
            of tuples, in the form ("propName", "condition", value).
            Valid condition values: "=", "!=", "<", "<=", ">", ">=".
            Only the first two conditions may be used for string values.
        any_properties: A set of property conditions, any of which will
            cause the overall the condition to pass. This parameter is a
            list of tuples, in the form ("propName", "condition",
            value). Valid condition values: "=", "!=", "<", "<=", ">",
            ">=". Only the first two conditions may be used for string
            values.
        defined: A list of string property names, all of which must be
            present on an event for it to pass.
        includeData: Whether or not event data should be included in the
            return. If this parameter is False, and if there are no
            conditions specified on associated data, the properties
            table will not be queried.
        includeSystem: Specifies whether system events are included in
            the return.
        isSystem: Specifies whether the returned event must or must not
            be a system event.

    Returns:
        The AlarmQueryResult object is functionally a list of AlarmEvent
        objects. The AlarmQueryResult object has a built-in getDataset()
        function that will return a Standard Dataset containing the
        Event Id (UUID of the alarm), Source Path, Display Path, Event
        Time, State (as an integer), and Priority (as an integer).
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
    priority=None,  # type: Optional[List[Union[str, unicode]]]
    state=None,  # type: Optional[List[Union[str, unicode]]]
    path=None,  # type: Optional[List[Union[str, unicode]]]
    source=None,  # type: Optional[List[Union[str, unicode]]]
    displaypath=None,  # type: Optional[List[Union[str, unicode]]]
    all_properties=None,  # type: Optional[List[Tuple[Union[str, unicode], Union[str, unicode], Any]]]
    any_properties=None,  # type: Optional[List[Tuple[Union[str, unicode], Union[str, unicode], Any]]]
    defined=None,  # type: Optional[List[Union[str, unicode]]]
    includeShelved=False,  # type: Optional[bool]
):
    # type: (...) -> AlarmQueryResultImpl
    """Queries the current state of alarms.

    The result is a list of alarm events, which can be queried for
    individual properties. The result object also has a getDataset()
    function that can be used to convert the query results into a normal
    dataset, with the columns: EventId, Source, DisplayPath, EventTime,
    State, Priority.

    Args:
        priority: A list of possible priorities to match. Priorities can
            be specified by name or number, with the values:
            Diagnostic(0), Low(1), Medium(2), High(3), Critical(4).
        state: A list of states to allow. Valid values: "ClearUnacked",
            "ClearAcked", "ActiveUnacked", "ActiveAcked".
        path: A list of possible source paths to search at. The
            wildcard "*" may be used. Works the same as the source
            argument, and either can be used.
        source: A list of possible source paths to search at. The
            wildcard "*" may be used. Works the same as the path
            argument, and either can be used.
        displaypath: A list of display paths to search at. Display paths
            are separated by "/", and if a path ends in "/*", everything
            below that path will be searched as well.
        all_properties: A set of property conditions, all of which must
            be met for the condition to pass. This parameter is a list
            of tuples, in the form ("propName", "condition", value).
            Valid condition values: "=", "!=", "<", "<=", ">", ">=".
            Only the first two conditions may be used for string values.
        any_properties: A set of property conditions, any of which will
            cause the overall the condition to pass. This parameter is a
            list of tuples, in the form ("propName", "condition",
            value). Valid condition values: "=", "!=", "<", "<=", ">",
            ">=". Only the first two conditions may be used for string
            values.
        defined: A list of string property names, all of which must be
            present on an event for it to pass.
        includeShelved: A flag indicating whether shelved events should
            be included in the results. Defaults to "False".

    Returns:
        The AlarmQueryResult object is functionally a list of AlarmEvent
        objects. The AlarmQueryResult object has a built-in getDataset()
        function that will return a Standard Dataset containing the
        Event Id (UUID of the alarm), Source Path, Display Path, Event
        Time, State (as an integer), and Priority (as an integer).
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


def shelve(path, timeoutSeconds=None, timeoutMinutes=None):
    # type: (List[Union[str, unicode]], int, int) -> None
    """This function shelves the specified alarms for the specified
    amount of time.

    The paths may be either source paths, or display paths. The time can
    be specified in minutes (timeoutMinutes) or seconds
    (timeoutSeconds). If an alarm is already shelved, this will
    overwrite the remaining time. To unshelve alarms, this function may
    be used with a time of "0".

    Args:
        path: A list of possible source paths to search at. If a path
            ends in "/*", the results will include anything below that
            path.
        timeoutSeconds: The amount of time to shelve the matching alarms
            for, specified in seconds. 0 indicates that matching alarm
            events should now be allowed to pass.
        timeoutMinutes: The amount of time to shelve the matching alarms
            for, specified in minutes. 0 indicates that matching alarm
            events should now be allowed to pass.
    """
    print(path, timeoutSeconds, timeoutMinutes)


def unshelve(path):
    # type: (List[Union[str, unicode]]) -> None
    """Unshelves alarms in accordance with the path parameter.

    Args:
        path: A list of possible source paths to search at. If a path
            ends in "/*", the results will include anything below that
            path.
    """
    print(path)
