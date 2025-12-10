__all__ = ["Binding", "DefaultBindableModel"]

from typing import Any

from java.lang import Object


class Binding(object):
    def update(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError


class DefaultBindableModel(Object):
    def __init__(self):
        # type: () -> None
        super(DefaultBindableModel, self).__init__()

    def bind(self, toBind):
        # type: (Binding) -> None
        pass

    def modelUpdated(self, *args):
        # type: (*Any) -> None
        pass

    def unbind(self, toUnbind):
        # type: (Binding) -> None
        pass

    def unbindAll(self):
        # type: () -> None
        pass

    def update(self):
        # type: () -> None
        pass
