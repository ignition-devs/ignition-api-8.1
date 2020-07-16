# Copyright (C) 2019
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Tag Functions
The following functions give you access to interact with Ignition
Tags."""

__all__ = [
    'browse',
    'browseTags',
    'browseTagsSimple',
    'queryTagCalculations',
    'read',
    'readAll',
    'readAsync',
    'readBlocking',
    'write',
    'writeAll'
]

import warnings

import system.date
from java.lang import Object


# noinspection PyMethodMayBeStatic
class BrowseTag(object):
    """BrowseTag class."""

    def __init__(self,
                 name=None,
                 path=None,
                 type_=None,
                 dataType=None):
        """BrowseTag initializer.

        Args:
            name (str): The name of the tag.
            path (str): The path of the tag.
            type_ (object): The type of the tag.
            dataType (object): The data type of the tag.
        """
        self.name = name
        self.path = path
        self.type = type_
        self.dataType = dataType

    def isDB(self):
        return True

    def isExpression(self):
        return True

    def isFolder(self):
        return True

    def isMemory(self):
        return True

    def isOPC(self):
        return True

    def isQuery(self):
        return True

    def isUDT(self):
        return True


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it."""

    def __init__(self,
                 value=None,
                 quality=None,
                 timestamp=None):
        self.value = value
        self.quality = quality
        self.timestamp = timestamp

    def derive(self, diagnosticMessage):
        pass

    def equals(self, value, includeTimestamp):
        pass

    def getQuality(self):
        pass

    def getTimestamp(self):
        pass

    def getValue(self):
        pass


# noinspection PyMethodMayBeStatic
class QualityCode(Object):
    """QualityCode contains a 32-bit integer code and optionally a
    diagnostic string."""

    def getCode(self):
        pass

    def getCodeName(self, arg):
        pass

    def getCodesJson(self):
        pass

    def getDiagnosticMessage(self):
        pass

    def getLevel(self, arg):
        pass

    def getName(self):
        pass

    def getQualityFor(self, arg):
        pass

    def isBad(self):
        return False

    def isBadOrError(self):
        return False

    def isError(self):
        return False

    def isGood(self):
        return True

    def isNot(self, arg):
        return True

    def isNotGood(self):
        return False

    def isUncertain(self):
        return False

    def toString(self):
        return ''

    def toValue(self):
        pass

    @staticmethod
    def values(self):
        pass

    @staticmethod
    def worstOf(a, b):
        pass

    @staticmethod
    def worstOfAll(*args):
        pass


class Results(object):
    """The results of a browse operation. May only represent a partial
    result set, which can be determined by comparing the Total
    Available Size to the Returned Size. If there is a mismatch, the
    continuation point should be non-null and can be used in
    constructing the subsequent BrowseFilter to continue the browse."""

    def error(self, result):
        pass

    def getContinuationPoint(self):
        pass

    def getResultQuality(self):
        pass

    def getResults(self):
        pass

    def getReturnedSize(self):
        pass

    def getTotalAvailableSize(self):
        pass

    def of(self, arg):
        pass

    def setContinuationPoint(self, continuationPoint):
        pass

    def setResultQuality(self, value):
        pass

    def setResults(self, results):
        pass

    def setTotalAvailableResults(self, totalAvailableResults):
        pass

    def toString(self):
        pass


def browse(path, filter=None):
    """Returns a list of tags found at the specified tag path. The
    list objects are returned as dictionaries with some basic
    information about each tag.

    Args:
        path (str): The path that will be browsed, typically to a
            folder or UDT instance.
        filter (dict): A dictionary of browse filter parameters.
            Parameters include name (with wildcards), dataType,
            valueSource, tagType, typeId, quality (specify Good or
            Bad), and maxResults.
            The aforementioned wildcard character is the * character.
            Again, the wildcard is only used with the Name parameter.

    Returns:
        Results: A Results object which contains a list of tag
            dictionaries, one for each tag found during the browse.
            Use .getResults() on the results object to get the list of
            tag dictionaries, or .getReturnedSize() to the the number
            of items in results. Refer to the list of tagBrowse
            objects.
    """
    print path, filter
    return Results()


