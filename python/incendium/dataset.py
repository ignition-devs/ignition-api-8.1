# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Dataset module."""

__all__ = [
    'to_xml'
]

import system.dataset


def to_xml(dataset, root='root', element='row'):
    """Returns a string XML representation of the Dataset.

    Args:
        dataset (Dataset): The input dataset.
        root (str): The value of the root. If not provided, it
            defaults to "root".
        element (str): The value of the row. If not provided, it
            defaults to "row".

    Returns:
        str: The string XML representation of the dataset.
    """
    headers = system.dataset.getColumnHeaders(dataset)
    data = system.dataset.toPyDataSet(dataset)
    new_line = '\n'
    tab = ' ' * 4
    ret_str = '<%s>%s' % (root, new_line)

    for row in data:
        ret_str += '%s<%s>%s' % (tab, element, new_line)
        for header in headers:
            ret_str += '%s<%s>%s</%s>%s' % (tab * 2, header, row[header],
                                            header, new_line)
        ret_str += '%s</%s>%s' % (tab, element, new_line)
    ret_str += '</%s>' % root

    return ret_str
