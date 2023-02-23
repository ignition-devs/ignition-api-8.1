from __future__ import print_function

__all__ = [
    "AWTEvent",
    "Color",
    "Component",
    "Container",
    "Dimension",
    "Frame",
    "Graphics",
    "GridLayout",
    "Image",
    "LayoutManager",
    "Point",
    "Toolkit",
    "Window",
]

from typing import Any, Optional

from dev.thecesrom.helper.types import AnyStr
from java.awt.geom import Dimension2D, Point2D
from java.lang import Object
from java.util import EventObject


class LayoutManager(object):
    def addLayoutComponent(self, name, comp):
        # type: (AnyStr, Component) -> None
        raise NotImplementedError

    def layoutContainer(self, parent):
        # type: (Container) -> None
        raise NotImplementedError

    def minimumLayoutSize(self, parent):
        # type: (Container) -> Dimension
        raise NotImplementedError

    def preferredLayoutSize(self, parent):
        # type: (Container) -> Dimension
        raise NotImplementedError

    def removeLayoutComponent(self, comp):
        # type: (Component) -> None
        raise NotImplementedError


class AWTEvent(EventObject):
    _id = None  # type: int

    def __init__(self, source, id):
        # type: (Object, int) -> None
        super(AWTEvent, self).__init__(source)
        self._id = id

    def getID(self):
        # type: () -> int
        return self._id

    def paramString(self):
        # type: () -> AnyStr
        pass

    def setSource(self, newSource):
        # type: (Object) -> None
        pass


class Color(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Color, self).__init__()
        print(args)


class Component(Object):
    def imageUpdate(
        self,
        img,  # type: Image
        infoflags,  # type: int
        x,  # type: int
        y,  # type: int
        width,  # type: int
        height,  # type: int
    ):
        # type: (...) -> bool
        return True


class Container(Component):
    def add(self, *args):
        # type: (*Any) -> Optional[Component]
        pass


class Dimension(Dimension2D):
    height = None  # type: int
    width = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Dimension, self).__init__()
        print(args)

    def getHeight(self):
        # type: () -> float
        pass

    def getSize(self):
        # type: () -> Dimension
        pass

    def getWidth(self):
        # type: () -> float
        pass

    def setSize(self, *args):
        # type: (*Any) -> None
        pass


class Image(Object):
    def flush(self):
        # type: () -> None
        pass

    def getAccelerationPriority(self):
        # type: () -> float
        pass

    def setAccelerationPriority(self, priority):
        # type: (float) -> None
        pass


class Point(Point2D):
    x = 0
    y = 0

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Point, self).__init__()
        print(args)

    def getLocation(self):
        # type: () -> Point
        pass

    def getX(self):
        # type: () -> float
        pass

    def getY(self):
        # type: () -> float
        pass

    def move(self, x, y):
        # type: (int, int) -> None
        pass

    def setLocation(self, *args):
        # type: (*Any) -> None
        pass

    def translate(self, dx, dy):
        # type: (int, int) -> None
        pass


class Toolkit(Object):
    def __init__(self):
        # type: () -> None
        super(Toolkit, self).__init__()

    def beep(self):
        # type: () -> None
        print(self, "Beep!")

    @staticmethod
    def getDefaultToolkit():
        # type: () -> Toolkit
        return Toolkit()


class Window(Container):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Window, self).__init__()


class Frame(Window):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Frame, self).__init__(*args)


class Graphics(Object):
    def create(self):
        # type: () -> Graphics
        raise NotImplementedError


class GridLayout(Object, LayoutManager):
    def __init__(
        self,
        rows=None,  # type: Optional[int]
        cols=None,  # type: Optional[int]
        hgap=None,  # type: Optional[int]
        vgap=None,  # type: Optional[int]
    ):
        # type: (...) -> None
        super(GridLayout, self).__init__()
        print(rows, cols, hgap, vgap)

    def addLayoutComponent(self, name, comp):
        # type: (AnyStr, Component) -> None
        pass

    def getColumns(self):
        # type: () -> int
        pass

    def getHgap(self):
        # type: () -> int
        pass

    def getRows(self):
        # type: () -> int
        pass

    def getVgap(self):
        # type: () -> int
        pass

    def layoutContainer(self, parent):
        # type: (Container) -> None
        pass

    def minimumLayoutSize(self, parent):
        # type: (Container) -> Dimension
        pass

    def preferredLayoutSize(self, parent):
        # type: (Container) -> Dimension
        pass

    def removeLayoutComponent(self, comp):
        # type: (Component) -> None
        pass

    def setColumns(self, cols):
        # type: (int) -> None
        pass

    def setHgap(self, hgap):
        # type: (int) -> None
        pass

    def setRows(self, rows):
        # type: (int) -> None
        pass

    def setVgap(self, vgap):
        # type: (int) -> None
        pass
