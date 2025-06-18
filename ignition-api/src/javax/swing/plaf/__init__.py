__all__ = ["ComponentUI", "DesktopPaneUI"]

from java.awt import Component, Graphics
from java.lang import Object


class ComponentUI(Object):
    def __init__(self):
        # type: () -> None
        super(ComponentUI, self).__init__()

    def contains(self, c, x, y):
        # type: (Component, int, int) -> bool
        return True

    def paint(self, g, c):
        # type: (Graphics, Component) -> None
        pass

    def update(self, g, c):
        # type: (Graphics, Component) -> None
        pass


class DesktopPaneUI(ComponentUI):
    def __init__(self):
        # type: () -> None
        super(DesktopPaneUI, self).__init__()
