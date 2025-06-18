__all__ = ["Animator"]

from java.lang import Object


class Animator(Object):
    def cancel(self):
        # type: () -> bool
        return True

    def pause(self):
        # type: () -> None
        pass

    def resume(self):
        # type: () -> None
        pass
