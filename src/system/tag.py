"""Tag Functions.

The following functions give you access to interact with Ignition Tags.
"""

from __future__ import print_function

__all__ = [
    "DEFAULT_TIMEOUT_MILLIS",
    "LEGACY_DEFAULT_TIMEOUT_MILLIS",
    "TAG_PATH",
    "browse",
    "browseHistoricalTags",
    "configure",
    "copy",
    "deleteAnnotations",
    "deleteTags",
    "exists",
    "exportTags",
    "getConfiguration",
    "importTags",
    "isOverlaysEnabled",
    "move",
    "query",
    "queryAnnotations",
    "queryTagCalculations",
    "queryTagDensity",
    "queryTagHistory",
    "readAsync",
    "readBlocking",
    "rename",
    "requestGroupExecution",
    "setOverlaysEnabled",
    "storeAnnotations",
    "storeTagHistory",
    "writeAsync",
    "writeBlocking",
]

from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.history.annotations import (
    Annotation,
)
from java.lang import String
from java.util import Date

DEFAULT_TIMEOUT_MILLIS = 45000
LEGACY_DEFAULT_TIMEOUT_MILLIS = 45000
TAG_PATH = None  # type: Any


def browse(path, filter=None):
    # type: (String, Optional[Dict[String, Any]]) -> Results
    """Returns a list of tags found at the specified Tag path.

    The list objects are returned as dictionaries with some basic
    information about each Tag.

    Args:
        path: The path that will be browsed, typically to a folder or
            UDT instance.
        filter: A dictionary of browse filter keys.

    Returns:
        A Results object which contains a list of Tag dictionaries, one
        for each Tag found during the browse.
    """
    print(path, filter)
    return Results()


def browseHistoricalTags(
    path,  # type: String
    nameFilters=None,  # type: Optional[List[String]]
    maxSize=None,  # type: Optional[int]
    continuationPoint=None,  # type: Optional[Any]
):
    # type: (...) -> Results
    """Will browse for any historical Tags at the provided historical
    path.

    It will only browse for Tags at the path, and will not go down
    through any children. Will return with a BrowseResults object.

    Args:
        path: The Historical Tag Path to browse.
        nameFilters: A list of name filters to be applied to the result
            set. Optional.
        maxSize: The maximum size of the result set. Optional.
        continuationPoint: Sets the continuation point in order to
            continue a browse that was previously started and then
            limited. Use getContinuationPoint() on the Results object to
            get the continuation point. Optional.

    Returns:
        A Results object which contains a list of Tag dictionaries, one
        for each Tag found during the browse.
    """
    print(path, nameFilters, maxSize, continuationPoint)
    return Results()


def configure(
    basePath,  # type: String
    tags,  # type: List[Dict[String, Any]]
    collisionPolicy="o",  # type: String
):
    # type: (...) -> List[QualityCode]
    """Creates Tags from a given list of Python dictionaries or from a
    JSON source string.

    Can be used to overwrite a current Tag's configuration.

    When utilizing this function, the Tag definitions must specify the
    names of properties with their scripting/JSON name.

    Args:
        basePath: The starting point where the new Tags will be created.
            When making changes to existing tags with this function,
            you want to set the path to the parent folder of the
            existing Tag(s), not the Tag(s) themselves.
        tags: A list of Tag definitions, where each Tag definition is a
            Python dictionary. Alternately, a JSON source string may be
            passed to this parameter. When editing existing tags, it is
            generally easier to retrieve the Tag configurations with
            system.Tag.getConfiguration, modify the results of the
            getConfiguration call, and then write the new configuration
            to the parent folder of the existing Tag(s).
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include:

            a - Abort and throw an exception
            o - Overwrite and replace existing Tag's configuration
            i - Ignore that item in the list
            m - Merge, modifying values that are specified in the
                definition, without impacting values that aren't defined
                in the definition. Use this when you want to apply a
                slight change to tags, without having to build a
                complete configuration object.

            Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(basePath, tags, collisionPolicy)
    return [QualityCode() for _ in tags]


def copy(
    tags,  # type: List[String]
    destination,  # type: String
    collisionPolicy="o",  # type: String
):
    # type: (...) -> List[QualityCode]
    """Copies tags from one folder to another.

    Multiple Tag and folder paths may be passed to a single call of this
    function. The new destination can be a separate Tag provider.

    Args:
        tags: A List of Tag paths to move.
        destination: The destination to copy the Tags to. All specified
            tags will be copied to the same destination. The destination
            Tag provider must be specified.
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode() for _ in tags]


