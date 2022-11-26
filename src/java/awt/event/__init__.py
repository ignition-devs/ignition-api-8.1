from __future__ import print_function

__all__ = ["ActionEvent", "ComponentEvent", "MouseEvent"]

from typing import Any

from java.awt import AWTEvent, Component, Point
from java.lang import Object, String


class ActionEvent(AWTEvent):
    ACTION_FIRST = None  # type: int
    ACTION_LAST = None  # type: int
    ACTION_PERFORMED = None  # type: int
    ACTION_MASK = None  # type: int
    CTRL_MASK = None  # type: int
    META_MASK = None  # type: int
    SHIFT_MASK = None  # type: int

    def __init__(self, source, id, *args):
        # type: (Object, int, *Any) -> None
        print(args)
        super(ActionEvent, self).__init__(source, id)

    def getActionCommand(self):
        # type: () -> String
        pass

    def getModifiers(self):
        # type: () -> int
        pass

    def getWhen(self):
        # type: () -> long
        pass


class ComponentEvent(AWTEvent):
    COMPONENT_FIRST = None  # type: int
    COMPONENT_HIDDEN = None  # type: int
    COMPONENT_LAST = None  # type: int
    COMPONENT_MOVED = None  # type: int
    COMPONENT_RESIZED = None  # type: int
    COMPONENT_SHOWN = None  # type: int

    def __init__(self, source, id):
        # type: (Object, int) -> None
        super(ComponentEvent, self).__init__(source, id)

    def getComponent(self):
        # type: () -> Component
        pass


class InputEvent(ComponentEvent):
    ALT_DOWN_MASK = None  # type: int
    ALT_GRAPH_DOWN_MASK = None  # type: int
    ALT_GRAPH_MASL = None  # type: int
    ALT_MASK = None  # type: int
    BUTTON1_DOWN_MASK = None  # type: int
    BUTTOM1_MASK = None  # type: int
    BUTTON2_DOWN_MASK = None  # type: int
    BUTTON2_MASK = None  # type: int
    BUTTON3_DOWN_MASK = None  # type: int
    BUTTON3_MASK = None  # type: int
    CTRL_DOWN_MASK = None  # type: int
    CTRL_MASK = None  # type: int
    META_DOWN_MASK = None  # type: int
    META_MASK = None  # type: int
    SHIFT_DOWN_MASK = None  # type: int
    SHIFT_MASK = None  # type: int

    def consume(self):
        # type: () -> None
        pass

    @staticmethod
    def getMaskForButton(button):
        # type: (int) -> int
        pass

    def getModifiersEx(self):
        # type: () -> int
        pass

    @staticmethod
    def getModifiersExText(modifiers):
        # type: (int) -> String
        pass

    def getWhen(self):
        # type: () -> long
        pass

    def isAltDown(self):
        # type: () -> bool
        return True

    def isAltGraphDown(self):
        # type: () -> bool
        return True

    def isConsumed(self):
        # type: () -> bool
        return True

    def isControlDown(self):
        # type: () -> bool
        return True

    def isMetaDown(self):
        # type: () -> bool
        return True

    def isShiftDown(self):
        # type: () -> bool
        return True


class MouseEvent(InputEvent):
    BUTTON1 = None  # type: int
    BUTTON2 = None  # type: int
    BUTTON3 = None  # type: int
    MOUSE_CLICKED = None  # type: int
    MOUSE_DRAGGED = None  # type: int
    MOUSE_ENTERED = None  # type: int
    MOUSE_EXITED = None  # type: int
    MOUSE_FIRST = None  # type: int
    MOUSE_LAST = None  # type: int
    MOUSE_MOVED = None  # type: int
    MOUSE_PRESSED = None  # type: int
    MOUSE_RELEASED = None  # type: int
    MOUSE_WHEEL = None  # type: int
    NOBUTTON = None  # type: int

    def __init__(self, source, id, *args):
        # type: (Component, int, *Any) -> None
        print(args)
        super(MouseEvent, self).__init__(source, id)

    def getButton(self):
        # type: () -> int
        pass

    def getClickCount(self):
        # type: () -> int
        pass

    def getLocationOnScreen(self):
        # type: () -> Point
        pass

    @staticmethod
    def getMouseModifiersText(modifiers):
        # type: (int) -> String
        pass

    def getPoint(self):
        # type: () -> Point
        pass

    def getX(self):
        # type: () -> int
        pass

    def getXOnScreen(self):
        # type: () -> int
        pass

    def getY(self):
        # type: () -> int
        pass

    def getYOnScreen(self):
        # type: () -> int
        pass

    def isPopupTrigger(self):
        # type: () -> bool
        return True

    def translatePoint(self, x, y):
        # type: (int, int) -> None
        pass
