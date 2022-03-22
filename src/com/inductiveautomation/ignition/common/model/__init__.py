__all__ = ["Version"]

import re

from java.lang import IllegalArgumentException, Object


class Version(Object):
    dev = True
    snapshot = False

    def __init__(self, major=0, minor=0, rev=0, build=0, beta=0, rc=0):
        self.major = major
        self.minor = minor
        self.rev = rev
        self.build = build
        self.beta = beta
        self.rc = rc

    def __eq__(self, other):
        return self._compare(other, True) == 0

    def __str__(self):
        return self.toString()

    def _compare(self, that, strict=False):
        this = self.toTuple(strict)
        that = that.toTuple(strict)
        return (this > that) - (this < that)

    def compareTo(self, that):
        return self._compare(that, True) if isinstance(that, type(self)) else None

    def exists(self):
        pass

    @staticmethod
    def fromXML(inputStream):
        pass

    def getBasicString(self):
        return (
            "{}.{}.{}-rc{}".format(self.major, self.minor, self.rev, self.rc)
            if self.rc > 0
            else "{}.{}.{}".format(self.major, self.minor, self.rev)
        )

    def getBeta(self):
        return self.beta

    def getBuildNumber(self):
        return self.build

    def getMajor(self):
        return self.major

    def getMinor(self):
        return self.minor

    def getRc(self):
        return self.rc

    def getRevision(self):
        return self.rev

    def getXML(self):
        pass

    def isDev(self):
        return self.dev

    def isFutureVersion(self, arg):
        cls = type(self)
        if isinstance(arg, basestring):
            that = self.parse(arg)
        elif isinstance(arg, cls):
            that = arg
        else:
            raise TypeError("isFutureVersion(): 1st arg can't be coerced to String.")

        return self._compare(that) == -1

    def isSnapshot(self):
        return self.snapshot

    @staticmethod
    def parse(s):
        sem_ver = [int(i) for i in re.findall(r"-?\d+", s)]
        if len(sem_ver) < 3:
            raise IllegalArgumentException('Invalid version: "{}"'.format(s))
        build_number = sem_ver[3] if len(sem_ver) == 4 else 0
        return Version(sem_ver[0], sem_ver[1], sem_ver[2], build_number)

    def toParseableString(self):
        return "{}.{}.{}.{}".format(self.major, self.minor, self.rev, self.build)

    def toString(self):
        if self.rc > 0:
            return "{}.{}.{}-rc{} (b{})".format(
                self.major, self.minor, self.rev, self.rc, self.build
            )
        if self.isSnapshot():
            return "{}.{}.{}-SNAPSHOT (b{})".format(
                self.major, self.minor, self.rev, self.build
            )
        if self.build is not None:
            return "{}.{}.{} (b{})".format(self.major, self.minor, self.rev, self.build)

        return "{}.{}.{}".format(self.major, self.minor, self.rev)

    def toTuple(self, strict=False):
        return (
            (self.major, self.minor, self.rev, self.build, self.beta, self.rc)
            if strict
            else (self.major, self.minor, self.rev)
        )
