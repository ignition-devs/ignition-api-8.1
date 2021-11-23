"""Dataset Functions.

The following functions give you access to view and interact with
datasets.
"""

from __future__ import print_function, unicode_literals

__all__ = [
    "addColumn",
    "addRow",
    "addRows",
    "appendDataset",
    "clearDataset",
    "dataSetToHTML",
    "deleteRow",
    "deleteRows",
    "exportCSV",
    "exportExcel",
    "exportHTML",
    "filterColumns",
    "formatDates",
    "fromCSV",
    "getColumnHeaders",
    "setValue",
    "sort",
    "toCSV",
    "toDataSet",
    "toExcel",
    "toPyDataSet",
    "updateRow",
]

import os.path
from typing import Any, Dict, List, Optional, Type, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import DatasetUtilities
from java.util import Locale

PyDataSet = DatasetUtilities.PyDataSet


def addColumn(
    dataset,  # type: BasicDataset
    colIndex,  # type: int
    col,  # type: List[Any]
    colName,  # type: Union[str, unicode]
    colType,  # type: Type
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new column added
    or inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a column to a dataset. You'll need to
    do something with the new dataset that this function creates to
    achieve something useful. If the columnIndex argument is omitted,
    the column will be appended to the end of the dataset.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        colIndex: The index (starting at 0) at which to insert the new
            column. Will throw an IndexError if less than zero or
            greater than the length of the dataset. If omitted, the new
            column will be appended to the end. Optional.
        col: A Python sequence representing the data for the new column.
            Its length must equal the number of rows in the dataset.
        colName: The name of the column.
        colType: The type of the of the column. The type can be the
            Python equivalent of String, Long, Double, Short, Integer,
            Float, Boolean, null, or java.util.Date if they exist.

    Returns:
        A new dataset with the new column inserted or appended.
    """
    print(dataset, colIndex, col, colName, colType)
    return BasicDataset()


def addRow(dataset, rowIndex, row):
    # type: (BasicDataset, int, List[Any]) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a row to a dataset. You'll need to do
    something with the new dataset that this function creates to achieve
    something useful. If the rowIndex argument is omitted, the row will
    be appended to the end of the dataset.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        rowIndex: The index (starting at 0) at which to insert the new
            row. Will throw an IndexError if less than zero or greater
            than the length of the dataset. If omitted, the new row will
            be appended to the end. Optional.
        row: A Python sequence representing the data for the new row.
            Its length must equal the number of columns in the dataset.

    Returns:
        A new dataset with the new row inserted or appended.
    """
    print(dataset, rowIndex, row)
    return BasicDataset()


def addRows(dataset, rowIndex, rows):
    # type: (BasicDataset, int, List[Any]) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a row to a dataset. You'll need to do
    something with the new dataset that this function creates to achieve
    something useful. If the rowIndex argument is omitted, the row will
    be appended to the end of the dataset.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        rowIndex: The index (starting at 0) at which to insert the new
            row. Will throw an IndexError if less than zero or greater
            than the length of the dataset. If omitted, the new row will
            be appended to the end. Optional.
        rows: A Python sequence representing the data for the new rows.
            The length of each sequence must equal the number of columns
            in the dataset.

    Returns:
        A new dataset with the new row inserted or appended.
    """
    print(dataset, rowIndex, rows)
    return BasicDataset()


def appendDataset(dataset1, dataset2):
    # type: (BasicDataset, BasicDataset) -> BasicDataset
    """Takes two different datasets and returns a new dataset with the
    second dataset appended to the first.

    Will throw an error if the number and types of columns do not match.

    Args:
        dataset1: The dataset that will come first in the returned
            dataset.
        dataset2: The second dataset that will be appended to the end in
            the returned dataset.

    Returns:
        A new dataset that is a combination of the original two
        datasets.
    """
    print(dataset1, dataset2)
    return BasicDataset()


def clearDataset(dataset):
    # type: (BasicDataset) -> BasicDataset
    """Takes a dataset and returns a new dataset with all of the same
    column names, but all of the rows deleted.

    Args:
        dataset: The starting dataset. If NULL, a NULL dataset will be
            returned.

    Returns:
        A new dataset with no data.
    """
    print(dataset)
    return BasicDataset()


def dataSetToHTML(
    showHeaders,  # type: bool
    dataset,  # type: BasicDataset
    title,  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode]
    """Formats the contents of a dataset as an HTML page, returning the
    results as a string.

    Uses the <table> element to create a data table page.

    Args:
        showHeaders: If True(1), the HTML table will include a header
            row.
        dataset: The dataset to export.
        title: The title for the HTML page.

    Returns:
        The HTML page as a string.
    """
    print(showHeaders, dataset, title)
    return "<html><head>{}</head><body>data</body></html>".format(title)


def deleteRow(dataset, rowIndex):
    # type: (BasicDataset, int) -> BasicDataset
    """Takes a dataset and returns a new dataset with a row removed.

    Datasets are immutable, so it is important to realize that this
    function does not actually remove the row from the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        rowIndex: The index (starting at 0) of the row to delete.

    Returns:
        A new dataset with the specified row removed.

    Raises:
        IndexError: If rowIndex is less than zero or greater than the
            row count of the dataset -1.
    """
    print(dataset, rowIndex)
    if rowIndex < 0:
        raise IndexError("Error")

    return BasicDataset()


def deleteRows(dataset, rowIndices):
    # type: (BasicDataset, List[int]) -> BasicDataset
    """Takes a dataset and returns a new dataset with one or more rows
    removed.

    Datasets are immutable, so it is important to realize that this
    function does not actually remove the rows from the argument
    dataset. You'll need to do something with the new dataset that this
    function creates to achieve something useful.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        rowIndices: The indices (starting at 0) of the rows to delete.

    Returns:
        A new dataset with the specified row removed.

    Raises:
        IndexError: If any element is less than zero or greater than the
            number of rows in the dataset - 1.
    """
    print(dataset, rowIndices)
    if -1 in rowIndices:
        raise IndexError("Error")

    return BasicDataset()


def exportCSV(
    filename,  # type: Union[str, unicode]
    showHeaders,  # type: bool
    dataset,  # type: BasicDataset
):
    # type: (...) -> Union[str, unicode]
    """Exports the contents of a dataset as a CSV file, prompting the
    user to save the file to disk.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True (1), the CSV file will include a header
            row.
        dataset: The dataset to export.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset)
    return os.path.expanduser("~")


