# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Ignition date module."""

__all__ = [
    'now'
]

import datetime


def now():
    """Returns a java.util.Date object that represents the current time according to the local
    system clock.

    Returns:
        Date: A new date, set to the current date and time.
    """
    return datetime.datetime.now()
