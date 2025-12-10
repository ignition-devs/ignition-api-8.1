__all__ = [
    "AbstractScheduleModel",
    "BasicScheduleModel",
    "CompositeScheduleModel",
    "HolidayModel",
    "ScheduleAdjustment",
    "ScheduleRepeatStyle",
]

from typing import Iterable, List, Union

from java.lang import Enum
from java.util import Calendar, Date

from com.inductiveautomation.ignition.common.util import Timeline
from com.palantir.ptoss.cinch.core import DefaultBindableModel


class AbstractScheduleModel(DefaultBindableModel):
    def __init__(self):
        # type: () -> None
        super(AbstractScheduleModel, self).__init__()

    def getDescription(self):
        # type: () -> Union[str, unicode]
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getScheduleForDay(self, cal):
        # type: (Calendar) -> Timeline
        raise NotImplementedError

    def getType(self):
        # type: () -> Union[str, unicode]
        pass

    def isObserveHolidays(self):
        # type: () -> bool
        raise NotImplementedError

    def setDescription(self, description):
        # type: (Union[str, unicode]) -> None
        pass

    def setName(self, name):
        # type: (Union[str, unicode]) -> None
        pass

    def setObserveHolidays(self, observeHolidays):
        # type: (bool) -> None
        raise NotImplementedError


class BasicScheduleModel(AbstractScheduleModel):
    def __init__(self):
        # type: () -> None
        super(BasicScheduleModel, self).__init__()

    def getAllDayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getFridayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getMondayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getRepeat(self):
        # type: () -> ScheduleRepeatStyle
        pass

    def getRepeatOff(self):
        # type: () -> int
        pass

    def getRepeatOn(self):
        # type: () -> int
        pass

    def getSaturdayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getScheduleForDay(self, cal):
        # type: (Calendar) -> Timeline
        pass

    def getStartingAt(self):
        # type: () -> Date
        pass

    def getSundayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getThursdayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getTuesdayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getWednesdayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def getWeekDayTime(self):
        # type: () -> Union[str, unicode]
        pass

    def isAllDays(self):
        # type: () -> bool
        return True

    def isFriday(self):
        # type: () -> bool
        return True

    def isMonday(self):
        # type: () -> bool
        return True

    def isObserveHolidays(self):
        # type: () -> bool
        return True

    def isRepeating(self):
        # type: () -> bool
        return True

    def isSaturday(self):
        # type: () -> bool
        return True

    def isSunday(self):
        # type: () -> bool
        return True

    def isThursday(self):
        # type: () -> bool
        return True

    def isTuesday(self):
        # type: () -> bool
        return True

    def isUseDays(self):
        # type: () -> bool
        return True

    def isWednesday(self):
        # type: () -> bool
        return True

    def isWeekDays(self):
        # type: () -> bool
        return True

    def set(self, that):
        # type: (BasicScheduleModel) -> None
        pass

    def setAllDays(self, allDays):
        # type: (bool) -> None
        pass

    def setAllDayTime(self, allDayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setFriday(self, friday):
        # type: (bool) -> None
        pass

    def setFridayTime(self, fridayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setMonday(self, monday):
        # type: (bool) -> None
        pass

    def setMondayTime(self, mondayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setObserveHolidays(self, observeHolidays):
        # type: (bool) -> None
        pass

    def setRepeat(self, repeat):
        # type: (ScheduleRepeatStyle) -> None
        pass

    def setRepeatOff(self, repeatOff):
        # type: (int) -> None
        pass

    def setRepeatOn(self, repeatOn):
        # type: (int) -> None
        pass

    def setSaturday(self, saturday):
        # type: (bool) -> None
        pass

    def setSaturdayTime(self, saturdayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setStartingAt(self, startingAt):
        # type: (Date) -> None
        pass

    def setSunday(self, sunday):
        # type: (bool) -> None
        pass

    def setSundayTime(self, sundayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setThursday(self, thursday):
        # type: (bool) -> None
        pass

    def setThursdayTime(self, thursdayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setTuesday(self, tuesday):
        # type: (bool) -> None
        pass

    def setTuesdayTime(self, tuesdayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setWednesday(self, wednesday):
        # type: (bool) -> None
        pass

    def setWednesdayTime(self, wednesdayTime):
        # type: (Union[str, unicode]) -> None
        pass

    def setWeekDays(self, weekDays):
        # type: (bool) -> None
        pass

    def setWeekDayTime(self, weekDayTime):
        # type: (Union[str, unicode]) -> None
        pass


class CompositeScheduleModel(AbstractScheduleModel):
    def __init__(self, models):
        # type: (List[AbstractScheduleModel]) -> None
        super(CompositeScheduleModel, self).__init__()
        self._models = models

    def getModels(self):
        # type: () -> List[AbstractScheduleModel]
        return self._models

    def getScheduleForDay(self, cal):
        # type: (Calendar) -> Timeline
        pass

    def isObserveHolidays(self):
        # type: () -> bool
        return True

    def setObserveHolidays(self, observeHolidays):
        # type: (bool) -> None
        pass


class HolidayModel(DefaultBindableModel):
    date = None  # type: Date
    name = None  # type: Union[str, unicode]
    repeatAnnually = None  # type: bool

    def __init__(self, name, date, repeatAnnually):
        # type: (Union[str, unicode], Date, bool) -> None
        super(HolidayModel, self).__init__()
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        # type: () -> Date
        return self.date

    def getName(self):
        # type: () -> Union[str, unicode]
        return self.name

    def isRepeatAnnually(self):
        # type: () -> bool
        return self.repeatAnnually

    def set(self, that):
        # type: (HolidayModel) -> None
        pass

    def setDate(self, date):
        # type: (Date) -> None
        self.date = date

    def setName(self, name):
        # type: (Union[str, unicode]) -> None
        self.name = name

    def setRepeatAnnually(self, repeatAnnually):
        # type: (bool) -> None
        self.repeatAnnually = repeatAnnually


class ScheduleAdjustment(DefaultBindableModel):
    start = None  # type: Date
    end = None  # type: Date
    available = None  # type: bool
    note = None  # type: Union[str, unicode]

    def __init__(self, start, end, available, note):
        # type: (Date, Date, bool, Union[str, unicode]) -> None
        super(ScheduleAdjustment, self).__init__()
        self.start = start
        self.end = end
        self.available = available
        self.note = note

    def contains(self, timestamp):
        # type: (long) -> bool
        return True

    def getEnd(self):
        # type: () -> Date
        return self.end

    def getNote(self):
        # type: () -> Union[str, unicode]
        return self.note

    def getStart(self):
        # type: () -> Date
        return self.start

    def isAvailable(self):
        # type: () -> bool
        return self.available

    def setAvailable(self, available):
        # type: (bool) -> None
        self.available = available

    def setEnd(self, end):
        # type: (Date) -> None
        self.end = end

    def setNote(self, note):
        # type: (Union[str, unicode]) -> None
        self.note = note

    def setStart(self, start):
        # type: (Date) -> None
        self.start = start


class ScheduleRepeatStyle(Enum):
    @staticmethod
    def values():
        # type: () -> Iterable[ScheduleRepeatStyle]
        pass
