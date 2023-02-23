__all__ = ["JTextComponent"]

from dev.thecesrom.helper.types import AnyStr
from java.awt import Container


class JTextComponent(Container):
    """JTextComponent is the base class for swing text components."""

    _text = "Text"  # type: AnyStr

    def getText(self, *args):
        # type: (*int) -> AnyStr
        return self._text

    def setText(self, t):
        # type: (AnyStr) -> None
        self._text = t
