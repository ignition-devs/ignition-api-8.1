"""File Functions.

The following functions give you access to read and write to files.
"""

from __future__ import print_function

__all__ = [
    "fileExists",
    "getTempFile",
    "openFile",
    "openFiles",
    "readFileAsBytes",
    "readFileAsString",
    "saveFile",
    "writeFile",
]

import io
import os.path
import tempfile

from typing import Any, List, Optional

from java.lang import String


def fileExists(filepath):
    # type: (String) -> bool
    """Checks to see if a file or folder at a given path exists.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file or folder to check.

    Returns:
        True if the file/folder exists, False otherwise.
    """
    return os.path.isfile(filepath)


def getTempFile(extension):
    # type: (String) -> String
    """Creates a new temp file on the host machine with a certain
    extension, returning the path to the file.

    The file is marked to be removed when the Java VM exits.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        extension: An extension, like ".txt", to append to the end of
            the temporary file.

    Returns:
        The path to the newly created temp file.
    """
    suffix = ".{}".format(extension)
    with tempfile.NamedTemporaryFile(suffix=suffix) as temp:
        return unicode(temp.name)


def openFile(extension=None, defaultLocation=None):
    # type: (Optional[String], Optional[String]) -> Optional[String]
    r"""Shows an "Open File" dialog box, prompting the user to choose a
    file to open.

    Returns the path to the file that the user chose, or None if the
    user canceled the dialog box. An extension can optionally be passed
    in that sets the filetype filter to that extension.

    Args:
        extension: A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation: A folder location, like "C:\\MyFiles", to use
            as the starting location for the file chooser. Optional.

    Returns:
        The path to the selected file, or None if canceled.
    """
    print(extension, defaultLocation)
    return ""


def openFiles(
    extension=None,  # type: Optional[String]
    defaultLocation=None,  # type: Optional[String]
):
    # type: (...) -> Optional[List[String]]
    r"""Shows an "Open File" dialog box, prompting the user to choose a
    file or files to open.

    Returns the paths to the files that the user chooses, or None if the
    user canceled the dialog box. An extension can optionally be passed
    in that sets the filetype filter to that extension.

    Args:
        extension: A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation: A folder location, like "C:\\MyFiles", to use
            as the starting location for the file chooser. Optional.

    Returns:
        The paths to the selected files, or None if canceled.
    """
    print(extension, defaultLocation)
    return ["path/to/file"]


def readFileAsBytes(filepath):
    # type: (String) -> Any
    """Opens the file found at path filename, and reads the entire file.

    Returns the file as an array of bytes. Commonly this array of bytes
    is uploaded to a database table with a column of type BLOB (Binary
    Large OBject). This upload would be done through an INSERT or UPDATE
    SQL statement run through the system.db.runPrepUpdate function. You
    could also write the bytes to another file using the
    system.file.writeFile function, or send the bytes as an email
    attachment using system.net.sendEmail.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to read.

    Returns:
        The contents of the file as an array of bytes.
    """
    with io.open(filepath, "r+b") as f:
        return f.read()


def readFileAsString(filepath, encoding="UTF-8"):
    # type: (String, Optional[String]) -> String
    """Opens the file found at path filename, and reads the entire file.

    Returns the file as a string. Common things to do with this string
    would be to load it into the text property of a component, upload it
    to a database table, or save it to another file using
    system.file.writeFile function.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to read.
        encoding: The character encoding of the file to be read. Will
            throw an exception if the string does not represent a
            supported encoding. Common encodings are "UTF-8",
            "ISO-8859-1" and "US-ASCII". Default is "UTF-8". Optional.

    Returns:
        The contents of the file as a string.
    """
    with io.open(filepath, "r", encoding=encoding) as f:
        return unicode(f.read())


def saveFile(
    filename,  # type: String
    extension=None,  # type: Optional[String]
    typeDesc=None,  # type: Optional[String]
):
    # type: (...) -> Optional[String]
    """Prompts the user to save a new file named filename.

    The optional extension and typeDesc arguments can be added to be
    used as a type filter. If the user accepts the save, the path to
    that file will be returned. If the user cancels the save, None will
    be returned.

    Args:
        filename: A file name to suggest to the user.
        extension: The appropriate file extension, like "jpeg", for the
            file. Optional.
        typeDesc: A description of the extension, like "JPEG Image".
            Optional.

    Returns:
        The path to the file that the user decided to save to, or None
        if they canceled.
    """
    print(filename, extension, typeDesc)
    return ""


def writeFile(
    filepath,  # type: String
    data,  # type: Any
    append=False,  # type: bool
    encoding="UTF-8",  # type: String
):
    # type: (...) -> None
    """Writes the given data to the file at file path filename.

    If the file exists, the append argument determines whether or not it
    is overwritten (the default) or appended to. The data argument can
    be either a string or an array of bytes (commonly retrieved from a
    BLOB in a database or read from another file using
    system.file.readFileAsBytes).

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to write to.
        data: The character or binary content to write to the file.
        append: If True, the file will be appended to if it already
            exists. If False, the file will be overwritten if it
            exists. The default is False. Optional.
        encoding: The character encoding of the file to write. Will
            throw an exception if the string does not represent a
            supported encoding. Common encodings are "UTF-8",
            "ISO-8859-1" and "US-ASCII". Default is "UTF-8". Optional.
    """
    print(filepath, data, append, encoding)
