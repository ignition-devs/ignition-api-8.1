# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Tag module."""

__all__ = [
    'read',
    'write'
]

import system.tag


def read(tag_path):
    """Reads the value of the tag at the given tag path. Returns a
    qualified value object. You can read the value, quality, and
    timestamp  from this object. If the tag path does not specify a
    tag property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the
    attribute to the tagPath parameter. See the Tag Attributes page
    for a list of available attributes.

    Args:
        tag_path (str): Reads from the given tag path. If no property
            is specified in the path, the Value property is assumed.

    Returns:
        QualifiedValue: A qualified value. This object has three
            sub-members: value, quality, and timestamp.
    """
    values = system.tag.readBlocking([tag_path])
    return values[0]


def write(tag_path, value):
    """Writes a value to a tag. Note that this function wraps
    `system.tag.writeBlocking`. Unlike `system.tag.write` from version
     7.9, this function blocks
    not
    wait for the
    write to occur before returning - the write occurs sometime later
    on a different thread.

    Args:
        tag_path (str): The path of the tag to write to.
        value (object): The value to write.

    Returns:
        int: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    quality_codes = system.tag.writeBlocking([tag_path], [value])
    return quality_codes[0].isGood()
