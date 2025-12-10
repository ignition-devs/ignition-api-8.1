from typing import Union

from com.inductiveautomation.vision.api.client.components.model import (
    AbstractVisionPanel,
)

class BasicContainer(AbstractVisionPanel):
    def __init__(self, name: Union[str, unicode, None] = ...) -> None: ...
