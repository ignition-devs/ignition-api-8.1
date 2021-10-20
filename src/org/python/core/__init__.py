from __future__ import print_function

__all__ = ["PyObject", "PyType"]

from java.lang import Object


class PyObject(Object):
    """All objects known to the Jython runtime system are represented by
    an instance of the class PyObject or one of its subclasses.
    """

    def __init__(self, objType=None):
        print(objType)

    def __abs__(self):
        pass

    def __add__(self, other):
        pass

    def __and__(self, other):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __cmp__(self, other):
        pass

    def __coerce__(self, pyo):
        pass

    def __coerce_ex__(self, o):
        pass

    def __complex__(self):
        pass

    def __contains__(self, o):
        pass

    def __delete__(self, obj):
        pass

    def __delitem__(self, key):
        pass

    def __delslice__(self, start, stop, step=None):
        pass

    def __dir__(self):
        pass

    def __div__(self, other):
        pass

    def __ensure_finalizer__(self):
        pass

    def __findattr__(self, name):
        pass

    def __findattr_ex__(self, name):
        pass

    def __finditem__(self, key):
        pass

    def __float__(self):
        pass

    def __floordiv__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __get__(self, obj, type):
        pass

    def __getattr__(self, name):
        pass

    def __getitem__(self, key):
        pass

    def __getnewargs__(self):
        pass

    def __getslice__(self, start, stop, step=None):
        pass

    def __gt__(self, other):
        pass

    def __hex__(self):
        pass

    def __iadd__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __idivmod__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __ilshift__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __index__(self):
        pass

    def __int__(self):
        pass

    def __invert__(self):
        pass

    def __ior__(self, other):
        pass

    def __ipow__(self, other):
        pass

    def __irshift__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __iter__(self):
        pass

    def __iternext__(self):
        pass

    def __itruediv__(self, other):
        pass

    def __ixor__(self, other):
        pass

    def __le__(self, other):
        pass

    def __long__(self):
        pass

    def __lshift__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __neg__(self):
        pass

    def __nonzero__(self):
        pass

    def __not__(self):
        pass

    def __oct__(self):
        pass

    def __or__(self, other):
        pass

    def __pos__(self):
        pass

    def __pow__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __rpow__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __set__(self, obj, value):
        pass

    def __setitem__(self, key, value):
        pass

    def __setslice__(self, start, stop, value):
        pass

    def __sub__(self, other):
        pass

    def __tojava__(self, c):
        pass

    def __truediv__(self, other):
        pass

    def __trunc__(self):
        pass

    def __unicode__(self):
        pass

    def __xor__(self, other):
        pass

    def _add(self, o2):
        pass

    def _and(self, o2):
        pass

    def _callextra(self, *args, **kwargs):
        pass

    def _cmp(self, o):
        pass

    def _div(self, o2):
        pass

    def _divmod(self, o2):
        pass

    def _doget(self, container, wherefound=None):
        pass

    def _doset(self, container, value):
        pass

    def _eq(self, o):
        pass

    def _floordiv(self, o2):
        pass

    def _ge(self, o):
        pass

    def _gt(self, o):
        pass

    def _iadd(self, o2):
        pass

    def _iand(self, o2):
        pass

    def _idiv(self, o2):
        pass

    def _idivmod(self, o2):
        pass

    def _ifloordiv(self, o2):
        pass

    def _ilshift(self, o2):
        pass

    def _imod(self, o2):
        pass

    def _imul(self, o2):
        pass

    def _in(self, o):
        pass

    def _ior(self, o2):
        pass

    def _ipow(self, o2):
        pass

    def _irshift(self, o2):
        pass

    def _is(self, o):
        pass

    def _isnot(self, o):
        pass

    def _isub(self, o2):
        pass

    def _itruediv(self, o2):
        pass

    def _ixor(self, o2):
        pass

    def _jcall(self, *args):
        pass

    def _jcallexc(self, *args):
        pass

    def _jthrow(self, t):
        pass

    def _le(self, o):
        pass

    def _lshift(self, o2):
        pass

    def _lt(self, o):
        pass

    def _mod(self, o2):
        pass

    def _mul(self, o2):
        pass

    def _ne(self, o):
        pass

    def _notin(self, o):
        pass

    def _or(self, o2):
        pass

    def _pow(self, o2):
        pass

    def _rshift(self, o2):
        pass

    def _sub(self, o2):
        pass

    def _truediv(self, o2):
        pass

    def _xor(self, o2):
        pass

    def asDouble(self):
        pass

    def asIndex(self, err=None):
        pass

    def asInt(self, index=None):
        pass

    def asIterable(self):
        pass

    def asLong(self, index=None):
        pass

    def asName(self, arg):
        pass

    def asString(self, index=None):
        pass

    def asStringOrNull(self, index=None):
        pass

    def bit_length(self):
        pass

    def conjugate(self):
        pass

    def delDict(self):
        pass

    def delType(self):
        pass

    def dispatch__init__(self, *args, **kwargs):
        pass

    def fastGetClass(self):
        pass

    def fastGetDict(self):
        pass

    def finalize(self):
        pass

    def getDict(self):
        pass

    def getType(self):
        pass

    def impAttr(self):
        pass

    def implementsDescrDelete(self):
        pass

    def implementsDescrGet(self):
        pass

    def implementsDescrSet(self):
        pass

    def invoke(self, *args, **kwargs):
        pass

    def isCallable(self):
        pass

    def isDataDescr(self):
        pass

    def isIndex(self):
        pass

    def isInteger(self):
        pass

    def isMappingType(self):
        pass

    def isNumberType(self):
        pass

    def isSequenceType(self):
        pass

    def mergeClassDict(self, accum, aClass):
        pass

    def mergeDictAttr(self, accum, attr):
        pass

    def mergeListAttr(self, accum, attr):
        pass

    def noAttributeError(self, name):
        pass

    def object___subclasshook__(self, type, subclass):
        pass

    def readonlyAttributeError(self, name):
        pass

    def runsupportedopMessage(self, op, o2):
        pass

    def setDict(self, newDict):
        pass

    def setType(self, type):
        pass


