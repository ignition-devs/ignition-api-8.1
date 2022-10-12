from __future__ import print_function

__all__ = ["SimplifiedTagPath"]

from com.inductiveautomation.ignition.common.tags.paths import AbstractTagPath


class SimplifiedTagPath(AbstractTagPath):
    def __init__(self, delegate):
        print(delegate)
