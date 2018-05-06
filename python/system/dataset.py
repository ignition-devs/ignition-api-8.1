# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Dataset Functions
The following functions give you access to view and interact with datasets."""

__all__ = [
    'getColumnHeaders',
    'toDataSet',
    'toPyDataSet'
]


def getColumnHeaders(dataset):
    """Takes in a dataset and returns the headers as a python list.

    Args:
        dataset (Dataset): The input dataset.

    Returns:
        list[str]: A list of column header strings.
    """
    print dataset
    return []


def toDataSet(*args):
    """This function is used to 1) convert PyDataSets to DataSets, and 2) create new datasets from
    raw Python lists. When creating a new dataset, headers should have unique names.

    1) system.dataset.toDataSet(dataset)
    2) system.dataset.toDataSet(headers, data)

    Args:
        args: A variable-length argument list.

    Returns:
        Dataset: The newly created dataset.
    """
    for arg in args:
        print arg


def toPyDataSet(dataset):
    """This function converts from a normal DataSet to a PyDataSet, which is a wrapper class which
    makes working with datasets more Python-esque.

    Args:
        dataset (Dataset): A DataSet object to convert into a PyDataSet.

    Returns:
        PyDataSet: The newly created PyDataSet.
    """
    print dataset
