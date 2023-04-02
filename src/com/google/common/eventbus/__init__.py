from __future__ import print_function

__all__ = ["EventBus"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class EventBus(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(EventBus, self).__init__()
        print(args)

    def identifier(self):
        # type: () -> AnyStr
        pass

    def post(self, event):
        # type: (Object) -> None
        pass

    def register(self, obj):
        # type: (Object) -> None
        pass

    def unregister(self, obj):
        # type: (Object) -> None
        pass
