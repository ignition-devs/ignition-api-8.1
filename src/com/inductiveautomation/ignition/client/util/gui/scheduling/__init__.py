__all__ = ["ScheduleModel"]

from typing import Iterable

from com.palantir.ptoss.cinch.core import DefaultBindableModel
from dev.coatl.helper.types import AnyStr
from java.lang import Enum


class ScheduleModel(DefaultBindableModel):
    def __init__(self):
        # type: () -> None
        super(ScheduleModel, self).__init__()

    def deselectDayOfWeek(self, day):
        # type: (ScheduleModel.DayOfWeek) -> None
        pass

    def getEveryHour(self):
        # type: () -> AnyStr
        pass

    def getHour(self):
        # type: () -> AnyStr
        pass

    def getMinute(self):
        # type: () -> AnyStr
        pass

    def getSelectedDays(self):
        # type: () -> AnyStr
        pass

    def isAlldays(self):
        # type: () -> bool
        return True

    def isDaySelected(self, day):
        # type: (ScheduleModel.DayOfWeek) -> bool
        pass

    def isEveryHourEnabled(self):
        # type: () -> bool
        return True

    def isEveryMinuteEnabled(self):
        # type: () -> bool
        return True

    def isHourEnabled(self):
        # type: () -> bool
        return True

    def isMinuteEnabled(self):
        # type: () -> bool
        return True

    def selectDayOfWeek(self, day):
        # type: (ScheduleModel.DayOfWeek) -> None
        pass

    def setAllDays(self, allDays):
        # type: (bool) -> None
        pass

    def setEveryHour(self, everyHour):
        # type: (AnyStr) -> None
        pass

    def setHour(self, hour):
        # type: (AnyStr) -> None
        pass

    def setHourEnabled(self, hourEnabled):
        # type: (bool) -> None
        pass

    def setMinute(self, minute):
        # type: (AnyStr) -> None
        pass

    def setMinuteEnabled(self, minuteEnabled):
        # type: (bool) -> None
        pass

    def setSelectedDays(self, selectedDays):
        # type: (AnyStr) -> None
        pass

    def toCronString(self):
        # type: () -> AnyStr
        pass

    class DayOfWeek(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[ScheduleModel.DayOfWeek]
            pass
