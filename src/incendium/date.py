# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Date module."""

__all__ = [
    'compare'
]


def compare(date_1, date_2):
    """Compares two dates.

    Args:
        date_1 (Date): The first date.
        date_2 (Date): The second date.

    Returns:
        int: 0 if date_1 and date_2 are equal, -1. If date_2 is
            greater than date_1, 1. If date_1 is greater than date_2.
    """
    ret_val = 1

    if date_1 == date_2:
        ret_val = 0
    elif date_1 < date_2:
        ret_val = -1

    return ret_val
