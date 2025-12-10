__all__ = ["ScheduleModel"]

from typing import Iterable, Union

from java.lang import Enum

from com.palantir.ptoss.cinch.core import DefaultBindableModel


class ScheduleModel(DefaultBindableModel):

    class DayOfWeek(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[ScheduleModel.DayOfWeek]
            pass

    def __init__(self):
        # type: () -> None
        super(ScheduleModel, self).__init__()

    def deselectDayOfWeek(self, day):
        # type: (ScheduleModel.DayOfWeek) -> None
        pass

    def getEveryHour(self):
        # type: () -> Union[str, unicode]
        pass

    def getHour(self):
        # type: () -> Union[str, unicode]
        pass

    def getMinute(self):
        # type: () -> Union[str, unicode]
        pass

    def getSelectedDays(self):
        # type: () -> Union[str, unicode]
        pass

    def isAlldays(self):
        # type: () -> bool
        return True

    def isDaySelected(self, day):
        # type: (ScheduleModel.DayOfWeek) -> bool
        return True

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
        # type: (Union[str, unicode]) -> None
        pass

    def setHour(self, hour):
        # type: (Union[str, unicode]) -> None
        pass

    def setHourEnabled(self, hourEnabled):
        # type: (bool) -> None
        pass

    def setMinute(self, minute):
        # type: (Union[str, unicode]) -> None
        pass

    def setMinuteEnabled(self, minuteEnabled):
        # type: (bool) -> None
        pass

    def setSelectedDays(self, selectedDays):
        # type: (Union[str, unicode]) -> None
        pass

    def toCronString(self):
        # type: () -> Union[str, unicode]
        pass
