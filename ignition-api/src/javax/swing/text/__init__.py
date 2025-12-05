__all__ = ["JTextComponent"]

from typing import Union

from java.awt import Container


class JTextComponent(Container):
    """JTextComponent is the base class for swing text components."""

    _text = "Text"  # type: Union[str, unicode]

    def getText(self, *args):
        # type: (*int) -> Union[str, unicode]
        return self._text

    def setText(self, t):
        # type: (Union[str, unicode]) -> None
        self._text = t
