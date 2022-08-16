from __future__ import print_function

__all__ = ["BufferedImage"]

from typing import Any

from java.awt import Image


class BufferedImage(Image):
    def __init__(self, *args):
        # type: (Any) -> None
        print(args)
