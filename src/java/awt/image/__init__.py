from __future__ import print_function

__all__ = ["BufferedImage", "ImageObserver"]

from typing import Any

from java.awt import Image


class ImageObserver(object):
    def imageUpdate(
        self,
        img,  # type: Image
        infoflags,  # type: int
        x,  # type: int
        y,  # type: int
        width,  # type: int
        height,  # type: int
    ):
        # type: (...) -> bool
        raise NotImplementedError


class BufferedImage(Image):
    def __init__(self, *args):
        # type: (Any) -> None
        print(args)
