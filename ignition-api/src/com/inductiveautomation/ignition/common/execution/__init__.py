__all__ = ["ExecutionManager"]

from typing import Any, Optional, Union

from java.lang import Runnable
from java.util.concurrent import ScheduledFuture, TimeUnit


class ExecutionManager(object):
    def executeOnce(
        self,
        command,  # type: Runnable
        delay=None,  # type: Optional[long]
        unit=None,  # type: Optional[TimeUnit]
    ):
        # type: (...) -> Union[None, ScheduledFuture]
        raise NotImplementedError

    def register(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    def registerAtFixedRate(
        self,
        owner,  # type: Union[str, unicode]
        name,  # type: Union[str, unicode]
        command,  # type: Runnable
        rate,  # type: int
        unit,  # type: TimeUnit
    ):
        # type: (...) -> None
        raise NotImplementedError

    def registerAtFixedRateWithInitialDelay(
        self,
        owner,  # type: Union[str, unicode]
        name,  # type: Union[str, unicode]
        command,  # type: Runnable
        rate,  # type: int
        unit,  # type: TimeUnit
        initialDelay,  # type: int
    ):
        # type: (...) -> None
        raise NotImplementedError

    def registerWithInitialDelay(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    def scheduleWithFixedDelay(
        self,
        command,  # type: Runnable
        initialDelay,  # type: int
        delay,  # type: int
        unit,  # type: TimeUnit
    ):
        # type: (...) -> ScheduledFuture
        raise NotImplementedError

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError

    def unregister(self, owner, name, interrupt):
        # type: (Union[str, unicode], Union[str, unicode], bool) -> None
        pass

    def unregisterAll(self, owner):
        # type: (Union[str, unicode]) -> None
        pass