def deleteAnnotations(paths, storageIds):
    # type: (List[String], List[String]) -> List[BasicQualifiedValue]
    """Removes stored annotations from the sqlth_annotations table.

    Requires the full Tag path (including history provider) for each
    annotation, as well as each annotation's storage ID.

    The function expects two lists (PySequences) of equal length. The
    items in each list is 1-to-1, meaning the first item in the "paths"
    list relates to the first item in the "storageIds" list, the second
    item in "paths" relates to the second item in "storageIds", etc.

    Args:
        paths: A list of Tag paths with existing annotations. The paths
            are equivalent to what would be used for a Tag history
            query, and should specify the source provider as well. For
            example, "[HistoryProvider/Gateway:Provider]Path/To/Tag".
        storageIds: A sequence of storage identifiers that will be
            deleted. Storage ID values can be retrieved with
            system.tag.queryAnnotations.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure, and if successful, the storage id of the
        annotation will have been deleted.
    """
    print(paths, storageIds)
    return [BasicQualifiedValue()]


def deleteTags(tagPaths):
    # type: (List[String]) -> List[QualityCode]
    """Deletes multiple Tags or Tag Folders.

    When deleting a Tag Folder, all Tags under the folder are also
    deleted.

    Args:
        tagPaths: A List of the paths to the Tags or Tag Folders that
            are to be removed.

    Returns:
         A List of QualityCode objects, one for each Tag in the list,
         that is representative of the result of the operation.
    """
    print(tagPaths)
    return [QualityCode() for _ in tagPaths]


def exists(tagPath):
    # type: (String) -> bool
    """Checks whether or not a Tag with a given path exists.

    Args:
        tagPath: The path of the Tag to look up.

    Returns:
        True if a Tag exists for the given path, False otherwise.
    """
    print(tagPath)
    return True


def exportTags(
    filePath,  # type: String
    tagPaths,  # type: List[String]
    recursive=True,  # type: bool
    exportType="json",  # type: String
):
    # type: (...) -> None
    """Exports Tags to a file on a local file system.

    The term "local file system" refers to the scope in which the script
    was running; for example, running this script in a Gateway Timer
    script will export the file to the Gateway file system.

    Args:
        filePath: The file path that the Tags will be exported to. If
            the file does not already exist, this function will attempt
            to create it.
        tagPaths: A List of Tag paths to export. All Tag paths in the
            list must be from the same parent folder.
        recursive: Set to True to export all Tags under each Tag path,
            including Tags in child folders. Defaults to True. Optional.
        exportType: The type of file that will be exported. Set to
            "json" or "xml". Defaults to "json". Optional.
    """
    print(filePath, tagPaths, recursive, exportType)


def getConfiguration(basePath, recursive=False):
    # type: (String, bool) -> List[Dict[String, Any]]
    """Retrieves Tags from the Gateway as Python dictionaries.

    These can be edited and then saved back using system.tag.configure.

    Args:
        basePath: The starting point where the Tags will be retrieved.
            This can be a folder containing, and if recursive is True,
            then the function will attempt to retrieve all of the tags
            in the folder.
        recursive: If True, the entire Tag Tree under the specified path
            will be retrieved. Note that this will only check one level
            under the base path. True recursion would require multiple
            uses of this function at different paths. Optional.

    Returns:
         A List of Tag dictionaries. Nested Tags are placed in a list
         marked as "tags" in the dictionary.
    """
    print(basePath, recursive)
    return [{}]


