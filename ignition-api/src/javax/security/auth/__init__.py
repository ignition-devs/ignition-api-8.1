from __future__ import print_function

__all__ = ["Subject"]

from typing import Any

from java.lang import Object


class Subject(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Subject, self).__init__()
        print(args)
