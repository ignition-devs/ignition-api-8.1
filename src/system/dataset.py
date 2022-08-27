"""Dataset Functions.

The following functions give you access to view and interact with
datasets.
"""

from __future__ import print_function

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

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.script.builtin import DatasetUtilities
from java.lang import String
from java.util import Date, Locale

ColType = Union[Date, float, int, str, unicode]


def addColumn(
    dataset,  # type: BasicDataset
    colIndex,  # type: int
    col,  # type: List[Any]
    colName,  # type: String
    colType,  # type: Type[ColType]
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new column added
    or inserted into it.

    If the `colIndex` argument is omitted, the column will be appended
    to the end of the dataset.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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
        colType: The type of the of the column. The type can be a Python
            builtin type, such as str, int, float, or a Java class, such
            as java.util.Date.

    Returns:
        A new dataset with the new column inserted or appended.
    """
    print(dataset, colIndex, col, colName, colType)
    return BasicDataset()


def addRow(dataset, rowIndex, row):
    # type: (BasicDataset, int, List[Any]) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    If the `rowIndex` argument is omitted, the column will be appended
    to the end of the dataset.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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
    # type: (BasicDataset, int, List[List[Any]]) -> BasicDataset
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    If the `rowIndex` argument is omitted, the column will be appended
    to the end of the dataset.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

    Args:
        dataset: The starting dataset. Please be aware that this dataset
            will not actually be modified (datasets are immutable), but
            rather will be the starting point for creating a new
            dataset.
        rowIndex: The index (starting at 0) at which to insert the new
            row. Will throw an IndexError if less than zero or greater
            than the length of the dataset. If omitted, the new row will
            be appended to the end. Optional.
        rows: A Python sequence of sequences representing the data for
            the new rows. The length of each sequence must equal the
            number of columns in the dataset.

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

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

    Args:
        dataset: The starting dataset.

    Returns:
        A new dataset with no data.
    """
    print(dataset)
    return BasicDataset()


def dataSetToHTML(showHeaders, dataset, title):
    # type: (bool, BasicDataset, String) -> String
    """Formats the contents of a dataset as an HTML page, returning the
    results as a string.

    Uses the <table> element to create a data table page.

    Args:
        showHeaders: If True, the HTML table will include a header
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

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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


def exportCSV(filename, showHeaders, dataset):
    # type: (String, bool, BasicDataset) -> String
    """Exports the contents of a dataset as a CSV file, prompting the
    user to save the file to disk.

    To write silently to a file, you cannot use the `dataset.export*`
    functions. Instead, use the `toCSV()` function.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the CSV file will include a header
            row.
        dataset: The dataset to export.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset)
    return os.path.expanduser("~")


def exportExcel(filename, showHeaders, dataset, nullsEmpty=False):
    # type: (String, bool, List[BasicDataset], bool) -> String
    """Exports the contents of a dataset as an Excel spreadsheet,
    prompting the user to save the file to disk.

    Uses the same format as the dataSetToExcel function.

    To write silently to a file, you cannot use the `dataset.export*`
    functions. Instead, use the `toExcel()` function.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the spreadsheet will include a header
            row.
        dataset: A sequence of datasets, one for each sheet in the
            resulting workbook.
        nullsEmpty: If True, the spreadsheet will leave cells with NULL
            values empty, instead of allowing Excel to provide a default
            value like 0. Defaults to False. Optional.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset, nullsEmpty)
    return os.path.expanduser("~")


def exportHTML(filename, showHeaders, dataset, title):
    # type: (String, bool, BasicDataset, String) -> String
    """Exports the contents of a dataset to an HTML page.

    Prompts the user to save the file to disk.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the HTML table will include a header
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
    columns,  # type: Union[List[String], List[int]]
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a view of the dataset containing only
    the columns found within the given list of columns.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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


