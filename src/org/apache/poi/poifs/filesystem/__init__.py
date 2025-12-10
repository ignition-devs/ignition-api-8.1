from typing import Any, List, Set, Union

from org.apache.poi.hpsf import ClassID


class Entry(object):
    def delete(self):
        # type: () -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getParent(self):
        # type: () -> DirectoryEntry
        raise NotImplementedError

    def isDirectoryEntry(self):
        # type: () -> bool
        raise NotImplementedError

    def isDocumentEntry(self):
        # type: () -> bool
        raise NotImplementedError

    def renameTo(self, newName):
        # type: (Union[str, unicode]) -> None
        raise NotImplementedError


class DirectoryEntry(Entry):
    def createDirectory(self, name):
        # type: (Union[str, unicode]) -> DirectoryEntry
        pass

    def createDocument(self, *args):
        # type: (*Any) -> None
        pass

    def delete(self):
        # type: () -> bool
        pass

    def getEntries(self):
        # type: () -> List[Entry]
        pass

    def getEntry(self, name):
        # type: (Union[str, unicode]) -> Entry
        pass

    def getEntryCount(self):
        # type: () -> int
        pass

    def getEntryNames(self):
        # type: () -> Set[Union[str, unicode]]
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getParent(self):
        # type: () -> DirectoryEntry
        pass

    def getStorageClsid(self):
        # type: () -> ClassID
        pass

    def hasEntry(self, name):
        # type: (Union[str, unicode]) -> bool
        pass

    def isDirectoryEntry(self):
        # type: () -> bool
        pass

    def isDocumentEntry(self):
        # type: () -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def renameTo(self, newName):
        # type: (Union[str, unicode]) -> None
        pass

    def setStorageClsid(self, clsidStorage):
        # type: (ClassID) -> None
        pass
