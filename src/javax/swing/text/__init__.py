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

    def setText(self, t):
        """Sets the text of this TextComponent to the specified text.
        If the text is null or empty, has the effect of simply deleting
        the old text. When text has been inserted, the resulting caret
        location is determined by the implementation of the caret class.

        Args:
            t (str): The new text to be set.
        """
        self._text = t
