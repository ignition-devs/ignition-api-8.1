from typing import Any, Dict, Optional

from com.inductiveautomation.ignition.common.gson import Gson
from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpRequest, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture
from org.python.core import PyObject

class CookieManager(JCookieManager):
    def __init__(self, *args: Any) -> None: ...

class JythonHttpClient(Object):
    def delete(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def deleteAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def get(self, *args: PyObject, **kwargs: AnyStr) -> Response: ...
    def getAsync(self, *args: PyObject, **kwargs: AnyStr) -> Promise: ...
    def getConnectTimeout(self) -> long: ...
    def getCookieManager(self) -> CookieManager: ...
    def getJavaClient(self) -> HttpClient: ...
    def getRedirectPolicy(self) -> AnyStr: ...
    def getVersion(self) -> AnyStr: ...
    def head(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def headAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def options(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def optionsAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def parseChart(self, contentType: AnyStr) -> Optional[Charset]: ...
    def patch(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def patchAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def post(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def postAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def put(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def putAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def request(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def requestAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def setGson(self, gson: Gson) -> None: ...
    def trace(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def traceAsync(
        self,
        url: AnyStr,
        params: Optional[Dict[AnyStr, Any]] = ...,
        data: Optional[Any] = ...,
        file: Optional[AnyStr] = ...,
        headers: Optional[Dict[AnyStr, Any]] = ...,
        username: Optional[AnyStr] = ...,
        password: Optional[AnyStr] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...

class Promise(Object):
    def cancel(self) -> bool: ...
    def get(self, *args: PyObject, **kwargs: AnyStr) -> Any: ...
    def getFuture(self) -> CompletableFuture: ...
    def handleException(self, callback: PyObject) -> Promise: ...
    def isDone(self) -> bool: ...
    def then(self, callback: PyObject) -> Promise: ...
    def whenComplete(self, callback: PyObject) -> None: ...

class Response(Object):
    class RequestWrapper(Object):
        def __init__(self, *args: Any) -> None: ...
        def getHeaders(self) -> Any: ...
        def getJavaRequest(self) -> HttpRequest: ...
        def getMethod(self) -> AnyStr: ...
        def getTimeout(self) -> long: ...
        def getUrl(self) -> AnyStr: ...
        def getVersion(self) -> AnyStr: ...

    def __init__(
        self, httpResponse: HttpResponse, client: JythonHttpClient
    ) -> None: ...
    @property
    def body(self) -> Any: ...
    @property
    def clientError(self) -> bool: ...
    @property
    def cookieManager(self) -> CookieManager: ...
    @property
    def good(self) -> bool: ...
    @property
    def headers(self) -> Dict[AnyStr, Any]: ...
    @property
    def javaResponse(self) -> HttpResponse: ...
    @property
    def json(self) -> Dict[AnyStr, Any]: ...
    @property
    def request(self) -> Response.RequestWrapper: ...
    @property
    def serverError(self) -> bool: ...
    @property
    def statusCode(self) -> int: ...
    @property
    def text(self) -> AnyStr: ...
    @property
    def url(self) -> AnyStr: ...
    def getBody(self) -> Any: ...
    def getCookieManager(self) -> CookieManager: ...
    def getHeaders(self) -> Dict[AnyStr, Any]: ...
    def getJavaResponse(self) -> HttpResponse: ...
    def getJson(self, *args: Any, **kwargs: Any) -> Dict[AnyStr, Any]: ...
    def getRequest(self) -> Response.RequestWrapper: ...
    def getStatusCode(self) -> int: ...
    def getText(self, *args: Any, **kwargs: Any) -> AnyStr: ...
    def getUrl(self) -> AnyStr: ...
    def isClientError(self) -> bool: ...
    def isGood(self) -> bool: ...
    def isServerError(self) -> bool: ...
