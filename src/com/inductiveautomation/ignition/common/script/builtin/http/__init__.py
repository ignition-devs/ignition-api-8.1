from __future__ import print_function

__all__ = ["CookieManager", "JythonHttpClient", "Promise", "Response"]

from typing import Any, Optional

from com.inductiveautomation.ignition.common.gson import Gson
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture
from org.python.core import PyObject


class CookieManager(JCookieManager):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(CookieManager, self).__init__()
        print(args)


class JythonHttpClient(Object):
    """A Jython-optimized wrapper around the base HttpClient available
    in Java 11+.

    Mostly, through convenience functions that make things easier to use
    from Jython.
    """

    def delete(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def deleteAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def get(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def getAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def getConnectTimeout(self):
        # type: () -> long
        pass

    def getCookieManager(self):
        # type: () -> CookieManager
        pass

    def getJavaClient(self):
        # type: () -> HttpClient
        pass

    def getRedirectPolicy(self):
        # type: () -> AnyStr
        pass

    def getVersion(self):
        # type: () -> AnyStr
        pass

    def head(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def headAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def options(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def optionsAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def parseChart(self, contentType):
        # type: (AnyStr) -> Optional[Charset]
        pass

    def patch(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def patchAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def post(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def postAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def put(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def putAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def request(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def requestAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass

    def setGson(self, gson):
        # type: (Gson) -> None
        pass

    def trace(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Response
        pass

    def traceAsync(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Promise
        pass


class Promise(Object):
    def cancel(self):
        # type: () -> bool
        pass

    def get(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Any
        pass

    def getFuture(self):
        # type: () -> CompletableFuture
        pass

    def handleException(self, callback):
        # type: (PyObject) -> Promise
        pass

    def isDone(self):
        # type: () -> bool
        pass

    def then(self, callback):
        # type: (PyObject) -> Promise
        pass

    def whenComplete(self, callback):
        # type: (PyObject) -> None
        pass


class Response(Object):
    def __init__(self, httResponse, client):
        # type: (HttpResponse, JythonHttpClient) -> None
        super(Response, self).__init__()
        print(httResponse, client)
