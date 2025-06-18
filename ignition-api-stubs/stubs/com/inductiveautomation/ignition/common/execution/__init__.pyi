from typing import Any, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Runnable
from java.util.concurrent import ScheduledFuture, TimeUnit

class ExecutionManager:
    def executeOnce(
        self,
        command: Runnable,
        delay: Optional[long] = ...,
        unit: Optional[TimeUnit] = ...,
    ) -> Union[None, ScheduledFuture]: ...
    def register(self, *args: Any) -> None: ...
    def registerAtFixedRate(
        self, owner: AnyStr, name: AnyStr, command: Runnable, rate: int, unit: TimeUnit
    ) -> None: ...
    def registerAtFixedRateWithInitialDelay(
        self,
        owner: AnyStr,
        name: AnyStr,
        command: Runnable,
        rate: int,
        unit: TimeUnit,
        initialDelay: int,
    ) -> None: ...
    def registerWithInitialDelay(self, *args: Any) -> None: ...
    def scheduleWithFixedDelay(
        self, command: Runnable, initialDelay: int, delay: int, unit: TimeUnit
    ) -> ScheduledFuture: ...
    def shutdown(self) -> None: ...
    def unregister(self, owner: AnyStr, name: AnyStr, interrupt: bool) -> None: ...
    def unregisterAll(self, owner: AnyStr) -> None: ...