def importTags(filePath, basePath, collisionPolicy="o"):
    # type: (String, String, String) -> List[QualityCode]
    """Imports a JSON Tag file at the provided path.

    Also supports XML and CSV Tag file exports from legacy systems.

    Args:
        filePath: The file path of the Tag export to import.
        basePath: The Tag path that will serve as the root node for the
            imported Tags.
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(filePath, basePath, collisionPolicy)
    return [QualityCode()]


def isOverlaysEnabled():
    # type: () -> bool
    """Returns whether or not the current client's quality overlay
    system is currently enabled.

    Returns:
         True if overlays are currently enabled.
    """
    return False


def move(tags, destination, collisionPolicy="o"):
    # type: (String, String, String) -> List[QualityCode]
    """Moves Tags or Folders to a new destination.

    The new destination can be a separate Tag provider. If interested in
    copying the tags to a new destination, instead of moving them,
    please see the system.tag.copy page.

    Args:
        tags: A List of Tag paths to move.
        destination: The destination to move the Tags to. The
            destination Tag provider must be specified: i.e.,
            [default]Folder/myTag
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode() for _ in tags]


def query(
    provider=None,  # type: Optional[String]
    query=None,  # type: Optional[Dict[String, Any]]
    limit=None,  # type: Optional[int]
    continuation=None,  # type: Optional[String]
):
    # type: (...) -> Results
    """Queries a Tag Provider to produce a list of tags that meet the
    specified criteria.

    Args:
        provider: The Tag Provider to query. Optional.
        query: A JSON document that specifies the query conditions.
            Optional.
        limit: Maximum results to return. If more results are possible,
            the result will have a continuation point set. Optional.
        continuation: The Tag ID of a previously returned
            continuation point, to continue the associated query from
            that point. Optional.

    Returns:
        A dataset representing the results of the query.
    """
    print(provider, query, limit, continuation)
    return Results()


def queryAnnotations(
    paths,  # type: List[String]
    startTime=None,  # type: Optional[Date]
    endTime=None,  # type: Optional[Date]
    types=None,  # type: Optional[List[String]]
):
    # type: (...) -> List[Annotation]
    """Queries user stored annotations from the Tag history system for a
    set of paths, for a given time range.

    Args:
        paths: A list of Tag paths to query. The paths are equivalent to
            what would be used ofr a Tag history query, and should
            specify the source provider as well. For example,
            "[HistoryProvider/Gateway:Provider]Path/To/Tag".
        startTime: The start of the time range. If not defined, defaults
            to 12 hours ago. Optional.
        endTime: The end of time range. If not defined, defaults to
            "now". Optional.
        types: A list of string "types" to filter on. Types are defined
            by the annotations and various subsystems, and may vary with
            different providers. Possible annotation types are listed on
            the system.Tag.storeAnnotations page. Optional.

    Returns:
        A list of Annotation objects that match the query criteria.
    """
    print(paths, startTime, endTime, types)
    return [Annotation()]


