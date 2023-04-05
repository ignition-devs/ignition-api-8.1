from __future__ import print_function

__all__ = ["AttributeInfo", "ReadResult"]

from typing import Any, Iterator, List, Optional

from com.inductiveautomation.ignition.common.model.values import (
    QualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.model.types import (
    DataType,
    DataTypeClass,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class AttributeInfo(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(AttributeInfo, self).__init__()
        print(args)

    def getDesc(self):
        # type: () -> AnyStr
        pass

    def getId(self):
        # type: () -> int
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getType(self):
        # type: () -> DataType
        pass

    def setType(self, type_):
        # type: (DataType) -> None
        pass


class ReadResult(Object):
    def __init__(self, serviceResult=None):
        # type: (Optional[QualityCode]) -> None
        super(ReadResult, self).__init__()
        print(serviceResult)

    def getServiceResult(self):
        # type: () -> QualityCode
        pass

    def getTypeClass(self):
        # type: () -> DataTypeClass
        pass

    def getValues(self):
        # type: () -> List[QualifiedValue]
        pass

    def iterator(self):
        # type: () -> Iterator[QualifiedValue]
        pass

    def setServiceResult(self, serviceResult):
        # type: (QualityCode) -> None
        pass

    def setTypeClass(self, typeClass):
        # type: (DataTypeClass) -> None
        pass

    def setValues(self, values):
        # type: (List[QualifiedValue]) -> None
        pass

    def size(self):
        # type: () -> int
        pass
