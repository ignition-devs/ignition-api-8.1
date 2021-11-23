__all__ = [
    "AbstractScheduleModel",
    "BasicScheduleModel",
    "CompositeScheduleModel",
    "HolidayModel",
    "ScheduleAdjustment",
]

from java.lang import Object


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
    def __init__(self, name, date, repeatAnnually):
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def isRepeatedAnnually(self):
        return self.repeatAnnually


class ScheduleAdjustment(Object):
    def __init__(self):
        pass

    def contains(self, timestamp):
        pass

    def getEnd(self):
        pass

    def getNote(self):
        pass

    def getStart(self):
        pass

    def isAvailable(self):
        pass

    def setAvailable(self, available):
        pass

    def setEnd(self, end):
        pass

    def setNoe(self, note):
        pass

    def setStart(self, start):
        pass