def queryTagCalculations(
    paths,  # type: List[String]
    calculations,  # type: List[String]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    rangeHours=None,  # type: Optional[int]
    rangeMinutes=None,  # type: Optional[int]
    aliases=None,  # type: Optional[List[String]]
    includeBoundingValues=True,  # type: bool
    validatesSCExec=True,  # type: bool
    noInterpolation=False,  # type: bool
    ignoreBadQuality=False,  # type: bool
):
    # type: (...) -> BasicDataset
    """Queries various calculations (aggregations) for a set of tags
    over a specified range.

    Returns a dataset with a row per Tag, and a column per calculation.

    This is useful when you wish to aggregate Tag history collected over
    a period of time into a single value per aggregate. If you want
    multiple values aggregated to a single time slice (i.e., hourly
    aggregates for the same Tag over an 8 hour period) consider using
    system.Tag.queryTagHistory

    Args:
        paths: An array of Tag paths (strings) to query calculations
            for. The resulting dataset will have a row for each Tag, and
            a column for each calculation.
        calculations: An array of calculations (aggregation functions)
            to execute for each Tag. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad".
        startDate: The starting point for the calculation window. If
            omitted, and range is not used, 8 hours before the current
            time is used. Optional.
        endDate: The end of the calculation window. If omitted, and
            range is not used, uses the current time. Optional.
        rangeHours: Allows you to specify the query range in hours,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate. Optional.
        rangeMinutes: Same as rangeHours, but in minutes. Optional.
        aliases: Aliases that will be used to override the Tag path
            names in the result dataset. Must be 1-to-1 with the Tag
            paths. If not specified, the Tag paths themselves will be
            used. Optional.
        includeBoundingValues: A boolean flag indicating that the system
            should attempt to load values before and after the query
            bounds for the purpose of interpolation. The effect depends
            on the aggregates used. The default is True. Optional.
        validatesSCExec: A boolean flag indicating whether or not data
            should be validated against the scan class execution
            records. If False, calculations may include data that is
            assumed to be good, even though the system may not have been
            running. Default is True. Optional.
        noInterpolation: A boolean flag indicating that the system
            should not attempt to interpolate values in situations where
            it normally would, such as for analog tags. Default is
            False. Optional.
        ignoreBadQuality: A boolean flag indicating that bad quality
            values should not be used in the query process. If set, any
            value with a "bad" quality will be completely ignored in
            calculations. Default is False. Optional.

    Returns:
        A dataset representing the calculations over the specified
        range.
    """
    print(
        paths,
        calculations,
        startDate,
        endDate,
        rangeHours,
        rangeMinutes,
        aliases,
        includeBoundingValues,
        validatesSCExec,
        noInterpolation,
        ignoreBadQuality,
    )
    return BasicDataset()


def queryTagDensity(paths, startDate, endDate):
    # type: (List[String], Date, Date) -> BasicDataset
    """Queries the Tag history system for information about the density
    of data.

    In other words, how much data is available for a given time
    span.

    This function is called with a list of Tag paths, and a start and
    end date. The result set is a two column dataset specifying the
    timestamp, and a relative weight. Each row is valid from the given
    time until the next row. Tags are assigned a 1 or a 0 if they are
    present or not. All values are then multiplied together to get a
    decimal based percentage for the density. Thus, for four Tag paths
    passed in, if three Tags were present during the span, the result
    would be 0.75.

    Note:
        This function relies on being able to validate the data against
        tag group execution. This function will be unable to return
        density information for tags that were stored by an Internal
        Historian Provider, as well as cases where tag group validation
        is disabled (such as by disabling Enable State Data Detection).

    Args:
        paths: An array of Tag paths (strings) to query.
        startDate: The start of the range to query.
        endDate: The end of the range to query.

    Returns:
        A two-column dataset consisting of a timestamp and a weight.
        Each row is valid until the next row.
    """
    print(paths, startDate, endDate)
    return BasicDataset()


