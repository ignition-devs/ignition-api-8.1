# Copyright (C) 2018-2021
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev

"""Provides classes and interfaces that deal with editable and
noneditable text components. Examples of text components are text fields
and text areas, of which password fields and document editors are
special instantiations. Features that are supported by this package
include selection/highlighting, editing, style, and key mapping.
"""

from java.awt import Container


class JTextComponent(Container):
    """JTextComponent is the base class for swing text components."""

    _text = "Text"

    def getText(self):
        """Returns the text contained in this TextComponent."""
        return self._text
