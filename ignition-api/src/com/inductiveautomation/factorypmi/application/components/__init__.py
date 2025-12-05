from __future__ import print_function

__all__ = ["BasicContainer"]

from typing import Union

from com.inductiveautomation.vision.api.client.components.model import (
    AbstractVisionPanel,
)


class BasicContainer(AbstractVisionPanel):
    def __init__(self, name=None):
        # type: (Union[str, unicode, None]) -> None
        super(BasicContainer, self).__init__()
        print(name)