def queryTagHistory(
    paths,  # type: List[String]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    returnSize=-1,  # type: int
    aggregationMode="Average",  # type: String
    returnFormat="Wide",  # type: String
    columnNames=None,  # type: Optional[List[String]]
    intervalHours=None,  # type: Optional[int]
    intervalMinutes=None,  # type: Optional[int]
    rangeHours=None,  # type: Optional[int]
    rangeMinutes=None,  # type: Optional[int]
    aggregationModes=None,  # type: Optional[List[String]]
    includeBoundingValues=None,  # type: Optional[bool]
    validateSCExec=None,  # type: Optional[bool]
    noInterpolation=None,  # type: Optional[bool]
    ignoreBadQuality=None,  # type: Optional[bool]
    timeout=None,  # type: Optional[int]
    intervalSeconds=None,  # type: Optional[int]
    rangeSeconds=None,  # type: Optional[int]
):
    # type: (...) -> BasicDataset
    """Issues a query to the Tag Historian.

    Querying Tag history involves specifying the tags and the date
    range, as well as a few optional parameters. The Tag historian will
    find the relevant history and then interpolate and aggregate it
    together into a coherent, tabular result set.

    Args:
        paths: An array of Tag paths (strings) to query. Each Tag path
            specified will be a column in the result dataset.
        startDate: The earliest value to retrieve. If omitted, 8 hours
            before current time is used. Optional.
        endDate: The latest value to retrieve. If omitted, current time
            is used. Optional.
        returnSize: The number of samples to return. -1 will return
            values as they changed, and 0 will return the "natural"
            number of values based on the logging rates of the scan
            class(es) involved. -1 is the default. Optional.
        aggregationMode: The mode to use when aggregating multiple
            samples into one time slice. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad". Optional.
        returnFormat: Use "Wide" to have a column per Tag queried, or
            "Tall" to have a fixed-column format. Default is "Wide".
            Optional.
        columnNames: Aliases that will be used to override the column
            names in the result dataset. Must be 1-to-1 with the Tag
            paths. If not specified, the Tag paths themselves will be
            used as column titles. Optional.
        intervalHours: Allows you to specify the window interval in
            terms of hours, as opposed to using a specific return size.
            Optional.
        intervalMinutes: Same as intervalHours, but in minutes. Can be
            used on its own, or in conjunction with intervalHours.
            Optional.
        rangeHours: Allows you to specify the query range in hours,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate. Optional.
        rangeMinutes: Same as rangeHours, but in minutes. Optional.
        aggregationModes: A one-to-one list with paths specifying an
            aggregation mode per column. Optional.
        includeBoundingValues: A boolean flag indicating that the system
            should attempt to include values for the query bound times
            if possible. The default for this property depends on the
            query mode, so unless a specific behavior is desired, it is
            best to not include this parameter. Optional.
        validateSCExec: A boolean flag indicating whether or not data
            should be validated against the scan class execution
            records. If False, data will appear flat (but good quality)
            for periods of time in which the system wasn't running. If
            True, the same data would be bad quality during downtime
            periods. Optional.
        noInterpolation: A boolean flag indicating that the system
            should not attempt to interpolate values in situations where
            it normally would. This will also prevent the return of rows
            that are purely interpolated. Optional.
        ignoreBadQuality: A boolean flag indicating that bad quality
            values should not be used in the query process. If set, any
            value with a "bad" quality will be completely ignored in
            calculations and in the result set. Optional.
        timeout: Timeout in milliseconds for Client Scope. This property
            is ignored in the Gateway Scope. Optional.
        intervalSeconds: Same as intervalHours and interval Minutes, but
            in seconds. Can be used on its own, or in conjunction with
            intervalHours and intervalMinutes. Optional.
        rangeSeconds: Allows you to specify the query range in seconds,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate. Optional.

    Returns:
        A dataset representing the historian values for the specified
        Tag paths. The first column will be the timestamp, and each
        column after that represents a Tag.
    """
    print(
        paths,
        startDate,
        endDate,
        returnSize,
        aggregationMode,
        returnFormat,
        columnNames,
        intervalHours,
        intervalMinutes,
        rangeHours,
        rangeMinutes,
        aggregationModes,
        includeBoundingValues,
        validateSCExec,
        noInterpolation,
        ignoreBadQuality,
        timeout,
        intervalSeconds,
        rangeSeconds,
    )
    return BasicDataset()


