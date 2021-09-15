__all__ = ["Version"]

import re

from java.lang import Object


class Version(Object):
    dev = True
    snapshot = False

    def __init__(self, major=0, minor=0, rev=0, build=0, beta=0, rc=0):
        """Version initializer.

        Args:
            major (int): Major number.
            minor (int): Minor number.
            rev (int): Revision number.
            build (int): Build number.
            beta (int): Beta number.
            rc (int): Release Candidate number.
        """
        self.major = major
        self.minor = minor
        self.rev = rev
        self.build = build
        self.beta = beta
        self.rc = rc

    def __eq__(self, other, strict=False):
        ret = 0
        version_1 = [self.major, self.minor, self.rev]
        version_2 = [other.major, other.minor, other.rev]

        if strict:
            version_1.append(self.build)
            version_1.append(self.beta)
            version_1.append(self.rc)
            version_2.append(other.build)
            version_2.append(other.beta)
            version_2.append(other.rc)

        for i in range(max(len(version_1), len(version_2))):
            v_1 = version_1[i] if i < len(version_1) else 0
            v_2 = version_2[i] if i < len(version_2) else 0
            if v_1 > v_2:
                ret = 1
            elif v_1 < v_2:
                ret = -1
        return ret

    def __str__(self):
        return self.toString()

    def compareTo(self, that):
        """Compares two Versions.

        Note that this comparison is stricter than we want for Gateway
        restores or project imports. For those, isFutureVersion().

        Args:
            that (Version): The version to compare.

        Returns:
             int: 0 if self and that are equal, -1 if that is greater
                than self, or 1 if self is greater than that.
        """
        return self.__eq__(that, True)

    def exists(self):
        pass

    @staticmethod
    def fromXML(inputStream):
        pass

    def getBasicString(self):
        if self.rc > 0:
            ret = "{}.{}.{}-rc{}".format(
                self.major, self.minor, self.rev, self.rc
            )
        else:
            ret = "{}.{}.{}".format(self.major, self.minor, self.rev)
        return ret

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
        other = self.parse(arg)
        return self.__eq__(other) == -1

    def isSnapshot(self):
        return self.snapshot

    @staticmethod
    def parse(s):
        sem_ver = [int(i) for i in re.findall(r"-?\d+", s)]
        return Version(sem_ver[0], sem_ver[1], sem_ver[2])

    def toParseableString(self):
        """Returns the version as a compact, parseable (non-XML) string
        that can be parsed with the 1-string constructor of this class.

        Returns:
            string: Compact, parseable (non-XML) string.
        """
        return "{}.{}.{}.{}".format(
            self.major, self.minor, self.rev, self.build
        )

    def toString(self):
        if self.rc > 0:
            version = "{}.{}.{}-rc{} (b{})".format(
                self.major, self.minor, self.rev, self.rc, self.build
            )
        elif self.isSnapshot():
            version = "{}.{}.{}-SNAPSHOT (b{})".format(
                self.major, self.minor, self.rev, self.build
            )
        elif self.build is not None:
            version = "{}.{}.{} (b{})".format(
                self.major, self.minor, self.rev, self.build
            )
        else:
            version = "{}.{}.{}".format(self.major, self.minor, self.rev)
        return version
