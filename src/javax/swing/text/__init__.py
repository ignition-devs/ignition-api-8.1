# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

from java.awt import Container


class JTextComponent(Container):
    """JTextComponent is the base class for swing text components."""

    _text = 'Text'

    def getText(self):
        return self._text