class PyType(PyObject):
    @staticmethod
    def addBuilder(c, builder):
        pass

    def addMethod(self, meth):
        pass

    def compatibleForAssignment(self, other, attribute):
        pass

    def delBases(self):
        pass

    def delModule(self):
        pass

    @staticmethod
    def ensureBootstrapped():
        pass

    @staticmethod
    def ensureDoc():
        pass

    @staticmethod
    def ensureModule():
        pass

    def fastGetName(self):
        pass

    def fromClass(self, c, hardRef=False):
        pass

    def getAbstractMethods(self):
        pass

    def getBase(self):
        pass

    def getBases(self):
        pass

    def getDoc(self):
        pass

    def getFlags(self):
        pass

    def getModule(self):
        pass

    def getMro(self):
        pass

    def getName(self):
        pass

    def getNumSlots(self):
        pass

    def getProxyType(self):
        pass

    def getStatic(self):
        pass

    def instDict(self):
        pass

    def isSubType(self, supertype):
        pass

    def lookup_where(self, name, where):
        pass

    def lookup(self, name):
        pass

    def needsFinalizer(self):
        pass

    def newType(self, new_, metatype, name, bases, dict):
        pass

    def pyDelName(self):
        pass

    def pyGetName(self):
        pass

    def pySetName(self, name):
        pass

    def refersDirectlyTo(self, ob):
        pass

    def removeMethod(self, meth):
        pass

    def setAbstractMethods(self, value):
        pass

    def setBases(self, newBasesTuple):
        pass

    def setName(self, name):
        pass

    def super_lookup(self, ref, name):
        pass

    def traverse(self, visit, arg):
        pass

    def type___eq__(self, other):
        pass

    def type___ge__(self, other):
        pass

    def type___gt__(self, other):
        pass

    def type___instancecheck__(self, inst):
        pass

    def type___le__(self, other):
        pass

    def type___lt__(self, other):
        pass

    def type___ne__(self, other):
        pass

    def type___subclasscheck__(self, inst):
        pass

    def type___subclasses__(self):
        pass