def browseTags(parentPath, tagPath=None, tagType=None, dataType=None,
               udtParentType=None, recursive=False, sort='ASC'):
    """Returns an array of tags from a specific folder. The function
    supports filtering and recursion. Leave filters blank to return
    all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name
            in square brackets at the beginning of the parentPath
            string.
            Example: "[myTagProvider]MyTagsFolder". If the tag
            provider name is left off then the project default
            provider will be used.
        tagPath (str): Filters on a tag path. Use * as a wildcard for
            any number of characters and a ? for a single character.
            Optional.
        tagType (str): Filters on a tag type. Possible values are OPC,
            MEMORY, DB, QUERY, Folder, DERIVED and UDT_INST. Optional.
        dataType (str): The data type of the tag. Not used for UDT
            instances or folders. Possible values are Int1, Int2,
            Int4, Int8, Float4, Float8, Boolean, String, and DateTime.
            Optional.
        udtParentType (str): The name of the parent UDT.
        recursive (bool): Recursively search for tags inside of
            folders. Note: It is highly recommended that recursive is
            set to false, as server timeouts are more likely to occur.
            Optional.
        sort (str): Sets the sort order, possible values are ASC and
            DESC. Sorting is done on the full path of the tag.
            Optional.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the
            following variables: name, path, fullPath, type, dataType,
            and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    warnings.warn(
        "browseTags is deprecated, use browse instead.",
        DeprecationWarning
    )
    print(parentPath, tagPath, tagType, dataType,
          udtParentType, recursive, sort)
    return [BrowseTag()]


def browseTagsSimple(parentPath, sort):
    """Returns a sorted array of tags from a specific folder.

    Args:
        parentPath (str): The parent folder path. Leave blank for the
            root folder. Note: you can specify the tag provider name
            in square brackets at the beginning of the parentPath
            string.
            Example: "[myTagProvider]MyTagsFolder". If the tag
            provider name is left off then the project default
            provider will be used.
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
        DeprecationWarning
    )
    print(parentPath, sort)
    return [BrowseTag()]


def queryTagCalculations(paths, calculations,
                         startDate=system.date.addHours(system.date.now(), -8),
                         endDate=system.date.now(), rangeHours=None,
                         rangeMinutes=None, aliases=None,
                         includeBoundingValues=True, validatesSCExec=True,
                         noInterpolation=False, ignoreBadQuality=False):
    """Queries various calculations (aggregations) for a set of tags
    over a specified range. Returns a dataset with a row per tag, and
    a column per calculation.

    This is useful when you wish to aggregate tag history collected
    over a period of time into a single value per aggregate. If you
    want multiple values aggregated to a single time slice (i.e.,
    hourly aggregates for the same tag over an 8 hour period) consider
    using system.tag.queryTagHistory

    Args:
        paths: An array of tag paths (strings) to query calculations
            for. The resulting dataset will have a row for each tag,
            and a column for each calculation.
        calculations: An array of calculations (aggregation functions)
            to execute for each tag. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad".
        startDate: The starting point for the calculation window. If
            omitted, and range is not used, 8 hours before the current
            time is used.
        endDate: The end of the calculation window. If omitted, and
            range is not used, uses the current time.
        rangeHours: Allows you to specify the query range in hours,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate.
        rangeMinutes: Same as rangeHours, but in minutes.
        aliases: Aliases that will be used to override the tag path
            names in the result dataset. Must be 1-to-1 with the tag
            paths. If not specified, the tag paths themselves will be
            used.
        includeBoundingValues: A boolean flag indicating that the
            system should attempt to load values before and after the
            query bounds for the purpose of interpolation. The effect
            depends on the aggregates used. The default is "true".
        validatesSCExec: A boolean flag indicating whether or not data
            should be validated against the scan class execution
            records. If false, calculations may include data that is
            assumed to be good, even though the system may not have
            been running. Default is "true".
        noInterpolation: A boolean flag indicating that the system
            should not attempt to interpolate values in situations
            where it normally would, such as for analog tags. Default
            is "false".
        ignoreBadQuality: A boolean flag indicating that bad quality
            values should not be used in the query process. If set,
            any value with a "bad" quality will be completely ignored
            in calculations. Default is "false".

    Returns:
        Dataset: A dataset representing the calculations over the
            specified range.
    """
    print (paths, calculations, startDate, endDate, rangeHours,
           rangeMinutes, aliases, includeBoundingValues,
           validatesSCExec, noInterpolation, ignoreBadQuality)


