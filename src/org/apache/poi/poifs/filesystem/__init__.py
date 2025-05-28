from typing import Any, List, Set

from dev.coatl.helper.types import AnyStr
from org.apache.poi.hpsf import ClassID


class Entry(object):
    def delete(self):
        # type: () -> bool
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getParent(self):
        # type: () -> DirectoryEntry
        pass

    def isDirectoryEntry(self):
        # type: () -> bool
        pass

    def isDocumentEntry(self):
        # type: () -> bool
        pass

    def renameTo(self, newName):
        # type: (AnyStr) -> None
        pass


class DirectoryEntry(Entry):
    def createDirectory(self, name):
        # type: (AnyStr) -> DirectoryEntry
        pass

    def createDocument(self, *args):
        # type: (*Any) -> None
        pass

    def getEntries(self):
        # type: () -> List[Entry]
        pass

    def getEntry(self, name):
        # type: (AnyStr) -> Entry
        pass

    def getEntryCount(self):
        # type: () -> int
        pass

    def getEntryNames(self):
        # type: () -> Set[AnyStr]
        pass

    def getStorageClsid(self):
        # type: () -> ClassID
        pass

    def hasEntry(self, name):
        # type: (AnyStr) -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def setStorageClsid(self, clsidStorage):
        # type: (ClassID) -> None
        pass