def readAsync(tagPaths, callback):
    # type: (List[String], Callable[..., Any]) -> None
    """Asynchronously reads the value of the Tags at the given paths.

    You must provide a python callback function that can process the
    read results.

    Args:
        tagPaths: A List of Tag paths to read from. If no property is
            specified in the path, the Value property is assumed.
        callback: A Python callback function to process the read
            results. The function definition must provide a single
            argument, which will hold a List of qualified values when
            the callback function is invoked. The qualified values will
            have three sub members: value, quality, and timestamp.
    """
    print(tagPaths, callback)


def readBlocking(tagPaths, timeout=45000):
    # type: (List[String], int) -> List[BasicQualifiedValue]
    """Reads the value of the Tags at the given paths.

    Will block until the read operation is complete or times out.

    Args:
        tagPaths: A List of Tag paths to read from. If no property is
            specified in a path, the Value property is assumed.
        timeout: How long to wait in milliseconds before the read
            operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified. Optional.

    Returns:
        A list of QualifiedValue objects corresponding to the Tag paths.
    """
    print(tagPaths, timeout)
    return [BasicQualifiedValue() for _ in tagPaths]


def rename(tag, newName, collisionPollicy="a"):
    # type: (String, String, String) -> QualityCode
    """Renames a single Tag or folder.

    Args:
        tag: A path to the Tag or folder to rename.
        newName: The new name for the tag or folder.
        collisionPollicy: The action to take when a Tag or folder with
            the same path and names is encountered. Possible values
            include "a" (Abort, throws an exception), "o" (Overwrite,
            completely replaces a Tag's configuration), and "i"
            (Ignore). Defaults to Abort if not specified. Optional.

    Returns:
        A QualityCode object that contains the result of the rename
        operation.
    """
    print(tag, newName, collisionPollicy)
    return QualityCode()


def requestGroupExecution(provider, tagGroup):
    # type: (String, String) -> None
    """Sends a request to the specified Tag Group to execute now.

    Args:
        provider: Name of the Tag Provider that the Tag Group is in.
        tagGroup: The name of the Tag Group to execute.
    """
    print(provider, tagGroup)


def setOverlaysEnabled(enabled):
    # type: (bool) -> None
    """Enables or disables the component quality overlay system.

    Args:
        enabled: True to turn on Tag overlays, False to turn
            them off.
    """
    print(enabled)


def storeAnnotations(
    paths,  # type: List[String]
    startTimes=None,  # type: Optional[List[Date]]
    endTimes=None,  # type: Optional[List[Date]]
    types=None,  # type: Optional[List[Annotation]]
    data=None,  # type: Optional[List[String]]
    storageIds=None,  # type: Optional[List[int]]
    deleted=None,  # type: Optional[List[bool]]
):
    # type: (...) -> List[BasicQualifiedValue]
    """Stores annotations into the Tag history system.

    Annotations are stored by the underlying historian implementations,
    so different providers may store in different ways, and some
    providers may not support annotation storage. All parameters are
    1-to-1, so all provided lists should be of the same length. If a
    particular annotation doesn't need a parameter, that element can be
    None in the list.

    Args:
        paths: A list of Tag paths to store for. The paths are
            equivalent to what would be used for a Tag history query,
            and should specify the source provider as well. For example,
            "[HistoryProvider/Gateway:Provider]Path/To/Tag". This
            parameter is required, even if storage ids are included,
            because it is used to identify the underlying storage
            provider.
        startTimes: The start times of the events. If omitted, defaults
            to the current time. Optional.
        endTimes: The end times of the event, if applicable. If omitted,
            does not store an end time for the annotation. Optional.
        types: The type id for the annotation. If not defined, "marker"
            will be used. See the Annotation Types for more details.
            Optional.
        data: Data for the annotation, such as text describing the
            meaning of the annotation. Optional.
        storageIds: If defined, the function will instead update the
            existing annotation instead of adding new ones, overriding
            existing values for the annotation with those provided by
            this function (if the corresponding delete parameter is
            True). Storage id is available on the Annotation object, and
            is returned as the result value from the storeAnnotations
            call. Optional.
        deleted: A list of booleans indicating that the individual
            annotation should be deleted. Requires storage id to be set
            as well. Optional.

    Returns:
        A list of QualifiedValues. The quality code will indicate
        success or failure. If successful,  the storage id of the
        annotation will be returned in the value.
    """
    print(paths, startTimes, endTimes, types, data, storageIds, deleted)
    return [BasicQualifiedValue() for _ in paths]


