__all__ = ["PageFormat", "Paper"]

from typing import List

from java.lang import Object


class PageFormat(Object):
    LANDSCAPE = 0
    PORTRAIT = 1
    REVERSE_LANDSCAPE = 2

    def clone(self):
        # type: () -> Object
        pass

    def getHeight(self):
        # type: () -> float
        pass

    def getImageableHeight(self):
        # type: () -> float
        pass

    def getImageableWidth(self):
        # type: () -> float
        pass

    def getImageableX(self):
        # type: () -> float
        pass

    def getImageableY(self):
        # type: () -> float
        pass

    def getMatrix(self):
        # type: () -> List[float]
        pass

    def getOrientation(self):
        # type: () -> int
        pass

    def getPaper(self):
        # type: () -> Paper
        pass

    def setOrientation(self, orientation):
        # type: (int) -> None
        pass

    def setPaper(self, paper):
        # type: (Paper) -> None
        pass


class Paper(Object):
    def clone(self):
        # type: () -> Object
        pass

    def getHeight(self):
        # type: () -> float
        pass

    def getImageableHeight(self):
        # type: () -> float
        pass

    def getImageableWidth(self):
        # type: () -> float
        pass

    def getImageableX(self):
        # type: () -> float
        pass

    def getImageableY(self):
        # type: () -> float
        pass

    def getWidth(self):
        # type: () -> float
        pass

    def setImageableArea(self, x, y, width, height):
        # type: (float, float, float, float) -> None
        pass

    def setSize(self, width, height):
        # type: (float, float) -> None
        pass
