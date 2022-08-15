__all__ = [
    "AbstractScheduleModel",
    "BasicScheduleModel",
    "CompositeScheduleModel",
    "HolidayModel",
    "ScheduleAdjustment",
]

from java.lang import Object, String
from java.util import Date


class AbstractScheduleModel(Object):
    def getScheduleForDay(self, cal):
        pass

    def getType(self):
        pass

    def isObserveHolidays(self):
        pass

    def setObserveHolidays(self, observeHolidays):
        pass


class BasicScheduleModel(AbstractScheduleModel):
    def getAllDayTime(self):
        pass

    def getFridayTime(self):
        pass

    def getMondayTime(self):
        pass

    def getRepeat(self):
        pass

    def getRepeatOff(self):
        pass

    def getRepeatOn(self):
        pass

    def getSaturdayTime(self):
        pass

    def getStartingAt(self):
        pass

    def getSundayTime(self):
        pass

    def getThursdayTime(self):
        pass

    def getTuesdayTime(self):
        pass

    def getWednesdayTime(self):
        pass

    def getWeekDayTime(self):
        pass

    def isAllDays(self):
        pass

    def isFriday(self):
        pass

    def isMonday(self):
        pass

    def isRepeating(self):
        pass

    def isSaturday(self):
        pass

    def isSunday(self):
        pass

    def isThursday(self):
        pass

    def isTuesday(self):
        pass

    def isUseDays(self):
        pass

    def isWednesday(self):
        pass

    def isWeekDays(self):
        pass

    def set(self, that):
        pass

    def setAllDays(self, allDays):
        pass

    def setAllDayTime(self, allDayTime):
        pass

    def setFriday(self, friday):
        pass

    def setFridayTime(self, fridayTime):
        pass

    def setMonday(self, monday):
        pass

    def setMondayTime(self, mondayTime):
        pass

    def setRepeat(self, repeat):
        pass

    def setRepeatOff(self, repeatOff):
        pass

    def setRepeatOn(self, repeatOn):
        pass

    def setSaturday(self, saturday):
        pass

    def setSaturdayTime(self, saturdayTime):
        pass

    def setStartingAt(self, startingAt):
        pass

    def setSunday(self, sunday):
        pass

    def setSundayTime(self, sundayTime):
        pass

    def setThursday(self, thursday):
        pass

    def setThursdayTime(self, thursdayTime):
        pass

    def setTuesday(self, tuesday):
        pass

    def setTuesdayTime(self, tuesdayTime):
        pass

    def setWednesday(self, wednesday):
        pass

    def setWednesdayTime(self, wednesdayTime):
        pass

    def setWeekDays(self, weekDays):
        pass

    def setWeekDayTime(self, weekDayTime):
        pass


class CompositeScheduleModel(AbstractScheduleModel):
    def getModels(self):
        pass


class HolidayModel(Object):
    date = None  # type: Date
    name = None  # type: String
    repeatAnnually = None  # type: bool

    def __init__(self, name, date, repeatAnnually):
        # type: (String, Date, bool) -> None
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        # type: () -> Date
        return self.date

    def getName(self):
        # type: () -> String
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
        # type: (String) -> None
        self.name = name

    def setRepeatAnnually(self, repeatAnnually):
        # type: (bool) -> None
        self.repeatAnnually = repeatAnnually


class ScheduleAdjustment(Object):
    start = None  # type: Date
    end = None  # type: Date
    available = None  # type: bool
    note = None  # type: String

    def __init__(self, start, end, available, note):
        # type: (Date, Date, bool, String) -> None
        self.start = start
        self.end = end
        self.available = available
        self.note = note

    def contains(self, timestamp):
        # type: (long) -> bool
        pass

    def getEnd(self):
        # type: () -> Date
        return self.end

    def getNote(self):
        # type: () -> String
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
        # type: (String) -> None
        self.note = note

    def setStart(self, start):
        # type: (Date) -> None
        self.start = start