def read(tagPath):
    """Reads the value of the tag at the given tag path. Returns a
    qualified value object. You can read the value, quality, and
    timestamp  from this object. If the tag path does not specify a
    tag property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the
    attribute to the tagPath parameter. See the Tag Attributes page
    for a list of available attributes.

    Args:
        tagPath (str): Reads from the given tag path. If no property
            is specified in the path, the Value property is assumed.

    Returns:
        QualifiedValue: A qualified value. This object has three
            sub-members: value, quality, and timestamp.
    """
    warnings.warn(
        "read is deprecated, use readAsync or readBlocking instead.",
        DeprecationWarning
    )
    print tagPath
    return QualifiedValue()


def readAll(tagPaths):
    """Reads the values of each tag in the tag path list. Returns a
    sequence of qualified value objects. You can read the value,
    quality, and timestamp from each object in the return sequence.
    Reading in bulk like this is more efficient than calling read()
    many times.

    Args:
        tagPaths (list[str]): A sequence of tag paths to read from.

    Returns:
        list[QualifiedValue]: A sequence of qualified values
            corresponding to each tag path given. Each qualified value
            will have three sub-members: value, quality, and
            timestamp.
    """
    warnings.warn(
        "readAll is deprecated, use readAsync or readBlocking instead.",
        DeprecationWarning
    )
    print tagPaths
    items = []
    for i in range(len(tagPaths)):
        items.append(QualifiedValue())
    return items


def readAsync(tagPaths, callback):
    """Asynchronously reads the value of the Tags at the given paths.
    You must provide a python callback function that can process the
    read results.

    Args:
        tagPaths (list[str]): A List of Tag paths to read from. If no
            property is specified in the path, the Value property is
            assumed.
        callback (object): A Python callback function to process the
            read results. The function definition must provide a
            single argument, which will hold a List of qualified
            values when the callback function is invoked. The
            qualified values will have three sub members: value,
            quality, and timestamp.
    """
    print tagPaths, callback
    pass


def readBlocking(tagPaths, timeout=45000):
    """Reads the value of the Tags at the given paths. Will block
    until the read operation is complete or times out.

    Args:
        tagPaths (list[str]): A List of Tag paths to read from. If no
            property is specified in a path, the Value property is
            assumed.
        timeout (int): How long to wait in milliseconds before the
            read operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified. Optional.

    Returns:
        list[QualifiedValue]: A list of QualifiedValue objects
            corresponding to the Tag paths. Each qualified value will
            have three sub members: value, quality, and timestamp.
    """
    print tagPaths, timeout
    items = []
    for i in range(len(tagPaths)):
        items.append(QualifiedValue())
    return items


def write(tagPath, value, suppressErrors=False):
    """Writes a value to a tag. Note that this function writes
    asynchronously. This means that the function does not wait for the
    write to occur before returning - the write occurs sometime later
    on a different thread.

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
        DeprecationWarning
    )
    print tagPath, value, suppressErrors
    return 1


def writeAll(tagPaths, values):
    """Performs an asynchronous bulk write. Takes two sequences that
    must have the same number of entries. The first is the list of tag
    paths to write to, and the second is a list of values to write.
    This function is dramatically more efficient than calling write
    multiple times.

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
        DeprecationWarning
    )
    print tagPaths, values
    return [1] * len(tagPaths)


def writeAsync(tagPaths, values, callback):
    """Asynchronously writes values to Tags a the given paths. You
    must provide a Python callback function that can process the write
    results.

    Args:
        tagPaths (list[str]): A List of Tag paths to write to. If no
            property is specified in a Tag path, the Value property is
            assumed.
        values (list[object]): The values to write to the specified
            paths.
        callback (object): A Python callback function to process the
            write results. The function definition must provide a
            single argument, which will hold a List of quality codes
            when the callback function is invoked. The quality codes
            will hold the result of the write operation for that Tag.
    """
    print tagPaths, values, callback
    pass


def writeBlocking(tagPaths, values, timeout=45000):
    """Asynchronously writes values to Tags a the given paths. You
    must provide a Python callback function that can process the write
    results.

    Args:
        tagPaths (list[str]): A List of Tag paths to write to. If no
            property is specified in a Tag path, the Value property is
            assumed.
        values (list[object]): The values to write to the specified
            paths.
        timeout  (int): How long to wait in milliseconds before the
            write operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified.

    Returns:
        list[QualityCode]: A List of QualityCode objects, one for each
            Tag path. Each quality code holds the result of the write
            operation for that Tag.
    """
    print tagPaths, values, timeout
    pass
