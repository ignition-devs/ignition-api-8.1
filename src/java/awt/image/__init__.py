"""Provides classes for creating and modifying images.

Images are processed using a streaming framework that involves an image
producer, optional image filters, and an image consumer. This framework
makes it possible to progressively render an image while it is being
fetched and generated. Moreover, the framework allows an application to
discard the storage used by an image and to regenerate it at any time.
This package provides a number of image producers, consumers, and
filters that you can configure for your image processing needs.
"""

from __future__ import print_function

__all__ = ["BufferedImage"]

from typing import Any

from java.awt import Image


class BufferedImage(Image):
    """The BufferedImage subclass describes an Image with an accessible
    buffer of image data.

    A BufferedImage is comprised of a ColorModel and a Raster of image
    data. The number and types of bands in the SampleModel of the Raster
    must match the number and types required by the ColorModel to
    represent its color and alpha components. All BufferedImage objects
    have an upper left corner coordinate of (0, 0). Any Raster used to
    construct a BufferedImage must therefore have minX=0 and minY=0.

    This class relies on the data fetching and setting methods of
    Raster, and on the color characterization methods of ColorModel.
    """

    def __init__(self, *args):
        # type: (Any) -> None
        print(args)