def exportExcel(
    filename,  # type: Union[str, unicode]
    showHeaders,  # type: bool
    dataset,  # type: List[BasicDataset]
    nullsEmpty=False,  # type: Optional[bool]
):
    # type: (...) -> Union[str, unicode]
    """Exports the contents of a dataset as an Excel spreadsheet,
    prompting the user to save the file to disk.

    Uses the same format as the dataSetToExcel function.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True (1), the spreadsheet will include a header
            row.
        dataset: A sequence of datasets, one for each sheet in the
            resulting workbook.
        nullsEmpty: If True (1), the spreadsheet will leave cells with
            NULL values empty, instead of allowing Excel to provide a
            default value like 0. Defaults to False. Optional.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset, nullsEmpty)
    return os.path.expanduser("~")


def exportHTML(
    filename,  # type: Union[str, unicode]
    showHeaders,  # type: bool
    dataset,  # type: BasicDataset
    title,  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode]
    """Exports the contents of a dataset to an HTML page.

    Prompts the user to save the file to disk.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True (1), the HTML table will include a header
            row.
        dataset: The dataset to export.
        title: The title for the HTML page.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset, title)
    return os.path.expanduser("~")


def filterColumns(
    dataset,  # type: BasicDataset
    columns,  # type: List[Union[Union[str, unicode], int]]
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a view of the dataset containing only
    the columns found within the given list of columns.

    Args:
        dataset: The starting dataset.
        columns: A list of columns to keep in the returned dataset. The
            columns may be in integer index form (starting at 0), or the
            name of the columns as Strings.

    Returns:
        A new dataset containing the filtered columns.
    """
    print(dataset, columns)
    return BasicDataset()


def formatDates(
    dataset,  # type: BasicDataset
    dateFormat,  # type: Union[str, unicode]
    locale=Locale.ENGLISH,  # type: Optional[Any]
):
    # type: (...) -> BasicDataset
    """Returns a new dataset with Date columns as strings formatted
    according to the dateFormat specified.

    Args:
        dataset: The starting dataset to format.
        dateFormat: A valid Java DateFormat string such as
            "yyyy-MM-dd HH:mm:ss". See system.date.format for more
            information on the valid characters.
        locale: The Locale to use for formatting. If no Locale is
            specified, the default Locale will be used. Optional.

    Returns:
        A new dataset, containing the formatted dates.
    """
    print(dataset, dateFormat, locale)
    return BasicDataset()


def fromCSV(csv):
    # type: (Union[str, unicode]) -> BasicDataset
    """Converts a dataset stored in a CSV formatted string to a dataset
    that can be immediately assignable to a dataset property in your
    project.

    Usually this is used in conjunction with
    system.file.readFileAsString when reading in a CSV file that was
    exported using system.dataset.toCSV. The CSV string must be
    formatted in a specific way.

    Args:
        csv: A string holding a CSV dataset.

    Returns:
        A new dataset.
    """
    print(csv)
    return BasicDataset()


def getColumnHeaders(dataset):
    # type: (BasicDataset) -> List[Union[str, unicode]]
    """Takes in a dataset and returns the headers as a python list.

    Args:
        dataset: The input dataset.

    Returns:
        A list of column header strings.
    """
    print(dataset)
    return []


def setValue(
    dataset,  # type: BasicDataset
    rowIndex,  # type: int
    columnName,  # type: Union[str, unicode]
    value,  # type: Any
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a new dataset with a one value
    altered.

    Datasets are immutable, so it is important to realize that this
    function does not actually set a value in the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    Args:
        dataset: The starting dataset. Will not be modified (datasets
            are immutable), but acts as the basis for the returned
            dataset.
        rowIndex: The index of the row to set the value at (starting at
            0).
        columnName: The name of the column to set the value at. Case
            insensitive.
        value: The new value for the specified row/column.

    Returns:
         A new dataset, with the new value set at the given location.
    """
    print(dataset, rowIndex, columnName, value)
    return BasicDataset()


def sort(
    dataset,  # type: BasicDataset
    keyColumn,  # type: Union[Union[str, unicode], int]
    ascending=True,  # type: Optional[bool]
):
    # type: (...) -> BasicDataset
    """Sorts a dataset and returns the sorted dataset.

    This works on numeric, as well as alphanumeric columns. It will go
    character by character, going from 0-9, A-Z, a-z.

    Args:
        dataset: The dataset to sort.
        keyColumn: The index or column name of the column to sort on.
        ascending: True for ascending order, False for descending order.
            If omitted, ascending order will be used. Optional.

    Returns:
        A new sorted dataset.
    """
    print(dataset, keyColumn, ascending)
    return BasicDataset()


def toCSV(
    dataset,  # type: BasicDataset
    showHeaders=True,  # type: Optional[bool]
    forExport=False,  # type: Optional[bool]
    localized=False,  # type: Optional[bool]
):
    # type: (...) -> Union[str, unicode]
    """Formats the contents of a dataset as CSV (comma separated
    values), returning the resulting CSV as a string.

    If the "forExport" flag is set, then the format will be appropriate
    for parsing using the system.dataset.fromCSV function.

    Args:
        dataset: The dataset to export to CSV.
        showHeaders: If set to True(1), a header row will be present in
            the CSV. Default is True(1). Optional.
        forExport: If set to True(1), extra header information will be
            present in the CSV data which is necessary for the CSV to be
            compatible with the fromCSV method. Overrides showHeaders.
            Default is False(0). Optional.
        localized: If set to True(1), the string representations of the
            values in the CSV data will be localized. Default is
            False(0). Optional.

    Returns:
        The CSV data as a string.
    """
    print(dataset, showHeaders, forExport, localized)
    return ""


def toDataSet(*args):
    # type: (...) -> BasicDataset
    """This function is used to convert PyDataSets to DataSets, and to
    create new datasets from raw Python lists.

    When creating a new dataset, headers should have unique names.

    1) system.dataset.toDataSet(dataset)
    2) system.dataset.toDataSet(headers, data)

    Args:
        args: A variable-length argument list.

    Returns:
        The newly created dataset.
    """
    print(args)
    return BasicDataset()


def toExcel(
    showHeaders,  # type: bool
    dataset,  # type: List[BasicDataset]
    nullsEmpty=False,  # type: Optional[bool]
    sheetNames=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> Any
    """Formats the contents of one or more datasets as an excel
    spreadsheet, returning the results as a string.

    Each dataset specified will be added as a worksheet in the Excel
    workbook. This function uses an xml-format for Excel spreadsheets,
    not the native Excel file format.

    Args:
        showHeaders: If True, the spreadsheet will include a header row.
            If False, the header row will be omitted.
        dataset: A sequence of one or more datasets, one for each sheet
            in the resulting workbook.
        nullsEmpty: If True (1), the spreadsheet will leave cells with
            NULL values empty, instead of allowing Excel to provide a
            default value like 0. Defaults to False. Optional.
        sheetNames: Expects a list of strings, where each string is a
            name for one of the datasets. When used, there must be an
            equal number of string names in sheetName as there are
            datasets in the dataset parameter. Names provided in this
            parameter may be sanitized into acceptable Excel sheet
            names. Optional.

    Returns:
        An Excel-compatible XML-based workbook, with one worksheet per
        dataset.
    """
    print(showHeaders, dataset, nullsEmpty, sheetNames)


def toPyDataSet(dataset):
    # type: (BasicDataset) -> PyDataSet
    """This function converts from a normal DataSet to a PyDataSet,
    which is a wrapper class which makes working with datasets more
    Python-esque.

    Args:
        dataset: A DataSet object to convert into a PyDataSet.

    Returns:
        The newly created PyDataSet.
    """
    print(dataset)
    return PyDataSet()


def updateRow(
    dataset,  # type: BasicDataset
    rowIndex,  # type: int
    changes,  # type: Dict[Union[str, unicode], Any]
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a new dataset with a one row altered.

    Datasets are immutable, so it is important to realize that this
    function does not actually change the row in the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    To alter the row, this function takes a Python dictionary to
    represent the changes to make to the specified row. The keys in the
    dictionary are used to find the columns to alter.

    Args:
        dataset: The starting dataset. Will not be modified (datasets
            are immutable), but acts as the basis for the returned
            dataset.
        rowIndex: The index of the row to update (starting at 0).
        changes: A Dictionary of changes to make. They keys in the
            dictionary should match column names in the dataset, and
            their values will be used to update the row.

    Returns:
         A new dataset with the values at the specified row updated
         according to the values in the dictionary.
    """
    print(dataset, rowIndex, changes)
    return BasicDataset()
