"""Tag Functions.

The following functions give you access to interact with Ignition Tags.
"""

from __future__ import print_function

__all__ = [
    "browse",
    "browseHistoricalTags",
    "browseTags",
    "browseTagsSimple",
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
    "queryAnnotations",
    "queryTagCalculations",
    "queryTagDensity",
    "queryTagHistory",
    "read",
    "readAll",
    "readAsync",
    "readBlocking",
    "rename",
    "requestGroupExecution",
    "setOverlaysEnabled",
    "storeAnnotations",
    "storeTagHistory",
    "write",
    "writeAll",
    "writeAsync",
    "writeBlocking",
]

import warnings

import system.date
from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.script.builtin.ialabs import (
    BrowseTag,
)
from java.util import Date


def browse(path, filter=None):
    """Returns a list of tags found at the specified tag path.

    The list objects are returned as dictionaries with some basic
    information about each tag.

    Args:
        path (str): The path that will be browsed, typically to a folder
            or UDT instance.
        filter (dict): A dictionary of browse filter parameters.
            Parameters include name (with wildcards), dataType,
            valueSource, tagType, typeId, quality (specify Good or Bad),
            and maxResults. The aforementioned wildcard character is the
            * character. Again, the wildcard is only used with the Name
            parameter.

    Returns:
        Results: A Results object which contains a list of tag
            dictionaries, one for each tag found during the browse. Use
            .getResults() on the results object to get the list of tag
            dictionaries, or .getReturnedSize() to the the number of
            items in results. Refer to the list of tagBrowse objects.
    """
    print(path, filter)
    return Results()


def browseHistoricalTags(
    path, nameFilters=None, maxSize=None, continuationPoint=None
):
    """Will browse for any historical Tags at the provided historical
    path.

    It will only browse for Tags at the path, and will not go down
    through any children. Will return with a BrowseResults object.

    Args:
        path (str): The Historical Tag Path to browse. See the Tag
            Export page for a description of how to construct a
            historical Tag Path.
        nameFilters (list[str]): A list of name filters to be applied to
            the result set. Optional.
        maxSize (int): The maximum size of the result set. Optional.
        continuationPoint (object): Sets the continuation point in order
            to continue a browse that was previously started and then
            limited. Use .getContinuationPoint() on the BrowseResults
            object to get the continuation point. Optional.

    Returns:
        Results: A Results object which contains a list of Tag
            dictionaries, one for each Tag found during the browse.
    """
    print(path, nameFilters, maxSize, continuationPoint)
    return Results()


def browseTags(
    parentPath,
    tagPath=None,
    tagType=None,
    dataType=None,
    udtParentType=None,
    recursive=False,
    sort="ASC",
):
    """Returns an array of tags from a specific folder.

    The function supports filtering and recursion. Leave filters blank
    to return all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        tagPath (str): Filters on a tag path. Use * as a wildcard for
            any number of characters and a ? for a single character.
            Optional.
        tagType (str): Filters on a tag type. Possible values are OPC,
            MEMORY, DB, QUERY, Folder, DERIVED and UDT_INST. Optional.
        dataType (str): The data type of the tag. Not used for UDT
            instances or folders. Possible values are Int1, Int2, Int4,
            Int8, Float4, Float8, Boolean, String, and DateTime.
            Optional.
        udtParentType (str): The name of the parent UDT. Optional.
        recursive (bool): Recursively search for tags inside of folders.
            Note: It is highly recommended that recursive is set to
            False, as server timeouts are more likely to occur.
            Optional.
        sort (str): Sets the sort order, possible values are ASC and
            DESC. Sorting is done on the full path of the tag. Optional.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the
            following variables: name, path, fullPath, type, dataType,
            and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    warnings.warn(
        "browseTags is deprecated, use browse instead.", DeprecationWarning
    )
    print(
        parentPath,
        tagPath,
        tagType,
        dataType,
        udtParentType,
        recursive,
        sort,
    )
    return [BrowseTag()]


def browseTagsSimple(parentPath, sort):
    """Returns a sorted array of tags from a specific folder.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        sort (str): Sets the sort order, possible values are ASC and
            DESC.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the
            following variables: name, path, fullPath, type, dataType,
            and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    warnings.warn(
        "browseTagsSimple is deprecated, use browse instead.",
        DeprecationWarning,
    )
    print(parentPath, sort)
    return [BrowseTag()]


