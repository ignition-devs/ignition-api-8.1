from __future__ import print_function

__all__ = ["AbstractVisionPanel"]

from typing import Optional

from java.awt import LayoutManager
from javax.swing import JPanel


class AbstractVisionPanel(JPanel):
    def __init__(self, layout=None, isDoubleBuffered=None):
        # type: (Optional[LayoutManager], Optional[bool]) -> None
        super(AbstractVisionPanel, self).__init__()
        print(layout, isDoubleBuffered)