def storeTagHistory(
    historyprovider,  # type: String
    tagprovider,  # type: String
    paths,  # type: List[String]
    values,  # type: List[Any]
    qualities=None,  # type: Optional[List[int]]
    timestamps=None,  # type: Optional[List[Date]]
):
    # type: (...) -> None
    """Inserts data into the Tag history system, allowing Tag history to
    be recorded via scripting.

    The Tag paths are associated with a historical and realtime
    provider, but they do not necessarily need to exist in the realtime
    provider. This means records from non-existent (virtual) Tags can be
    stored in the Tag History system. Because of this, it is imperative
    that Tag paths passed to the function are typed precisely, otherwise
    the history will be stored at an incorrect path.

    Note that the Tag History system does cache Tag data. Thus, if this
    function is called, the Tag path and Tag id are cached until the
    history provider or gateway are restarted. This means manually
    removing the Tag from the sqlth_te table, and then calling this
    function again with the same path will not re-populate the Tag
    execution table (especially so when working purely with virtual Tag
    paths). Instead, the cache must first be cleared, and then a new
    entry will be added the next time this function is called.

    If a Tag's datatype changes after recording Tag history, this
    function will create a new entry in the sqlth_te table to reflect
    the change.

    Args:
        historyprovider: The historical provider to store to.
        tagprovider: The name of the realtime Tag provider to associate
            these tags with. The Tag provider does not need to exist,
            and the Tag paths do not need to exist in it.
        paths: A list of paths to store. The values, qualities, and
            timestamps are one-to-one with the paths. A single path may
            be present multiple times in order to store multiple values.
        values: A list of values to store.
        qualities: A list of integer quality codes corresponding to the
            values. Quality codes can be found on the Tag Quality and
            Overlays page. If omitted, GOOD quality will be used.
            Optional.
        timestamps: A list of Date timestamps corresponding to the
            values. If omitted, the current time will be used. A
            java.util.date object may be passed, so the system.date
            functions can be used to return a timestamp. Optional.
    """
    print(historyprovider, tagprovider, paths, values, qualities, timestamps)


def writeAsync(
    tagPaths,  # type: List[String]
    values,  # type: List[Any]
    callback=None,  # type: Optional[Callable[..., Any]]
):
    # type: (...) -> None
    """Asynchronously writes values to Tags a the given paths.

    You must provide a Python callback function that can process the
    write results.

    Args:
        tagPaths: A List of Tag paths to write to. If no property is
            specified in a Tag path, the Value property is assumed.
        values: The values to write to the specified paths.
        callback: A Python callback function to process the write
            results. The function definition must provide a single
            argument: a List of QualityCode objects corresponding to the
            results of the write operation. Optional.
    """
    print(tagPaths, values, callback)


def writeBlocking(
    tagPaths,  # type: List[String]
    values,  # type: List[Any]
    timeout=45000,  # type: int
):
    # type: (...) -> List[QualityCode]
    """Writes values to Tags at the given paths.

    This function will block until the write operation is complete or
    times out.

    Args:
        tagPaths: A List of Tag paths to write to. If no property is
            specified in a Tag path, the Value property is assumed.
        values: The values to write to the specified paths.
        timeout: How long to wait in milliseconds before the write
            operation times out. This parameter is optional, and
            defaults to 45,000 milliseconds if not specified. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag path.
    """
    print(tagPaths, values, timeout)
    return [QualityCode() for _ in tagPaths]
