# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Date module."""

__all__ = [
    'compare'
]

import system.date


def compare(start_date=system.date.now(), end_date=system.date.now()):
    """Compares two Dates; Date a and Date b.

    Args:
        start_date (Date): The first date.
        end_date (Date): The second date.

    Returns:
        int: 0 if start_date and end_date are equal, -1. If end_date is greater than start_date, 1.
            If start_date is greater than end_date.
    """
    ret_val = 1

    if start_date == end_date:
        ret_val = 0
    elif start_date < end_date:
        ret_val = -1

    return ret_val
