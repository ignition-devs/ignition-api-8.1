__all__ = ["Point2D"]

from typing import Any

from java.lang import Object


class Point2D(Object):
    def clone(self):
        # type: () -> Object
        pass

    def distance(self, *args):
        # type: (*Any) -> float
        pass

    def distanceSq(self, *args):
        # type: (*Any) -> float
        pass

    def getX(self):
        # type: () -> float
        raise NotImplementedError

    def getY(self):
        # type: () -> float
        raise NotImplementedError

    def setLocation(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    class Double(Object):
        x = None  # type: float
        y = None  # type: float

        def __init__(self, x=0.0, y=0.0):
            # type: (float, float) -> None
            self.x = x
            self.y = y

        def clone(self):
            # type: () -> Object
            pass

        def distance(self, *args):
            # type: (*Any) -> float
            pass

        def distanceSq(self, *args):
            # type: (*Any) -> float
            pass

        def getX(self):
            # type: () -> float
            return self.x

        def getY(self):
            # type: () -> float
            return self.y

        def setLocation(self, x, y):
            # type: (float, float) -> None
            self.x = x
            self.y = y

    class Float(Object):
        x = None  # type: float
        y = None  # type: float

        def __init__(self, x=0.0, y=0.0):
            # type: (float, float) -> None
            self.x = x
            self.y = y

        def clone(self):
            # type: () -> Object
            pass

        def distance(self, *args):
            # type: (*Any) -> float
            pass

        def distanceSq(self, *args):
            # type: (*Any) -> float
            pass

        def getX(self):
            # type: () -> float
            return self.x

        def getY(self):
            # type: () -> float
            return self.y

        def setLocation(self, x, y):
            # type: (float, float) -> None
            self.x = x
            self.y = y