def formatDates(dataset, dateFormat, locale=Locale.ENGLISH):
    # type: (BasicDataset, String, Optional[Locale]) -> BasicDataset
    """Returns a new dataset with Date columns as strings formatted
    according to the dateFormat specified.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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
    # type: (String) -> BasicDataset
    """Converts a dataset stored in a CSV formatted string to a dataset
    that can be immediately assignable to a dataset property in your
    project.

    Usually this is used in conjunction with `readFileAsString` when
    reading in a CSV file that was exported using `toCSV`. The CSV
    string must be formatted in a specific way.

    Args:
        csv: A string holding a CSV dataset.

    Returns:
        A new dataset.
    """
    print(csv)
    return BasicDataset()


def getColumnHeaders(dataset):
    # type: (BasicDataset) -> List[String]
    """Takes in a dataset and returns the headers as a python list.

    Args:
        dataset: The input dataset.

    Returns:
        A list of column header strings.
    """
    print(dataset)
    return ["column1", "column2"]


def setValue(dataset, rowIndex, columnName, value):
    # type: (BasicDataset, int, String, Any) -> BasicDataset
    """Takes a dataset and returns a new dataset with a one value
    altered.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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
    keyColumn,  # type: Union[String, int]
    ascending=True,  # type: bool
):
    # type: (...) -> BasicDataset
    """Takes a dataset and returns a sorted version of dataset.

    The sort order is determined by a single column. This works on
    numeric, as well as alphanumeric columns.

    When sorting alphanumerically, contiguous numbers are treated as a
    single number: you may recognize this as a "natural sort".

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

    Args:
        dataset: The dataset to sort.
        keyColumn: The index or column name to sort on.
        ascending: True for ascending order, False for descending order.
            If omitted, ascending order will be used. Optional.

    Returns:
        A new sorted dataset.
    """
    print(dataset, keyColumn, ascending)
    return BasicDataset()


def toCSV(
    dataset,  # type: BasicDataset
    showHeaders=True,  # type: bool
    forExport=False,  # type: bool
    localized=False,  # type: bool
):
    # type: (...) -> String
    """Formats the contents of a dataset as CSV (comma separated
    values), returning the resulting CSV as a string.

    If the "forExport" flag is set, then the format will be appropriate
    for parsing using the `fromCSV` function.

    Args:
        dataset: The dataset to export to CSV.
        showHeaders: If set to True, a header row will be present in
            the CSV. Default is True. Optional.
        forExport: If set to True, extra header information will be
            present in the CSV data which is necessary for the CSV to be
            compatible with the fromCSV method. Overrides showHeaders.
            Default is False. Optional.
        localized: If set to True, the string representations of the
            values in the CSV data will be localized. Default is
            False. Optional.

    Returns:
        The CSV data as a string.
    """
    print(dataset, showHeaders, forExport, localized)
    return ""


def toDataSet(*args):
    # type: (*Any) -> BasicDataset
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
    nullsEmpty=False,  # type: bool
    sheetNames=None,  # type: Optional[List[String]]
):
    # type: (...) -> Any
    """Formats the contents of one or more datasets as an Excel
    spreadsheet, returning the results as a byte array.

    Each dataset specified will be added as a worksheet in the Excel
    workbook.

    Args:
        showHeaders: If True, the spreadsheet will include a header row.
            If False, the header row will be omitted.
        dataset: A sequence of one or more datasets, one for each sheet
            in the resulting workbook.
        nullsEmpty: If True, the spreadsheet will leave cells with
            NULL values empty, instead of allowing Excel to provide a
            default value like 0. Defaults to False. Optional.
        sheetNames: Expects a list of strings, where each string is a
            name for one of the datasets. When used, there must be an
            equal number of string names in sheetName as there are
            datasets in the dataset parameter. Names provided in this
            parameter may be sanitized into acceptable Excel sheet
            names. Optional.

    Returns:
        A byte array representing an Excel workbook.
    """
    print(showHeaders, dataset, nullsEmpty, sheetNames)


def toPyDataSet(dataset):
    # type: (Dataset) -> DatasetUtilities.PyDataSet
    """This function converts from a normal DataSet to a PyDataSet,
    which is a wrapper class which makes working with datasets more
    Python-esque.

    Args:
        dataset: A Dataset object to convert into a PyDataSet.

    Returns:
        The newly created PyDataSet.
    """
    print(dataset)
    return DatasetUtilities.PyDataSet()


def updateRow(dataset, rowIndex, changes):
    # type: (BasicDataset, int, Dict[String, Any]) -> BasicDataset
    """Takes a dataset and returns a new dataset with a one row altered.

    To alter the row, this function takes a Python dictionary to
    represent the changes to make to the specified row. The keys in the
    dictionary are used to find the columns to alter.

    Note:
        Datasets are immutable, which means they cannot be directly
        modified once created. Instead, this scripting function returns
        a new dataset with some modification applied, which must be
        assigned to a variable to be used.

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
