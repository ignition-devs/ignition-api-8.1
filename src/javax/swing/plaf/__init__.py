from java.awt import Component, Graphics
from java.lang import Object


class ComponentUI(Object):
    def __init__(self):
        # type: () -> None
        pass

    def contains(self, c, x, y):
        # type: (Component, int, int) -> bool
        pass

    def paint(self, g, c):
        # type: (Graphics, Component) -> None
        pass

    def update(self, g, c):
        # type: (Graphics, Component) -> None
        pass


class DesktopPaneUI(ComponentUI):
    def __init__(self):
        # type: () -> None
        pass
