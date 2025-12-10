from __future__ import print_function

__all__ = ["CookieManager", "JythonHttpClient", "Promise", "Response"]

from typing import Any, Dict, Optional, Union

from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpRequest, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture

from com.inductiveautomation.ignition.common.gson import Gson
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
        # type: (*PyObject, **Union[str, unicode]) -> Response
        pass

    def deleteAsync(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Promise
        pass

    def get(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Response
        pass

    def getAsync(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Promise
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
        # type: () -> Union[str, unicode]
        pass

    def getVersion(self):
        # type: () -> Union[str, unicode]
        pass

    def head(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def headAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def options(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def optionsAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def parseChart(self, contentType):
        # type: (Union[str, unicode]) -> Optional[Charset]
        pass

    def patch(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def patchAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def post(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def postAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def put(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def putAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def request(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def requestAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def setGson(self, gson):
        # type: (Gson) -> None
        pass

    def trace(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def traceAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass


class Promise(Object):
    def cancel(self):
        # type: () -> bool
        return True

    def get(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Any
        pass

    def getFuture(self):
        # type: () -> CompletableFuture
        pass

    def handleException(self, callback):
        # type: (PyObject) -> Promise
        pass

    def isDone(self):
        # type: () -> bool
        return True

    def then(self, callback):
        # type: (PyObject) -> Promise
        pass

    def whenComplete(self, callback):
        # type: (PyObject) -> None
        pass


class Response(Object):
    class RequestWrapper(Object):
        def __init__(self, *args):
            # type: (*Any) -> None
            super(Response.RequestWrapper, self).__init__()
            print(args)

        def getHeaders(self):
            # type: () -> Any
            pass

        def getJavaRequest(self):
            # type: () -> HttpRequest
            pass

        def getMethod(self):
            # type: () -> Union[str, unicode]
            pass

        def getTimeout(self):
            # type: () -> long
            pass

        def getUrl(self):
            # type: () -> Union[str, unicode]
            pass

        def getVersion(self):
            # type: () -> Union[str, unicode]
            pass

    def __init__(self, httpResponse, client):
        # type: (HttpResponse, JythonHttpClient) -> None
        super(Response, self).__init__()
        print(httpResponse, client)

    @property
    def body(self):
        # type: () -> Any
        pass

    @property
    def clientError(self):
        # type: () -> bool
        return True

    @property
    def cookieManager(self):
        # type: () -> CookieManager
        return self.getCookieManager()

    @property
    def good(self):
        # type: () -> bool
        return True

    @property
    def headers(self):
        # type: () -> Dict[Union[str, unicode], Any]
        return self.getHeaders()

    @property
    def javaResponse(self):
        # type: () -> HttpResponse
        return self.getJavaResponse()

    @property
    def json(self):
        # type: () -> Dict[Union[str, unicode], Any]
        return self.getJson()

    @property
    def request(self):
        # type: () -> Response.RequestWrapper
        return self.getRequest()

    @property
    def serverError(self):
        # type: () -> bool
        return self.isServerError()

    @property
    def statusCode(self):
        # type: () -> int
        return self.getStatusCode()

    @property
    def text(self):
        # type: () -> Union[str, unicode]
        return self.getText()

    @property
    def url(self):
        # type: () -> Union[str, unicode]
        return self.getUrl()

    def getBody(self):
        # type: () -> Any
        pass

    def getCookieManager(self):
        # type: () -> CookieManager
        pass

    def getHeaders(self):
        # type: () -> Dict[Union[str, unicode], Any]
        pass

    def getJavaResponse(self):
        # type: () -> HttpResponse
        pass

    def getJson(self, *args, **kwargs):
        # type: (*Any, **Any) -> Dict[Union[str, unicode], Any]
        pass

    def getRequest(self):
        # type: () -> Response.RequestWrapper
        pass

    def getStatusCode(self):
        # type: () -> int
        pass

    def getText(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def getUrl(self):
        # type: () -> Union[str, unicode]
        pass

    def isClientError(self):
        # type: () -> bool
        return True

    def isGood(self):
        # type: () -> bool
        return True

    def isServerError(self):
        # type: () -> bool
        return True
