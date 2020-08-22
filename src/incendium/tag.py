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
    """Reads the value of the Tags at the given paths. Will block
    until the read operation is complete or times out.

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
    """Writes a value to a tag. Note that this function will
    block until the write operation is complete or times out.

    Args:
        tag_path (str): The path of the tag to write to.
        value (object): The value to write.

    Returns:
        int: 0 if the write failed immediately, 1 if it succeeded
            immediately, and 2 if it is pending.
    """
    quality_codes = system.tag.writeBlocking([tag_path], [value])
    return quality_codes[0].isGood()