def configure(basePath, tags, collisionPolicy="o"):
    """Creates Tags from a given list of Python dictionaries or from a
    JSON source string.

    Can be used to overwrite a current Tag's configuration.

    When utilizing this function, the tag definitions must specify the
    names of properties with their scripting/JSON name. A reference of
    these properties can be found on the Tag Properties and Tag Alarm
    Properties pages.

    Args:
        basePath (str): The starting point where the new Tags will be
            created. When making changes to existing tags with this
            function, you want to set the path to the parent folder of
            the exiting tag(s), not the tag(s) themselves.
        tags (list[object]): A list of Tag definitions, where each Tag
            definition is a Python dictionary. Alternately, a JSON
            source string may be passed to this parameter. When editing
            existing tags, it is generally easier to retrieve the tag
            configurations with system.tag.getConfiguration, modify the
            results of the getConfiguration call, and then write the new
            configuration to the parent folder of the existing tag(s).
        collisionPolicy (str): The action to take when a tag or folder
            with the same path and name is encountered. Possible values
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
        list[QualityCode]: A List of QualityCode objects, one for each
            tag in the list, that is representative of the result of the
            operation.
    """
    print(basePath, tags, collisionPolicy)
    return [QualityCode()]


def copy(tags, destination, collisionPolicy="o"):
    """Copies tags from one folder to another.

    Multiple tag and folder paths may be passed to a single call of this
    function. The new destination can be a separate tag provider.

    Args:
        tags (list[str]): A List of Tag paths to move.
        destination (str): The destination to copy the Tags to. All
            specified tags will be copied to the same destination. The
            destination tag provider must be specified.
        collisionPolicy (str): The action to take when a tag or folder
            with the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        list[QualityCode]: A List of QualityCode objects, one for each
            tag in the list, that is representative of the result of the
            operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode()]


def deleteAnnotations(paths, storageIds):
    """Removes stored annotations from the sqlth_annotations table.

    Requires the full tag path (including history provider) for each
    annotation, as well as each annotation's storage ID. Storage ID
    values can be retrieved with system.tag.queryAnnotations.

    Args:
        paths (list[str]): A list of tag paths with existing
            annotations. The paths are equivalent to what would be used
            for a tag history query, and should specify the source
            provider as well. For example,
            "[HistoryProvider/Gateway:Provider]Path/To/Tag".
        storageIds (list[int]): A sequence of storage identifiers for If
            defined, these will be used to perform updates, or deletes
            (if the corresponding delete parameter is True). Storage id
            is available on the Annotation object, and is returned as
            the result value from the storeAnnotations call.

    Returns:
        list[QualifiedValue]: A list of qualified values. The quality
            code will indicate success or failure, and if successful,
            the storage id of the annotation will have been deleted.
    """
    print(paths, storageIds)


def deleteTags(tagPaths):
    """Deletes multiple Tags or Tag Folders.

    When deleting a Tag Folder, all Tags under the folder are also
    deleted.

    Args:
        tagPaths (list[str]): A List of the paths to the Tags or Tag
            Folders that are to be removed.

    Returns:
         list[QualityCode]: A List of QualityCode objects, one for each
            tag in the list, that is representative of the result of the
            operation, e.g. "Good", "Bad_NotFound", etc. The quality
            codes have a built-in isNotGood() method that can be used to
            determine if any deletions failed.
    """
    print(tagPaths)


def exists(tagPath):
    """Checks whether or not a tag with a given path exists.

    Args:
        tagPath (str): The path of the tag to look up.

    Returns:
        bool: True if a tag exists for the given path, False otherwise.
    """
    print(tagPath)
    return True


def exportTags(filePath, tagPaths, recursive=True, exportType="json"):
    """Exports Tags to a file on a local file system.

    The term "local file system" refers to the scope in which the script
    was running; for example, running this script in a Gateway Timer
    script will export the file to the Gateway file system.

    Args:
        filePath (str): The file path that the Tags will be exported to.
            If the file does not already exist, this function will
            attempt to create it.
        tagPaths (list[str]): A List of Tag paths to export. All Tag
            paths in the list must be from the same parent folder.
        recursive (bool): Set to True to export all Tags under each Tag
            path, including Tags in child folders. Defaults to True.
            Optional.
        exportType (str): The type of file that will be exported. Set to
            "json" or "xml". Defaults to "json". Optional.
    """
    print(filePath, tagPaths, recursive, exportType)


def getConfiguration(basePath, recursive=False):
    """Retrieves Tags from the Gateway as Python dictionaries.

    These can be edited and then saved back using system.tag.configure.

    Args:
        basePath (str): The starting point where the Tags will be
            retrieved. This can be a folder containing, and if recursive
            is True, then the function will attempt to retrieve all of
            the tags in the folder.
        recursive (bool): If True, the entire Tag Tree under the
            specified path will be retrieved. Note that this will only
            check one level under the base path. True recursion would
            require multiple uses of this function at different paths.
            Optional.

    Returns:
         dict: A List of Tag dictionaries. Nested Tags are placed in a
            list marked as "tags" in the dictionary.
    """
    print(basePath, recursive)


def importTags(filePath, basePath, collisionPolicy="o"):
    """Imports a JSON tag file at the provided path.

    Also supports XML and CSV Tag file exports from legacy systems.

    Args:
        filePath (str): The file path of the Tag export to import.
        basePath (str): The Tag path that will serve as the root node
            for the imported Tags.
        collisionPolicy (str): The action to take when a tag or folder
            with the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        list[QualityCode]: A List of QualityCode objects, one for each
            tag in the list, that is representative of the result of the
            operation.
    """
    print(filePath, basePath, collisionPolicy)
    return [QualityCode()]


def isOverlaysEnabled():
    """Returns whether or not the current client's quality overlay
    system is currently enabled.

    Returns:
         bool: True (1) if overlays are currently enabled.
    """
    return False


def move(tags, destination, collisionPolicy="o"):
    """Moves Tags or Folders to a new destination.

    The new destination can be a separate tag provider. If interested in
    copying the tags to a new destination, instead of moving them,
    please see the system.tag.copy page.

    Args:
        tags (list[str]): A List of Tag paths to move.
        destination (str): The destination to move the Tags to. The
            destination tag provider must be specified: i.e.,
            [default]Folder/myTag
        collisionPolicy (str): The action to take when a tag or folder
            with the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        list[QualityCode]: A List of QualityCode objects, one for each
            tag in the list, that is representative of the result of the
            operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode()]


