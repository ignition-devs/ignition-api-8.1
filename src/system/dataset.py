"""Dataset Functions.

The following functions give you access to view and interact with
datasets.
"""

from __future__ import print_function

__all__ = [
    "Dataset",
    "PyDataSet",
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

import os
from collections import Iterable

from java.util import Locale


class Dataset(Iterable):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def __iter__(self):
        """Return the iterator object itself."""
        pass

    def getColumnCount(self):
        """Returns the number of columns in the dataset.

        Returns:
            int: The number of columns in the dataset.
        """
        print(self)
        return 4

    def getColumnIndex(self, colName):
        """Returns the index of the column with the name colName.

        Args:
            colName (str): The name of the column

        Returns:
            int: The index of the column with the name colName.
        """
        print(self, colName)
        return 2

    def getColumnName(self, colIndex):
        """Returns the name of the column at the index colIndex.

        Args:
            colIndex (str): The index of the column.

        Returns:
            str: The name of the column at the index colIndex.
        """
        print(self, colIndex)
        return "Population"

    def getColumnNames(self):
        """Returns a list with the names of all the columns.

        Returns:
            list[str]: A list with the names of all the columns.
        """
        print(self)
        return ["City", "Population", "Timezone", "GMTOffset"]

    def getColumnType(self, colIndex):
        """Returns the type of the column at the index colIndex.

        Args:
            colIndex (int): The index of the column.

        Returns:
            object: The type of the column at the index colIndex.
        """
        print(self, colIndex)
        return type(0)

    def getColumnTypes(self):
        """Returns a list with the types of all the columns.

        Returns:
             list[object]: A list with the types of all the columns.
        """
        print(self)
        return [type(""), type(0), type(""), type(0)]

    def getRowCount(self):
        """Returns the number of rows in the dataset.

        Returns:
            int: The number of rows in the dataset.
        """
        print(self)
        return 5

    def getValueAt(self, *args):
        """Returns the value at the specified row index and column name.

        Args:
            args (object): args[0] = rowIndex, args[1] colIndex or
                colName.

        Returns:
            object: The value at the specified row index and column
                name.
        """
        ret = None
        if isinstance(args[1], int):
            print(self, "colIndex")
            ret = "PST"
        elif isinstance(args[1], str):
            print(self, "colName")
            ret = 2853114
        return ret


class PyDataSet(Iterable):
    """PyDatasets are special, in that they can be handled similarly to
    other Python sequences.
    """

    def __add__(self, other):
        """Add a new element."""
        pass

    def __iter__(self):
        """Return the iterator object itself."""
        pass

    def __len__(self):
        """Return the number of elements."""
        pass


def addColumn(dataset, colIndex, col, colName, colType):
    """Takes a dataset and returns a new dataset with a new column added
    or inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a column to a dataset. You'll need to
    do something with the new dataset that this function creates to
    achieve something useful. If the columnIndex argument is omitted,
    the column will be appended to the end of the dataset.

    Args:
        dataset (Dataset): The starting dataset. Please be aware that
            this dataset will not actually be modified (datasets are
            immutable), but rather will be the starting point for
            creating a new dataset.
        colIndex (int): The index (starting at 0) at which to insert the
            new column. Will throw an IndexError if less than zero or
            greater than the length of the dataset. If omitted, the new
            column will be appended to the end. Optional.
        col (list[object]): A Python sequence representing the data for
            the new column. Its length must equal the number of rows in
            the dataset.
        colName (str): The name of the column.
        colType (type): The type of the of the column. The type can be
            the Python equivalent of String, Long, Double, Short,
            Integer, Float, Boolean, null, or java.util.Date if they
            exist.

    Returns:
        Dataset: A new dataset with the new column inserted or appended.
    """
    print(dataset, colIndex, col, colName, colType)
    return Dataset()


def addRow(dataset, rowIndex, row):
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a row to a dataset. You'll need to do
    something with the new dataset that this function creates to achieve
    something useful. If the rowIndex argument is omitted, the row will
    be appended to the end of the dataset.

    Args:
        dataset (Dataset): The starting dataset. Please be aware that
            this dataset will not actually be modified (datasets are
            immutable), but rather will be the starting point for
            creating a new dataset.
        rowIndex (int): The index (starting at 0) at which to insert the
            new row. Will throw an IndexError if less than zero or
            greater than the length of the dataset. If omitted, the new
            row will be appended to the end. Optional.
        row (list[object]): A Python sequence representing the data for
            the new row. Its length must equal the number of columns in
            the dataset.

    Returns:
        Dataset: A new dataset with the new row inserted or appended.
    """
    print(dataset, rowIndex, row)
    return Dataset()


def addRows(dataset, rowIndex, rows):
    """Takes a dataset and returns a new dataset with a new row added or
    inserted into it.

    Datasets are immutable, so it is important to realize that this
    function does not actually add a row to a dataset. You'll need to do
    something with the new dataset that this function creates to achieve
    something useful. If the rowIndex argument is omitted, the row will
    be appended to the end of the dataset.

    Args:
        dataset (Dataset): The starting dataset. Please be aware that
            this dataset will not actually be modified (datasets are
            immutable), but rather will be the starting point for
            creating a new dataset.
        rowIndex (int): The index (starting at 0) at which to insert the
            new row. Will throw an IndexError if less than zero or
            greater than the length of the dataset. If omitted, the new
            row will be appended to the end. Optional.
        rows (list[object]): A Python sequence representing the data for
            the new rows. The length of each sequence must equal the
            number of columns in the dataset.

    Returns:
        Dataset: A new dataset with the new row inserted or appended.
    """
    print(dataset, rowIndex, rows)
    return Dataset()


def appendDataset(dataset1, dataset2):
    """Takes two different datasets and returns a new dataset with the
    second dataset appended to the first.

    Will throw an error if the number and types of columns do not match.

    Args:
        dataset1 (Dataset): The dataset that will come first in the
            returned dataset.
        dataset2 (Dataset): The second dataset that will be appended to
            the end in the returned dataset.

    Returns:
        Dataset: A new dataset that is a combination of the original two
            datasets.
    """
    print(dataset1, dataset2)
    return Dataset()


def clearDataset(dataset):
    """Takes a dataset and returns a new dataset with all of the same
    column names, but all of the rows deleted.

    Args:
        dataset (Dataset): The starting dataset. If NULL, a NULL dataset
            will be returned.

    Returns:
        Dataset: A new dataset with no data.
    """
    print(dataset)
    return Dataset()


def dataSetToHTML(showHeaders, dataset, title):
    """Formats the contents of a dataset as an HTML page, returning the
    results as a string.

    Uses the <table> element to create a data table page.

    Args:
        showHeaders (bool): If True(1), the HTML table will include a
            header row.
        dataset (Dataset): The dataset to export.
        title (str): The title for the HTML page.

    Returns:
        str: The HTML page as a string.
    """
    print(showHeaders, dataset, title)
    return "<html><head>{}</head><body>data</body></html>".format(title)


def deleteRow(dataset, rowIndex):
    """Takes a dataset and returns a new dataset with a row removed.

    Datasets are immutable, so it is important to realize that this
    function does not actually remove the row from the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    Args:
        dataset (Dataset): The starting dataset. Please be aware that
            this dataset will not actually be modified (datasets are
            immutable), but rather will be the starting point for
            creating a new dataset.
        rowIndex (int): The index (starting at 0) of the row to delete.

    Returns:
        Dataset: A new dataset with the specified row removed.

    Raises:
        IndexError: If rowIndex is less than zero or greater than the
            row count of the dataset -1.
    """
    print(dataset, rowIndex)
    if rowIndex < 0:
        raise IndexError("Error")

    return Dataset()


def deleteRows(dataset, rowIndices):
    """Takes a dataset and returns a new dataset with one or more rows
    removed.

    Datasets are immutable, so it is important to realize that this
    function does not actually remove the rows from the argument
    dataset. You'll need to do something with the new dataset that this
    function creates to achieve something useful.

    Args:
        dataset (Dataset): The starting dataset. Please be aware that
            this dataset will not actually be modified (datasets are
            immutable), but rather will be the starting point for
            creating a new dataset.
        rowIndices (list[int]): The indices (starting at 0) of the rows
            to delete.

    Returns:
        Dataset: A new dataset with the specified row removed.

    Raises:
        IndexError: If any element is less than zero or greater than the
            number of rows in the dataset - 1.
    """
    print(dataset, rowIndices)
    if -1 in rowIndices:
        raise IndexError("Error")

    return Dataset()


def exportCSV(filename, showHeaders, dataset):
    """Exports the contents of a dataset as a CSV file, prompting the
    user to save the file to disk.

    Args:
        filename (str): A suggested filename to save as.
        showHeaders (bool): If True (1), the CSV file will include a
            header row.
        dataset (Dataset): The dataset to export.

    Returns:
        str: The path to the saved file, or None if the action was
            canceled by the user.
    """
    print(filename, showHeaders, dataset)
    return os.path.expanduser("~")


def exportExcel(filename, showHeaders, dataset, nullsEmpty=False):
    """Exports the contents of a dataset as an Excel spreadsheet,
    prompting the user to save the file to disk. Uses the same format as
    the toExcel function.

    Args:
        filename (str): A suggested filename to save as.
        showHeaders (bool): If True (1), the spreadsheet will include a
            header row.
        dataset (list[Dataset]): A sequence of datasets, one for each
            sheet in the resulting workbook.
        nullsEmpty (bool): If True (1), the spreadsheet will leave cells
            with NULL values empty, instead of allowing Excel to provide
            a default value like 0. Defaults to False. Optional.

    Returns:
        str: The path to the saved file, or None if the action was
            canceled by the user.
    """
    print(filename, showHeaders, dataset, nullsEmpty)
    return os.path.expanduser("~")


def exportHTML(filename, showHeaders, dataset, title):
    """Exports the contents of a dataset to an HTML page.

    Prompts the user to save the file to disk.

    Args:
        filename (str): A suggested filename to save as.
        showHeaders (bool): If True (1), the HTML table will include a
            header row.
        dataset (Dataset): The dataset to export.
        title (str): The title for the HTML page.

    Returns:
        str: The path to the saved file, or None if the action was
            canceled by the user.
    """
    print(filename, showHeaders, dataset, title)
    return os.path.expanduser("~")


def filterColumns(dataset, columns):
    """Takes a dataset and returns a view of the dataset containing only
    the columns found within the given list of columns.

    Args:
        dataset (Dataset): The starting dataset.
        columns (list[object]): A list of columns to keep in the
            returned dataset. The columns may be in integer index form
            (starting at 0), or the name of the columns as Strings.

    Returns:
        Dataset: A new dataset containing the filtered columns.
    """
    print(dataset, columns)
    return Dataset()


def formatDates(dataset, dateFormat, locale=Locale.ENGLISH):
    """Returns a new dataset with Date columns as strings formatted
    according to the dateFormat specified.

    Args:
        dataset (Dataset): The starting dataset to format.
        dateFormat (str): A valid Java DateFormat string such as
            "yyyy-MM-dd HH:mm:ss". See system.date.format for more
            information on the valid characters.
        locale (Locale): The Locale to use for formatting. If no Locale
            is specified, the default Locale will be used. Optional.

    Returns:
        Dataset: A new dataset, containing the formatted dates.
    """
    print(dataset, dateFormat, locale)
    return Dataset()


def fromCSV(csv):
    """Converts a dataset stored in a CSV formatted string to a dataset
    that can be immediately assignable to a dataset property in your
    project.

    Usually this is used in conjunction with
    system.file.readFileAsString when reading in a CSV file that was
    exported using system.dataset.toCSV. The CSV string must be
    formatted in a specific way.

    Args:
        csv (str): A string holding a CSV dataset.

    Returns:
        Dataset: A new dataset.
    """
    print(csv)
    return Dataset()


def getColumnHeaders(dataset):
    """Takes in a dataset and returns the headers as a python list.

    Args:
        dataset (Dataset): The input dataset.

    Returns:
        list[str]: A list of column header strings.
    """
    print(dataset)
    return []


def setValue(dataset, rowIndex, columnName, value):
    """Takes a dataset and returns a new dataset with a one value
    altered.

    Datasets are immutable, so it is important to realize that this
    function does not actually set a value in the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    Args:
        dataset (Dataset): The starting dataset. Will not be modified
            (datasets are immutable), but acts as the basis for the
            returned dataset.
        rowIndex (int): The index of the row to set the value at
            (starting at 0).
        columnName (str): The name of the column to set the value at.
            Case insensitive.
        value (object): The new value for the specified row/column.

    Returns:
         Dataset: A new dataset, with the new value set at the given
            location.
    """
    print(dataset, rowIndex, columnName, value)
    return Dataset()


def sort(dataset, keyColumn, ascending=True):
    """Sorts a dataset and returns the sorted dataset.

    This works on numeric, as well as alphanumeric columns. It will go
    character by character, going from 0-9, A-Z, a-z.

    Args:
        dataset (Dataset): The dataset to sort.
        keyColumn (object): The index or column name of the column to
            sort on.
        ascending (bool): True for ascending order, False for descending
            order. If omitted, ascending order will be used. Optional.

    Returns:
        Dataset: A new sorted dataset.
    """
    print(dataset, keyColumn, ascending)
    return Dataset()


def toCSV(dataset, showHeaders=True, forExport=False, localized=False):
    """Formats the contents of a dataset as CSV (comma separated
    values), returning the resulting CSV as a string.

    If the "forExport" flag is set, then the format will be appropriate
    for parsing using the system.dataset.fromCSV function.

    Args:
        dataset (Dataset): The dataset to export to CSV.
        showHeaders (bool): If set to True(1), a header row will be
            present in the CSV. Default is True(1). Optional.
        forExport (bool): If set to True(1), extra header information
            will be present in the CSV data which is necessary for the
            CSV to be compatible with the fromCSV method. Overrides
            showHeaders. Default is False(0). Optional.
        localized (bool): If set to True(1), the string representations
            of the values in the CSV data will be localized. Default is
            False(0). Optional.

    Returns:
        str: The CSV data as a string.
    """
    print(dataset, showHeaders, forExport, localized)
    return ""


def toDataSet(*args):
    """This function is used to convert PyDataSets to DataSets, and to
    create new datasets from raw Python lists.

    When creating a new dataset, headers should have unique names.

    1) system.dataset.toDataSet(dataset)
    2) system.dataset.toDataSet(headers, data)

    Args:
        args: A variable-length argument list.

    Returns:
        Dataset: The newly created dataset.
    """
    for arg in args:
        print(arg)
    return Dataset()


def toExcel(showHeaders, dataset, nullsEmpty=False, sheetNames=None):
    """Formats the contents of one or more datasets as an excel
    spreadsheet, returning the results as a string.

    Each dataset specified will be added as a worksheet in the Excel
    workbook. This function uses an xml-format for Excel spreadsheets,
    not the native Excel file format.

    Args:
        showHeaders (bool): If True, the spreadsheet will include a
            header row. If False, the header row will be omitted.
        dataset (list[Dataset]): A sequence of one or more datasets,
            one for each sheet in the resulting workbook.
        nullsEmpty (bool): If True (1), the spreadsheet will leave cells
            with NULL values empty, instead of allowing Excel to provide
            a default value like 0. Defaults to False. Optional.
        sheetNames (list[str]): Expects a list of strings, where each
            string is a name for one of the datasets. When used, there
            must be an equal number of string names in sheetName as
            there are datasets in the dataset parameter. Names provided
            in this parameter may be sanitized into acceptable Excel
            sheet names. Optional.

    Returns:
        str: An Excel-compatible XML-based workbook, with one worksheet
            per dataset.
    """
    print(showHeaders, dataset, nullsEmpty, sheetNames)


def toPyDataSet(dataset):
    """This function converts from a normal DataSet to a PyDataSet,
    which is a wrapper class which makes working with datasets more
    Python-esque.

    Args:
        dataset (Dataset): A DataSet object to convert into a PyDataSet.

    Returns:
        PyDataSet: The newly created PyDataSet.
    """
    print(dataset)
    return PyDataSet()


def updateRow(dataset, rowIndex, changes):
    """Takes a dataset and returns a new dataset with a one row altered.

    Datasets are immutable, so it is important to realize that this
    function does not actually change the row in the argument dataset.
    You'll need to do something with the new dataset that this function
    creates to achieve something useful.

    To alter the row, this function takes a Python dictionary to
    represent the changes to make to the specified row. The keys in the
    dictionary are used to find the columns to alter.

    Args:
        dataset (Dataset): The starting dataset. Will not be modified
            (datasets are immutable), but acts as the basis for the
            returned dataset.
        rowIndex (int): The index of the row to update (starting at 0).
        changes (dict): A Dictionary of changes to make. They keys in
            the dictionary should match column names in the dataset, and
            their values will be used to update the row.

    Returns:
         Dataset: A new dataset with the values at the specified row
            updated according to the values in the dictionary.
    """
    print(dataset, rowIndex, changes)
    return Dataset()
