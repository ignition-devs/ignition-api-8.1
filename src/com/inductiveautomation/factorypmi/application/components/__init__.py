from __future__ import print_function

__all__ = ["BasicContainer"]

from typing import Optional

from com.inductiveautomation.vision.api.client.components.model import (
    AbstractVisionPanel,
)
from dev.thecesrom.helper.types import AnyStr


class BasicContainer(AbstractVisionPanel):
    def __init__(self, name=None):
        # type: (Optional[AnyStr]) -> None
        super(BasicContainer, self).__init__()
        print(name)