def queryAnnotations(paths, startTime=None, endTime=None, types=None):
    """Queries user stored annotations from the tag history system for a
    set of paths, for a given time range.

    Args:
        paths (list[str]): A list of tag paths to query. The paths are
            equivalent to what would be used ofr a tag history query,
            and should specify the source provider as well. For example,
            "[HistoryProvider/Gateway:Provider]Path/To/Tag".
        startTime (Date): The start of the time range. If not defined,
            defaults to 12 hours ago. Optional.
        endTime (Date): The end of time range. If not defined, defaults
            to "now". Optional.
        types (list[object]): A list of string "types" to filter on.
            Types are defined by the annotations and various subsystems,
            and may vary with different providers. Possible annotation
            types are listed on the system.tag.storeAnnotations page.
             Optional.

    Returns:
        list[object]: A list of Annotation objects that match the query
            criteria.
    """
    print(paths, startTime, endTime, types)


def queryTagCalculations(
    paths,
    calculations,
    startDate=None,
    endDate=None,
    rangeHours=None,
    rangeMinutes=None,
    aliases=None,
    includeBoundingValues=True,
    validatesSCExec=True,
    noInterpolation=False,
    ignoreBadQuality=False,
):
    """Queries various calculations (aggregations) for a set of tags
    over a specified range.

    Returns a dataset with a row per tag, and a column per calculation.

    This is useful when you wish to aggregate tag history collected over
    a period of time into a single value per aggregate. If you want
    multiple values aggregated to a single time slice (i.e., hourly
    aggregates for the same tag over an 8 hour period) consider using
    system.tag.queryTagHistory

    Args:
        paths (list[str]): An array of tag paths (strings) to query
            calculations for. The resulting dataset will have a row for
            each tag, and a column for each calculation.
        calculations (list[str]): An array of calculations (aggregation
            functions) to execute for each tag. Valid values are:
            "Average" (time-weighted), "MinMax", "LastValue",
            "SimpleAverage", "Sum", "Minimum", "Maximum", "DurationOn",
            "DurationOff", "CountOn", "CountOff", "Count", "Range",
            "Variance", "StdDev", "PctGood", and "PctBad".
        startDate (Date): The starting point for the calculation
            window. If omitted, and range is not used, 8 hours before
            the current time is used. Optional.
        endDate (Date): The end of the calculation window. If
            omitted, and range is not used, uses the current time.
            Optional.
        rangeHours (int): Allows you to specify the query range in
            hours, instead of using start and end date. Can be positive
            or negative, and can be used in conjunction with startDate
            or endDate. Optional.
        rangeMinutes (int): Same as rangeHours, but in minutes.
            Optional.
        aliases (list[str]): Aliases that will be used to override the
            tag path names in the result dataset. Must be 1-to-1 with
            the tag paths. If not specified, the tag paths themselves
            will be used. Optional.
        includeBoundingValues (bool): A boolean flag indicating that the
            system should attempt to load values before and after the
            query bounds for the purpose of interpolation. The effect
            depends on the aggregates used. The default is "True".
            Optional.
        validatesSCExec (bool): A boolean flag indicating whether or not
            data should be validated against the scan class execution
            records. If False, calculations may include data that is
            assumed to be good, even though the system may not have been
            running. Default is "True". Optional.
        noInterpolation (bool): A boolean flag indicating that the
            system should not attempt to interpolate values in
            situations where it normally would, such as for analog tags.
            Default is "False". Optional.
        ignoreBadQuality (bool): A boolean flag indicating that bad
            quality values should not be used in the query process. If
            set, any value with a "bad" quality will be completely
            ignored in calculations. Default is "False". Optional.

    Returns:
        BasicDataset: A dataset representing the calculations over the
            specified range.
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
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
    """Queries the Tag history system for information about the density
    of data.

    In other words, how much data is available for a given time span.

    This function is called with a list of Tag paths, and a start and
    end date. The result set is a two column dataset specifying the
    timestamp, and a relative weight. Each row is valid from the given
    time until the next row. Tags are assigned a 1 or a 0 if they are
    present or not. All values are then multiplied together to get a
    decimal based percentage for the density. Thus, for four Tag paths
    passed in, if three Tags were present during the span, the result
    would be 0.75.

    Args:
        paths (list[str]): An array of Tag paths (strings) to query.
        startDate (Date): The start of the range to query.
        endDate (Date): The end of the range to query.

    Returns:
        BasicDataset: A 2-column dataset consisting of a timestamp and a
            weight. Each row is valid until the next row.
    """
    print(paths, startDate, endDate)
    return BasicDataset()


def queryTagHistory(
    paths,
    startDate=None,
    endDate=None,
    returnSize=-1,
    aggregationMode="Average",
    returnFormat="Wide",
    columnNames=None,
    intervalHours=None,
    intervalMinutes=None,
    rangeHours=None,
    rangeMinutes=None,
    aggregationModes=None,
    includeBoundingValues=None,
    validateSCExec=None,
    noInterpolation=None,
    ignoreBadQuality=None,
    timeout=None,
    intervalSeconds=None,
    rangeSeconds=None,
):
    """Issues a query to the Tag Historian.

    Querying tag history involves specifying the tags and the date
    range, as well as a few optional parameters. The Tag historian will
    find the relevant history and then interpolate and aggregate it
    together into a coherent, tabular result set.

    Args:
        paths (list[str]): An array of tag paths (strings) to query.
            Each tag path specified will be a column in the result
            dataset.
        startDate (Date): The earliest value to retrieve. If
            omitted, 8 hours before current time is used. Optional.
        endDate (Date): The latest value to retrieve. If omitted,
            current time is used. Optional.
        returnSize (int): The number of samples to return. -1 will
            return values as they changed, and 0 will return the
            "natural" number of values based on the logging rates of the
            scan class(es) involved. -1 is the default. Optional.
        aggregationMode (str): The mode to use when aggregating multiple
            samples into one time slice. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad". Optional.
        returnFormat (str): Use "Wide" to have a column per tag queried,
            or "Tall" to have a fixed-column format. Default is "Wide".
            Optional.
        columnNames (list[str]): Aliases that will be used to override
            the column names in the result dataset. Must be 1-to-1 with
            the tag paths. If not specified, the tag paths themselves
            will be used as column titles. Optional.
        intervalHours (int): Allows you to specify the window interval
            in terms of hours, as opposed to using a specific return
            size. Optional.
        intervalMinutes (int): Same as intervalHours, but in minutes.
            Can be used on its own, or in conjunction with
            intervalHours. Optional.
        rangeHours (int): Allows you to specify the query range in
            hours, instead of using start and end date. Can be positive
            or negative, and can be used in conjunction with startDate
            or endDate. Optional.
        rangeMinutes (int): Same as rangeHours, but in minutes.
            Optional.
        aggregationModes (list[str]): A one-to-one list with paths
            specifying an aggregation mode per column. Optional.
        includeBoundingValues (bool): A boolean flag indicating that the
            system should attempt to include values for the query bound
            times if possible. The default for this property depends on
            the query mode, so unless a specific behavior is desired, it
            is best to not include this parameter. Optional.
        validateSCExec (bool): A boolean flag indicating whether or not
            data should be validated against the scan class execution
            records. If False, data will appear flat (but good quality)
            for periods of time in which the system wasn't running. If
            True, the same data would be bad quality during downtime
            periods. Optional.
        noInterpolation (bool): A boolean flag indicating that the
            system should not attempt to interpolate values in
            situations where it normally would. This will also prevent
            the return of rows that are purely interpolated. Optional.
        ignoreBadQuality (bool): A boolean flag indicating that bad
            quality values should not be used in the query process. If
            set, any value with a "bad" quality will be completely
            ignored in calculations and in the result set. Optional.
        timeout (int): Timeout in milliseconds for Client Scope. This
            property is ignored in the Gateway Scope. Optional.
        intervalSeconds (int): Same as intervalHours and interval
            Minutes, but in seconds. Can be used on its own, or in
            conjunction with intervalHours and intervalMinutes.
            Optional.
        rangeSeconds (int): Allows you to specify the query range in
            seconds, instead of using start and end date. Can be
            positive or negative, and can be used in conjunction with
            startDate or endDate. Optional.

    Returns:
        BasicDataset: A dataset representing the historian values for
            the specified tag paths. The first column will be the
            timestamp, and each column after that represents a tag.
    """
    endDate = system.date.now() if endDate is None else endDate
    startDate = (
        system.date.addHours(endDate, -8) if startDate is None else startDate
    )
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


def read(tagPath):
    """Reads the value of the tag at the given tag path.

    Returns a qualified value object. You can read the value, quality,
    and timestamp from this object. If the tag path does not specify a
    tag property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the
    attribute to the tagPath parameter. See the Tag Attributes page for
    a list of available attributes.

    Args:
        tagPath (str): Reads from the given tag path. If no property is
            specified in the path, the Value property is assumed.

    Returns:
        BasicQualifiedValue: A qualified value. This object has three
            sub-members: value, quality, and timestamp.
    """
    warnings.warn(
        "read is deprecated, use readAsync or readBlocking instead.",
        DeprecationWarning,
    )
    print(tagPath)
    return BasicQualifiedValue()


def readAll(tagPaths):
    """Reads the values of each tag in the tag path list.

    Returns a sequence of qualified value objects. You can read the
    value, quality, and timestamp from each object in the return
    sequence. Reading in bulk like this is more efficient than calling
    read() many times.

    Args:
        tagPaths (list[str]): A sequence of tag paths to read from.

    Returns:
        list[QualifiedValue]: A sequence of qualified values
            corresponding to each tag path given. Each qualified value
            will have three sub-members: value, quality, and timestamp.
    """
    warnings.warn(
        "readAll is deprecated, use readAsync or readBlocking instead.",
        DeprecationWarning,
    )
    print(tagPaths)
    return [BasicQualifiedValue() for _ in range(len(tagPaths))]


def readAsync(tagPaths, callback):
    """Asynchronously reads the value of the Tags at the given paths.

    You must provide a python callback function that can process the
    read results.

    Args:
        tagPaths (list[str]): A List of Tag paths to read from. If no
            property is specified in the path, the Value property is
            assumed.
        callback (object): A Python callback function to process the
            read results. The function definition must provide a single
            argument, which will hold a List of qualified values when
            the callback function is invoked. The qualified values will
            have three sub members: value, quality, and timestamp.
    """
    print(tagPaths, callback)


def readBlocking(tagPaths, timeout=45000):
    """Reads the value of the Tags at the given paths.

    Will block until the read operation is complete or times out.

    Args:
        tagPaths (list[str]): A List of Tag paths to read from. If no
            property is specified in a path, the Value property is
            assumed.
        timeout (int): How long to wait in milliseconds before the read
            operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified. Optional.

    Returns:
        list[BasicQualifiedValue]: A list of QualifiedValue objects
            corresponding to the Tag paths. Each qualified value will
            have three sub members: value, quality, and timestamp.
    """
    print(tagPaths, timeout)
    return [BasicQualifiedValue() for _ in tagPaths]


def rename(tag, newName, collisionPollicy="a"):
    """Renames a single tag or a folder.

    Args:
        tag (str): The tag path to rename.
        newName (str): The new name.
        collisionPollicy (str): The action to take when a tag or folder
            with the same path and names is encountered. Possible values
            include "a" (Abort, throws an exception), "o" (Overwrite,
            completely replaces a tag's configuration), and "i"
            (Ignore). Defaults to Abort if not specified.

    Returns:
        object: A quality code that contains the result of the rename
            operation.
    """
    print(tag, newName, collisionPollicy)


def requestGroupExecution(provider, tagGroup):
    """Sends a request to the specified Tag Group to execute now.

    Args:
        provider (str): Name of the Tag Provider that the Tag Group is
            in.
        tagGroup (str): The name of the Tag Group to execute.
    """
    print(provider, tagGroup)


def setOverlaysEnabled(enabled):
    """Enables or disables the component quality overlay system.

    Args:
        enabled (bool): True (1) to turn on tag overlays, False (0) to
            turn them off.
    """
    print(enabled)


def storeAnnotations(
    paths,
    startTimes=None,
    endTimes=None,
    types=None,
    data=None,
    storageIds=None,
    deleted=None,
):
    """Stores annotations into the tag history system.

    Annotations are stored by the underlying historian implementations,
    so different providers may store in different ways, and some
    providers may not support annotation storage. All parameters are
    1-to-1, so all provided lists should be of the same length. If a
    particular annotation doesn't need a parameter, that element can be
    None in the list.

    Args:
        paths (list[str]): A list of tag paths to store for. The paths
            are equivalent to what would be used for a tag history
            query, and should specify the source provider as well. For
            example, "[HistoryProvider/Gateway:Provider]Path/To/Tag".
            This parameter is required, even if storage ids are
            included, because it is used to identify the underlying
            storage provider.
        startTimes (list[Date]): The start times of the events. If
            omitted, defaults to the current time. Optional.
        endTimes (list[Date]): The end times of the event, if
            applicable. If omitted, does not store an end time for the
            annotation. Optional.
        types (list[str]): The type id for the annotation. If not
            defined, "marker" will be used. See the Annotation Types for
            more details. Optional.
        data (list[str]): Data for the annotation, such as text
            describing the meaning of the annotation. Optional.
        storageIds (list[int]): If defined, the function will instead
            update the existing annotation instead of adding new ones,
            overriding existing values for the annotation with those
            provided by this function (if the corresponding delete
            parameter is True). Storage id is available on the
            Annotation object, and is returned as the result value from
            the storeAnnotations call. Optional.
        deleted (list[bool]): A list of booleans indicating that the
            individual annotation should be deleted. Requires storage id
            to be set as well. Optional.

    Returns:
        list[QualifiedValue]: A list of qualified values. The quality
            code will indicate success or failure, and if successful,
            the storage id of the annotation will be returned in the
            value. Since annotations are stored by individual providers,
            there is no guarantee as to the type or format of the
            storage id. However, it can be held and re-used in order to
            update or delete.
    """
    print(paths, startTimes, endTimes, types, data, storageIds, deleted)


def storeTagHistory(
    historyprovider,
    tagprovider,
    paths,
    values,
    qualities=None,
    timestamps=None,
):
    """Inserts data into the tag history system, allowing Tag history to
    be recorded via scripting.

    The Tag paths are associated with a historical and realtime
    provider, but they do not necessarily need to exist in the realtime
    provider. This means records from non-existent (virtual) Tags can be
    stored in the Tag History system. Because of this, it is imperative
    that Tag paths passed to the function are typed precisely, otherwise
    the history will be stored at an incorrect path.

    Note that the Tag History system does cache tag data. Thus, if this
    function is called, the tag path and tag id are cached until the
    history provider or gateway are restarted. This means manually
    removing the tag from the sqlth_te table, and then calling this
    function again with the same path will not re-populate the tag
    execution table (especially so when working purely with virtual tag
    paths). Instead, the cache must first be cleared, and then a new
    entry will be added the next time this function is called.

    Args:
        historyprovider (str): The historical provider to store to.
        tagprovider (str): The name of the realtime tag provider to
            associate these tags with. The tag provider does not need to
            exist, and the tag paths do not need to exist in it.
        paths (list[str]): A list of paths to store. The values,
            qualities, and timestamps are one-to-one with the paths. A
            single path may be present multiple times in order to store
            multiple values.
        values (list[object]): A list of values to store.
        qualities (list[int]): A list of integer quality codes
            corresponding to the values. Quality codes can be found on
            the Tag Quality and Overlays page. If omitted, GOOD quality
            will be used. Optional.
        timestamps (list[Date]): A list of Date timestamps corresponding
            to the values. If omitted, the current time will be used. A
            java.util.date object may be passed, so the system.date
            functions can be used to return a timestamp. Optional.
    """
    print(historyprovider, tagprovider, paths, values, qualities, timestamps)


def write(tagPath, value, suppressErrors=False):
    """Writes a value to a tag.

    Note that this function writes asynchronously. This means that the
    function does not wait for the write to occur before returning - the
    write occurs sometime later on a different thread.

    Args:
        tagPath (str): The path of the tag to write to.
        value (object): The value to write.
        suppressErrors (bool): A flag indicating whether or not to
            suppress errors. Optional.

    Returns:
        int: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    warnings.warn(
        "write is deprecated, use writeAsync or writeBlocking instead.",
        DeprecationWarning,
    )
    print(tagPath, value, suppressErrors)
    return 1


def writeAll(tagPaths, values):
    """Performs an asynchronous bulk write.

    Takes two sequences that must have the same number of entries. The
    first is the list of tag paths to write to, and the second is a list
    of values to write. This function is dramatically more efficient
    than calling write multiple times.

    Args:
        tagPaths (list[str]): The paths of the tags to write to.
        values (list[object]): The values to write.

    Returns:
        list[int]: Array of ints with an element for each tag written
            to: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    warnings.warn(
        "writeAll is deprecated, use writeAsync or writeBlocking instead.",
        DeprecationWarning,
    )
    print(tagPaths, values)
    return [1] * len(tagPaths)


def writeAsync(tagPaths, values, callback=None):
    """Asynchronously writes values to Tags a the given paths.

    You must provide a Python callback function that can process the
    write results.

    Args:
        tagPaths (list[str]): A List of Tag paths to write to. If no
            property is specified in a Tag path, the Value property is
            assumed.
        values (list[object]): The values to write to the specified
            paths.
        callback (object): A Python callback function to process the
            write results. The function definition must provide a single
            single argument, which will hold a List of quality codes
            when the callback function is invoked. The quality codes
            will hold the result of the write operation for that Tag.
            Optional.
    """
    print(tagPaths, values, callback)


def writeBlocking(tagPaths, values, timeout=45000):
    """Writes values to Tags at the given paths.

    This function will block until the write operation is complete or
    times out.

    Args:
        tagPaths (list[str]): A List of Tag paths to write to. If no
            property is specified in a Tag path, the Value property is
            assumed.
        values (list[object]): The values to write to the specified
            paths.
        timeout (int): How long to wait in milliseconds before the write
            operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified.

    Returns:
        list[QualityCode]: A List of QualityCode objects, one for each
            Tag path. Each quality code holds the result of the write
            operation for that Tag.
    """
    print(tagPaths, values, timeout)
    return [QualityCode()]
