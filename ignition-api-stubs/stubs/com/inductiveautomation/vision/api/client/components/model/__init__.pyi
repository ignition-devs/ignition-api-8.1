from typing import Optional

from java.awt import LayoutManager
from javax.swing import JPanel

class AbstractVisionPanel(JPanel):
    def __init__(
        self,
        layout: Optional[LayoutManager] = ...,
        isDoubleBuffered: Optional[bool] = ...,
    ) -> None: ...
