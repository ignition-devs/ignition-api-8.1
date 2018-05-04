# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,R0913

"""Tag Functions
The following functions give you access to interact with Ignition Tags."""

__all__ = [
    'browseTags',
    'read',
    'readAll',
    'write',
    'writeAll'
]


class BrowseTag(object):
    """BrowseTag class."""

    def __init__(self,
                 name=None,
                 path=None,
                 _type=None,
                 dataType=None):
        """BrowseTag initializer.

        Args:
            name (str): The name of the tag.
            path (str): The path of the tag.
            _type (object): The type of the tag.
            dataType (object): The data type of the tag.
        """
        self.name = name
        self.path = path
        self.type = _type
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
    """QualifiedValue class"""

    def __init__(self,
                 value=None,
                 quality=None,
                 timestamp=None):
        self.value = value
        self.quality = quality
        self.timestamp = timestamp


def browseTags(parentPath, tagPath=None, tagType=None, dataType=None, udtParentType=None,
               recursive=False, sort='ASC'):
    """Returns an array of tags from a specific folder. The function supports filtering and
    recursion. Leave filters blank to return all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath (str): The parent folder path. Leave blank for the root folder. Note: you can
            specify the tag provider name in square brackets at the beginning of the parentPath
            string. Example: "[myTagProvider]MyTagsFolder". If the tag provider name is left off
            then the project default provider will be used.
        tagPath (str): Filters on a tag path. Use * as a wildcard for any number of characters
            and a ? for a single character. Optional.
        tagType (str): Filters on a tag type. Possible values are OPC, MEMORY, DB, QUERY, Folder,
            DERIVED and UDT_INST. Optional.
        dataType (str): The data type of the tag. Not used for UDT instances or folders. Possible
            values are Int1, Int2, Int4, Int8, Float4, Float8, Boolean, String, and DateTime.
            Optional.
        udtParentType (str): The name of the parent UDT.
        recursive (bool): Recursively search for tags inside of folders. Note: It is highly
            recommended that recursive is set to false, as server timeouts are more likely to occur.
            Optional.
        sort (str): Sets the sort order, possible values are ASC and DESC. Sorting is done on the
            full path of the tag. Optional.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the following variables: name, path,
            fullPath, type, dataType, and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    print(parentPath, tagPath, tagType, dataType, udtParentType, recursive, sort)
    return [BrowseTag()]


def read(tagPath):
    """Reads the value of the tag at the given tag path. Returns a qualified value object. You can
    read the value, quality, and timestamp from this object. If the tag path does not specify a tag
    property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the attribute to the tagPath
    parameter. See the Tag Attributes page for a list of available attributes.

    Args:
        tagPath (str): Reads from the given tag path. If no property is specified in the path, the
            Value property is assumed.

    Returns:
        QualifiedValue: A qualified value. This object has three sub-members: value, quality, and
            timestamp.
    """
    print tagPath
    return QualifiedValue()


def readAll(tagPaths):
    """Reads the values of each tag in the tag path list. Returns a sequence of qualified value
    objects. You can read the value, quality, and timestamp from each  object in the return
    sequence. Reading in bulk like this is more efficient than calling read() many times.

    Args:
        tagPaths (list[str]): A sequence of tag paths to read from.

    Returns:
        list[QualifiedValue]: A sequence of qualified values corresponding to each tag path
        given. Each qualified value will have three sub-members: value, quality, and timestamp.
    """
    print(tagPaths)
    items = []
    for i in range(len(tagPaths)):
        items.append(QualifiedValue())
    return items


def write(tagPath, value, suppressErrors=False):
    """Writes a value to a tag. Note that this function writes asynchronously. This means that
    the function does not wait for the write to occur before returning - the write occurs
    sometime later on a different thread.

    Args:
        tagPath (str): The path of the tag to write to.
        value (object): The value to write.
        suppressErrors (bool): A flag indicating whether or not to suppress errors. Optional.

    Returns:
        int: 0 if the write failed immediately, 1 if it succeeded immediately, and 2 if it is
        pending.
    """
    print(tagPath, value, suppressErrors)
    return 1


def writeAll(tagPaths, values):
    """Performs an asynchronous bulk write. Takes two sequences that must have the same number of
    entries. The first is the list of tag paths to write to, and the second is a list of values
    to write.This function is dramatically more efficient than calling write multiple times.

    Args:
        tagPaths (list[str]): The paths of the tags to write to.
        values (list[object]): The values to write.

    Returns:
        list[int]: Array of ints with an element for each tag written to: 0 if the write failed
            immediately, 1 if it succeeded immediately, and 2 if it is pending.
    """
    print(tagPaths, values)
    return [1] * len(tagPaths)
