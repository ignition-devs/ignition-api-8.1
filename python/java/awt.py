# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com


"""Contains all of the classes for creating user interfaces and for
painting graphics and images."""

__all__ = [
    'Color'
]

from java.lang import Object


class Color(Object):
    """The Color class is used to encapsulate colors in the default
    sRGB color space or colors in arbitrary color spaces identified by
    a ColorSpace. Every color has an implicit alpha value of 1.0 or an
    explicit one provided in the constructor. The alpha value defines
    the transparency of a color and can be represented by a float
    value in the range 0.0 - 1.0 or 0 - 255. An alpha value of 1.0 or
    255 means that the color is completely opaque and an alpha value
    of 0 or 0.0 means that the color is completely transparent. When
    constructing a Color with an explicit alpha or getting the
    color/alpha components of a Color, the color components are never
    premultiplied by the alpha component.

    The default color space for the Java 2D(tm) API is sRGB, a
    proposed standard RGB color space. For further information on
    sRGB, see http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html ."""

    def __init__(self, *args):
        print args
