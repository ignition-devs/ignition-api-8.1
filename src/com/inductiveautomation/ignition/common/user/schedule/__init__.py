__all__ = ["HolidayModel", "ScheduleAdjustment"]

from java.lang import Object


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
