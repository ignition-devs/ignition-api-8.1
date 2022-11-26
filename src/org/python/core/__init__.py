from __future__ import print_function

from copy import PyStringMap

__all__ = [
    "CodeFlag",
    "CompilerFlags",
    "PyBaseCode",
    "PyBuiltinCallable",
    "PyBuiltinMethod",
    "PyCell",
    "PyCode",
    "PyDescriptor",
    "PyException",
    "PyFrame",
    "PyFunction",
    "PyInteger",
    "PyList",
    "PyMethodDescr",
    "PyNewWrapper",
    "PyObject",
    "PySequence",
    "PySequenceList",
    "PyString",
    "PyStringMap",
    "PyTraceback",
    "PyTuple",
    "PyType",
    "TraceFunction",
    "Visitproc",
]

from typing import Any, Iterable, Iterator, List, Optional, Tuple, Union

from enum import Enum

import java.util
from java.io import PrintWriter
from java.lang import Class, Object, RuntimeException, String, StringBuilder, Throwable
from org.python.expose import TypeBuilder


class PyObject(Object):
    """All objects known to the Jython runtime system are represented by
    an instance of the class PyObject or one of its subclasses.
    """

    gcMonitorGlobal = None  # type: bool
    TYPE = None  # type: PyType

    def __init__(self, objtype=None):
        # type: (Optional[PyType]) -> None
        print(objtype)

    def __abs__(self):
        # type: () -> PyObject
        pass

    def __add__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __and__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __call__(self, *args, **kwargs):
        # type: (*Any, **Any) -> PyObject
        pass

    def __coerce__(self, pyo):
        # type: (PyObject) -> PyObject
        pass

    def __coerce_ex__(self, o):
        # type: (PyObject) -> Object
        pass

    def __complex__(self):
        # type: () -> complex
        pass

    def __contains__(self, o):
        # type: (PyObject) -> bool
        return True

    def __delete__(self, obj):
        # type: (PyObject) -> None
        pass

    def __delitem__(self, key):
        # type: (PyObject) -> None
        pass

    def __delslice__(self, start, stop, step=None):
        # type: (PyObject, PyObject, Optional[PyObject]) -> None
        pass

    def __dir__(self):
        # type: () -> PyObject
        pass

    def __div__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ensure_finalizer__(self):
        # type: () -> None
        pass

    def __findattr__(self, name):
        # type: (str) -> PyObject
        pass

    def __findattr_ex__(self, name):
        # type: (str) -> PyObject
        pass

    def __finditem__(self, key):
        # type: (str) -> PyObject
        pass

    def __float__(self):
        # type: () -> float
        pass

    def __floordiv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __get__(self, obj, type):
        # type: (PyObject, PyObject) -> PyObject
        pass

    def __getattr__(self, name):
        # type: (str) -> PyObject
        pass

    def __getitem__(self, key):
        # type: (Union[int, PyObject]) -> PyObject
        pass

    def __getnewargs__(self):
        # type: () -> Tuple[Any, ...]
        pass

    def __getslice__(self, start, stop, step=None):
        # type: (PyObject, PyObject, Optional[PyObject]) -> None
        pass

    def __hex__(self):
        # type: () -> str
        pass

    def __iadd__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __iand__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __idiv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __idivmod__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ifloordiv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ilshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __imod__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __imul__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __index__(self):
        # type: () -> PyObject
        pass

    def __int__(self):
        # type: () -> PyObject
        pass

    def __invert__(self):
        # type: () -> PyObject
        pass

    def __ior__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ipow__(self, other, dummy=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def __irshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __isub__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __iter__(self):
        # type: () -> Iterator[Any]
        pass

    def __iternext__(self):
        # type: () -> PyObject
        pass

    def __itruediv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ixor__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __le__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __long__(self):
        # type: () -> PyObject
        pass

    def __lshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __mod__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __mul__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __neg__(self):
        # type: () -> PyObject
        pass

    def __nonzero__(self):
        # type: () -> PyObject
        pass

    def __not__(self):
        # type: () -> PyObject
        pass

    def __oct__(self):
        # type: () -> PyObject
        pass

    def __or__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __pos__(self):
        # type: () -> PyObject
        pass

    def __pow__(self, o2, o3=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def __radd__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rand__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rdiv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rdivmod__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rfloordiv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rlshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rmod__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rmul__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __ror__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rpow__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rrshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rshift__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rsub__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rtruediv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rxor__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __set__(self, obj, value):
        # type: (PyObject, PyObject) -> None
        pass

    def __setitem__(self, key, value):
        # type: (Union[int, PyObject, str], PyObject) -> None
        pass

    def __setslice__(self, *args):
        # type: (*Any) -> None
        pass

    def __sub__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __tojava__(self, c):
        # type: (Class) -> Object
        pass

    def __truediv__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __trunc__(self):
        # type: () -> PyObject
        pass

    def __unicode__(self):
        # type: () -> unicode
        pass

    def __xor__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def _add(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _and(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _callextra(self, *args, **kwargs):
        # type: (*Any, **Any) -> PyObject
        pass

    def _cmp(self, o):
        # type: (PyObject) -> int
        pass

    def _div(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _divmod(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _doget(self, *args):
        # type: (*Any) -> PyObject
        pass

    def _doset(self, *args):
        # type: (*Any) -> Union[bool, PyObject]
        pass

    def _eq(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _floordiv(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ge(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _gt(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _iadd(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _iand(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _idiv(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _idivmod(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ifloordiv(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ilshift(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _imod(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _imul(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _in(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _ior(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ipow(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _irshift(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _is(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _isnot(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _isub(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _itruediv(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ixor(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _jcall(self, *args):
        # type: (*Any) -> PyObject
        pass

    def _jcallexc(self, *args):
        # type: (*Any) -> PyObject
        pass

    def _jthrow(self, t):
        # type: (Throwable) -> None
        pass

    def _le(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _lshift(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _lt(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _mod(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _mul(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _ne(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _notin(self, o):
        # type: (PyObject) -> PyObject
        pass

    def _or(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _pow(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _rshift(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _sub(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _truediv(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def _xor(self, o2):
        # type: (PyObject) -> PyObject
        pass

    def asDouble(self):
        # type: () -> float
        pass

    def asIndex(self, err=None):
        # type: (Optional[PyObject]) -> int
        pass

    def asInt(self, index=None):
        # type: (Optional[int]) -> int
        pass

    def asIterable(self):
        # type: () -> Iterable[PyObject]
        pass

    def asLong(self, index=None):
        # type: (Optional[int]) -> long
        pass

    def asName(self, arg):
        # type: (Union[int, PyObject]) -> String
        pass

    def asString(self, index=None):
        # type: (Optional[int]) -> String
        pass

    def asStringOrNull(self, index=None):
        # type: (Optional[int]) -> String
        pass

    def bit_length(self):
        # type: () -> int
        pass

    def conjugate(self):
        # type: () -> PyObject
        pass

    def delDict(self):
        # type: () -> None
        pass

    def delType(self):
        # type: () -> None
        pass

    def dispatch__init__(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def fastGetClass(self):
        # type: () -> PyObject
        pass

    def fastGetDict(self):
        # type: () -> PyObject
        pass

    def getDict(self):
        # type: () -> PyObject
        pass

    def getType(self):
        # type: () -> PyType
        pass

    def implementsDescrDelete(self):
        # type: () -> bool
        return True

    def implementsDescrGet(self):
        # type: () -> bool
        return True

    def implementsDescrSet(self):
        # type: () -> bool
        return True

    def invoke(self, *args, **kwargs):
        # type: (*Any, **Any) -> PyObject
        pass

    def isCallable(self):
        # type: () -> bool
        return True

    def isDataDescr(self):
        # type: () -> bool
        return True

    def isIndex(self):
        # type: () -> bool
        return True

    def isInteger(self):
        # type: () -> bool
        return True

    def isMappingType(self):
        # type: () -> bool
        return True

    def isNumberType(self):
        # type: () -> bool
        return True

    def isSequenceType(self):
        # type: () -> bool
        return True

    def noAttributeError(self, name):
        # type: (String) -> None
        pass

    @staticmethod
    def object___subclasshook__(type, subclass):
        # type: (PyType, PyObject) -> PyObject
        pass

    def readonlyAttributeError(self, name):
        # type: (String) -> None
        pass

    def setDict(self, newDict):
        # type: (PyObject) -> None
        pass

    def setType(self, type):
        # type: (PyType) -> None
        pass


class CodeFlag(Enum):
    CO_FUTURE_ABSOLUTE_IMPORT = 16384
    CO_FUTURE_DIVISION = 8192
    CO_FUTURE_PRINT_FUNCTION = 65536
    CO_FUTURE_UNICODE_LITERALS = 131072
    CO_FUTURE_WITH_STATEMENT = 32768
    CO_GENERATOR = 32
    CO_GENERATOR_ALLOWED = 4096
    CO_NESTED = 16
    CO_NEWLOCALS = 2
    CO_OPTIMIZED = 1
    CO_VARARGS = 4
    CO_VARKEYWORDS = 8
    flag = None  # type: int

    def isFlagBitSetIn(self, flags):
        # type: (int) -> bool
        return True

    @staticmethod
    def valueOf(name):
        # type: (String) -> CodeFlag
        pass

    @staticmethod
    def values():
        # type: () -> List[CodeFlag]
        pass


class CompilerFlags(Object):
    dont_imply_dedent = None  # type: bool
    encoding = None  # type: String
    only_ast = None  # type: bool
    PyCF_DONT_IMPLY_DEDENT = 512  # type: int
    PyCF_ONLY_AST = 1024  # type: int
    PyCF_SOURCE_IS_UTF8 = 256  # type: int
    source_is_utf8 = None  # type: bool

    def __init__(self, co_flags=None):
        # type: (Optional[int]) -> None
        print(co_flags)

    def combine(self, flags):
        # type: (Union[CompilerFlags, int]) -> CompilerFlags
        pass

    @staticmethod
    def getCompilerFlags(flags, frame):
        # type: (Union[CompilerFlags, int], PyFrame) -> CompilerFlags
        pass

    def isFlagSet(self, flag):
        # type: (CodeFlag) -> bool
        return True

    def toBits(self):
        # type: () -> int
        pass


class PyCode(PyObject):
    co_name = None  # type: String

    def call(self, *args):
        # type: (*Any) -> None
        pass


class PyBaseCode(PyCode):
    co_argcount = None  # type: int
    co_cellvars = None  # type: List[String]
    co_filename = None  # type: String
    co_firstlineno = None  # type: int
    co_flags = None  # type: CompilerFlags
    co_freevars = None  # type: List[String]
    co_nlocals = None  # type: int
    co_varnames = None  # type: List[String]
    jy_npurecell = None  # type: int
    varargs = None  # type: bool
    varkwargs = None  # type: bool

    def getCompilerFlags(self):
        # type: () -> CompilerFlags
        pass

    def hasFreevars(self):
        # type: () -> bool
        return True


class PyBuiltinCallable(PyObject):
    def bind(self, o):
        # type: (PyObject) -> PyBuiltinCallable
        raise NotImplementedError

    def fastGetName(self):
        # type: () -> PyObject
        pass

    def getDoc(self):
        # type: () -> String
        pass

    def getModule(self):
        # type: () -> PyObject
        pass

    def getSelf(self):
        # type: () -> PyObject
        pass

    def makeCall(self):
        # type: () -> PyObject
        pass

    def setInfo(self, info):
        # type: (PyBuiltinCallable.Info) -> None
        pass

    class Info(object):
        def getMaxargs(self):
            # type: () -> int
            raise NotImplementedError

        def getMinargs(self):
            # type: () -> int
            raise NotImplementedError

        def getName(self):
            # type: () -> String
            raise NotImplementedError

        def unexpectedCall(self, nargs, keywords):
            # type: (int, bool) -> PyException
            raise NotImplementedError


class PyBuiltinMethod(PyBuiltinCallable):
    def bind(self, o):
        # type: (PyObject) -> PyBuiltinCallable
        pass

    def makeDescriptor(self, t):
        # type: (PyType) -> PyMethodDescr
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyCell(PyObject):
    ob_ref = None  # type: PyObject

    def __init__(self):
        # type: () -> None
        super(PyCell, self).__init__()

    def getCellContents(self):
        # type: () -> PyObject
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyDescriptor(PyObject, PyBuiltinCallable.Info):
    def __init__(self, t, func):
        # type: (PyType, PyBuiltinCallable) -> None
        super(PyDescriptor, self).__init__(t)
        print(func)

    def getDoc(self):
        # type: () -> String
        pass

    def getMaxargs(self):
        # type: () -> int
        pass

    def getMinargs(self):
        # type: () -> int
        pass

    def getName(self):
        # type: () -> String
        pass

    def getObjClass(self):
        # type: () -> PyObject
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass

    def unexpectedCall(self, nargs, keywords):
        # type: (int, bool) -> PyException
        pass


class PyException(RuntimeException):
    traceback = None  # type: Optional[PyTraceback]
    type = None  # type: Optional[PyObject]
    value = None  # type: Optional[Union[PyObject, String]]

    def __init__(
        self,
        type_=None,  # type: Optional[PyObject]
        value=None,  # type: Optional[Union[PyObject, String]]
        traceback=None,  # type: Optional[PyTraceback]
    ):
        # type: (...) -> None
        super(PyException, self).__init__()
        self.type = type_
        self.value = value
        self.traceback = traceback

    @staticmethod
    def doRaise(type_, value, traceback):
        # type: (PyObject, PyObject, PyObject) -> PyException
        pass

    def exceptionClassName(self, obj):
        # type: (PyObject) -> String
        pass

    def isExceptionClass(self, obj):
        # type: (PyObject) -> bool
        return True

    def match(self, exc):
        # type: (PyObject) -> bool
        return True

    def normalize(self):
        # type: () -> None
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def super__printStackTrace(self, w):
        # type: (PrintWriter) -> None
        pass

    def tracebackHere(self, here, isFinally=None):
        # type: (PyFrame, Optional[bool]) -> None
        pass

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyFrame(PyObject):
    f_back = None  # type: PyFrame
    f_builtins = None  # type: PyObject
    f_code = None  # type: PyBaseCode
    f_env = None  # type: List[PyCell]
    f_exits = None  # type: List[PyObject]
    f_fastlocals = None  # type: List[PyObject]
    f_globals = None  # type: PyObject
    f_lasti = None  # type: int
    f_lineno = None  # type: int
    f_locals = None  # type: PyObject
    f_ncells = None  # type: int
    f_nfreevars = None  # type: int
    f_savedlocals = None  # type: List[Object]
    tracefunc = None  # type: TraceFunction

    def __init__(self, *args):
        # type: (*Any) -> None
        super(PyFrame, self).__init__()
        print(args)

    def checkGeneratorInput(self):
        # type: () -> Object
        pass

    def delglobal(self, index):
        # type: (String) -> None
        pass

    def dellocal(self, index):
        # type: (Union[int, String]) -> None
        pass

    def delTrace(self):
        # type: () -> None
        pass

    def getclosure(self, index):
        # type: (int) -> PyObject
        pass

    def getderef(self, index):
        # type: (int) -> PyObject
        pass

    def getf_locals(self):
        # type: () -> PyObject
        pass

    def getGeneratorInput(self):
        # type: () -> Object
        pass

    def getglobal(self, index):
        # type: (String) -> PyObject
        pass

    def getLine(self):
        # type: () -> int
        pass

    def getlocal(self, index):
        # type: (int) -> PyObject
        pass

    def getLocals(self):
        # type: () -> PyObject
        pass

    def getname(self, index):
        # type: (String) -> PyObject
        pass

    def getTrace(self):
        # type: () -> PyObject
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def setderef(self, index, value):
        # type: (int, PyObject) -> None
        pass

    def setglobal(self, index, value):
        # type: (String, PyObject) -> None
        pass

    def setline(self, line):
        # type: (int) -> None
        pass

    def setlocal(self, index, value):
        # type: (Union[int, String], PyObject) -> None
        pass

    def setTrace(self, trace):
        # type: (PyObject) -> None
        pass

    def to_cell(self, parm_index, env_index):
        # type: (int, int) -> None
        pass

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyFunction(PyObject):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(PyFunction, self).__init__()


class PyInteger(PyObject):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(PyInteger, self).__init__()


class PyMethodDescr(PyDescriptor):
    def __init__(self, t, func):
        # type: (PyType, PyBuiltinCallable) -> None
        super(PyMethodDescr, self).__init__(t, func)


class PyNewWrapper(PyBuiltinMethod):
    for_type = None  # type: PyType

    def __init__(self, *args):
        # type: (*Any) -> None
        super(PyNewWrapper, self).__init__()
        print(args)

    def getWrappedType(self):
        # type: () -> PyType
        pass

    def new_impl(self, init, subtype, *args, **kwargs):
        # type: (bool, PyType, *Any, **Any) -> PyObject
        raise NotImplementedError

    def setWrappedType(self, type_):
        # type: (PyType) -> None
        pass


class PySequence(PyObject):
    pass


class PySequenceList(PySequence):
    def add(self, *args):
        # type: (*Any) -> Optional[bool]
        raise NotImplementedError

    def addAll(self, *args):
        # type: (*Any) -> bool
        raise NotImplementedError

    def clear(self):
        # type: () -> None
        raise NotImplementedError

    def contains(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    def containsAll(self, c):
        # type: (java.util.Collection) -> bool
        raise NotImplementedError

    def get(self, index):
        # type: (int) -> Object
        raise NotImplementedError

    def getArray(self):
        # type: () -> List[PyObject]
        raise NotImplementedError

    def indexOf(self, o):
        # type: (Object) -> int
        raise NotImplementedError

    def isEmpty(self):
        # type: () -> bool
        raise NotImplementedError

    def iterator(self):
        # type: () -> java.util.Iterator
        raise NotImplementedError

    def lastIndexOf(self, o):
        # type: (Object) -> int
        raise NotImplementedError

    def listIterator(self, index=None):
        # type: (Optional[int]) -> java.util.ListIterator
        raise NotImplementedError

    def pyadd(self, *args):
        # type: (*Any) -> Optional[bool]
        raise NotImplementedError

    def pyget(self, index):
        # type: (int) -> PyObject
        raise NotImplementedError

    def pyset(self, index, element):
        # type: (int, PyObject) -> None
        raise NotImplementedError

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def remove(self, *args):
        # type: (*Any) -> Union[bool, None, Object]
        raise NotImplementedError

    def removeAll(self, c):
        # type: (java.util.Collection) -> bool
        raise NotImplementedError

    def retainAll(self, c):
        # type: (java.util.Collection) -> bool
        raise NotImplementedError

    def set(self, index, element):
        # type: (int, Object) -> Object
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError

    def subList(self, fromIndex, toIndex):
        # type: (int, int) -> List[PyObject]
        raise NotImplementedError

    def toArray(self, a=None):
        # type: (Optional[List[Object]]) -> List[Object]
        raise NotImplementedError

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyList(PySequenceList):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(PyList, self).__init__()

    def add(self, *args):
        # type: (*Any) -> Optional[bool]
        pass

    def addAll(self, *args):
        # type: (*Any) -> bool
        return True

    def append(self, o):
        # type: (PyObject) -> None
        pass

    def clear(self):
        # type: () -> None
        pass

    def contains(self, o):
        # type: (Object) -> bool
        return True

    def containsAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def count(self, o):
        # type: (PyObject) -> int
        pass

    def extend(self, o):
        # type: (PyObject) -> None
        pass

    @staticmethod
    def fromList(list_):
        # type: (List[PyObject]) -> PyList
        pass

    def get(self, index):
        # type: (int) -> Object
        pass

    def getArray(self):
        # type: () -> List[PyObject]
        pass

    def index(self, o, *args):
        # type: (PyObject, *int) -> int
        pass

    def indexOf(self, o):
        # type: (Object) -> int
        pass

    def insert(self, o):
        # type: (PyObject) -> None
        pass

    def isEmpty(self):
        # type: () -> bool
        return True

    def iterator(self):
        # type: () -> java.util.Iterator
        pass

    def lastIndexOf(self, o):
        # type: (Object) -> int
        pass

    def listIterator(self, index=None):
        # type: (Optional[int]) -> java.util.ListIterator
        pass

    def pyadd(self, *args):
        # type: (*Any) -> Optional[bool]
        pass

    def pyget(self, index):
        # type: (int) -> PyObject
        pass

    def pyset(self, index, element):
        # type: (int, PyObject) -> None
        pass

    def remove(self, *args):
        # type: (*Any) -> Union[bool, None, Object]
        pass

    def removeAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def retainAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def reverse(self):
        # type: () -> None
        pass

    def set(self, index, element):
        # type: (int, Object) -> Object
        pass

    def size(self):
        # type: () -> int
        pass

    def sort(self, *args):
        # type: (*PyObject) -> None
        pass

    def subList(self, fromIndex, toIndex):
        # type: (int, int) -> List[PyObject]
        pass

    def toArray(self, a=None):
        # type: (Optional[List[Object]]) -> List[Object]
        pass


class PyString(PyObject):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(PyString, self).__init__()


class PyTraceback(PyObject):
    tb_frame = None  # type: PyFrame
    tb_lineno = None  # type: int
    tb_next = None  # type: PyObject

    def __init__(self, next, frame):
        # type: (PyTraceback, PyFrame) -> None
        super(PyTraceback, self).__init__()
        print(next, frame)

    def dumpStack(self, buf=None):
        # type: (Optional[StringBuilder]) -> Optional[String]
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass


class PyTuple(PySequenceList):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(PyTuple, self).__init__()

    def add(self, *args):
        # type: (*Any) -> Optional[bool]
        pass

    def addAll(self, *args):
        # type: (*Any) -> bool
        return True

    def clear(self):
        # type: () -> None
        pass

    def contains(self, o):
        # type: (Object) -> bool
        return True

    def containsAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def count(self, value):
        # type: (PyObject) -> int
        pass

    @staticmethod
    def fromIterable(iterable):
        # type: (PyObject) -> PyTuple
        pass

    def get(self, index):
        # type: (int) -> Object
        pass

    def getArray(self):
        # type: () -> List[PyObject]
        pass

    def index(self, value, *args):
        # type: (PyObject, *int) -> int
        pass

    def indexOf(self, o):
        # type: (Object) -> int
        pass

    def isEmpty(self):
        # type: () -> bool
        return True

    def iterator(self):
        # type: () -> java.util.Iterator
        pass

    def lastIndexOf(self, o):
        # type: (Object) -> int
        pass

    def listIterator(self, index=None):
        # type: (Optional[int]) -> java.util.ListIterator
        pass

    def pyadd(self, *args):
        # type: (*Any) -> Optional[bool]
        pass

    def pyget(self, index):
        # type: (int) -> PyObject
        pass

    def pyset(self, index, element):
        # type: (int, PyObject) -> None
        pass

    def remove(self, *args):
        # type: (*Any) -> Union[bool, None, Object]
        pass

    def removeAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def retainAll(self, c):
        # type: (java.util.Collection) -> bool
        return True

    def set(self, index, element):
        # type: (int, Object) -> Object
        pass

    def size(self):
        # type: () -> int
        pass

    def subList(self, fromIndex, toIndex):
        # type: (int, int) -> List[PyObject]
        pass

    def toArray(self, a=None):
        # type: (Optional[List[Object]]) -> List[Object]
        pass

    def tuple___iter__(self):
        # type: () -> PyObject
        pass


class PyType(PyObject):
    @staticmethod
    def addBuilder(c, builder):
        # type: (Class, TypeBuilder) -> None
        pass

    def addMethod(self, meth):
        # type: (PyBuiltinMethod) -> None
        pass

    def compatibleForAssignment(self, other, attribute):
        # type: (PyType, String) -> None
        pass

    def delBases(self):
        # type: () -> None
        pass

    def delModule(self):
        # type: () -> None
        pass

    @staticmethod
    def ensureBootstrapped():
        # type: () -> bool
        return True

    @staticmethod
    def ensureDoc(arg):
        # type: (PyObject) -> None
        pass

    @staticmethod
    def ensureModule(arg):
        # type: (PyObject) -> None
        pass

    def fastGetName(self):
        # type: () -> String
        pass

    @staticmethod
    def fromClass(c, hardRef=False):
        # type: (Class, bool) -> PyType
        pass

    def getAbstractMethods(self):
        # type: () -> PyObject
        pass

    def getBase(self):
        # type: () -> PyObject
        pass

    def getBases(self):
        # type: () -> PyObject
        pass

    def getDoc(self):
        # type: () -> PyObject
        pass

    def getFlags(self):
        # type: () -> long
        pass

    def getModule(self):
        # type: () -> PyObject
        pass

    def getMro(self):
        # type: () -> Tuple[Any, ...]
        pass

    def getName(self):
        # type: () -> String
        pass

    def getNumSlots(self):
        # type: () -> int
        pass

    def getProxyType(self):
        # type: () -> Class
        pass

    def getStatic(self):
        # type: () -> PyObject
        pass

    def instDict(self):
        # type: () -> PyObject
        pass

    def isSubType(self, supertype):
        # type: (PyType) -> bool
        return True

    def lookup_where(self, name, where):
        # type: (String, List[PyObject]) -> PyObject
        pass

    def lookup(self, name):
        # type: (String) -> PyObject
        pass

    def needsFinalizer(self):
        # type: () -> bool
        return True

    @staticmethod
    def newType(
        new_,  # type: PyNewWrapper
        metatype,  # type: PyType
        name,  # type: String
        bases,  # type: Tuple[Any, ...]
        dict_,  # type: PyObject
    ):
        # type: (...) -> PyObject
        pass

    def pyDelName(self):
        # type: () -> None
        pass

    def pyGetName(self):
        # type: () -> PyObject
        pass

    def pySetName(self, name):
        # type: (PyObject) -> None
        pass

    def refersDirectlyTo(self, ob):
        # type: (PyObject) -> bool
        return True

    def removeMethod(self, meth):
        # type: (PyBuiltinMethod) -> None
        pass

    def setAbstractMethods(self, value):
        # type: (PyObject) -> None
        pass

    def setBases(self, newBasesTuple):
        # type: (PyObject) -> None
        pass

    def setName(self, name):
        # type: (String) -> None
        pass

    def super_lookup(self, ref, name):
        # type: (PyType, String) -> PyObject
        pass

    def traverse(self, visit, arg):
        # type: (Visitproc, Object) -> int
        pass

    def type___eq__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___ge__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___gt__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___instancecheck__(self, inst):
        # type: (PyObject) -> bool
        return True

    def type___le__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___lt__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___ne__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def type___subclasscheck__(self, inst):
        # type: (PyObject) -> bool
        return True

    def type___subclasses__(self):
        # type: () -> PyObject
        pass


class TraceFunction(Object):
    def traceCall(self, frame):
        # type: (PyFrame) -> TraceFunction
        raise NotImplementedError

    def traceException(self, frame, exc):
        # type: (PyFrame, PyException) -> TraceFunction
        raise NotImplementedError

    def traceLine(self, frame, line):
        # type: (PyFrame, int) -> TraceFunction
        raise NotImplementedError

    def traceReturn(self, frame, ret):
        # type: (PyFrame, PyObject) -> TraceFunction
        raise NotImplementedError


class Visitproc(object):
    def visit(self, obj, arg):
        # type: (PyObject, Object) -> int
        pass
