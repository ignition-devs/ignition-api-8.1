from typing import Any, Dict, Optional, Union

from com.inductiveautomation.ignition.common.gson import Gson
from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpRequest, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture
from org.python.core import PyObject

class CookieManager(JCookieManager):
    def __init__(self, *args: Any) -> None: ...

class JythonHttpClient(Object):
    def delete(self, *args: PyObject, **kwargs: Union[str, unicode]) -> Response: ...
    def deleteAsync(
        self, *args: PyObject, **kwargs: Union[str, unicode]
    ) -> Promise: ...
    def get(self, *args: PyObject, **kwargs: Union[str, unicode]) -> Response: ...
    def getAsync(self, *args: PyObject, **kwargs: Union[str, unicode]) -> Promise: ...
    def getConnectTimeout(self) -> long: ...
    def getCookieManager(self) -> CookieManager: ...
    def getJavaClient(self) -> HttpClient: ...
    def getRedirectPolicy(self) -> Union[str, unicode]: ...
    def getVersion(self) -> Union[str, unicode]: ...
    def head(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def headAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def options(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def optionsAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def parseChart(self, contentType: Union[str, unicode]) -> Optional[Charset]: ...
    def patch(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def patchAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def post(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def postAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def put(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def putAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def request(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def requestAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...
    def setGson(self, gson: Gson) -> None: ...
    def trace(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Response: ...
    def traceAsync(
        self,
        url: Union[str, unicode],
        params: Optional[Dict[Union[str, unicode], Any]] = ...,
        data: Optional[Any] = ...,
        file: Union[str, unicode, None] = ...,
        headers: Optional[Dict[Union[str, unicode], Any]] = ...,
        username: Union[str, unicode, None] = ...,
        password: Union[str, unicode, None] = ...,
        timeout: Optional[long] = ...,
    ) -> Promise: ...

class Promise(Object):
    def cancel(self) -> bool: ...
    def get(self, *args: PyObject, **kwargs: Union[str, unicode]) -> Any: ...
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
        def getMethod(self) -> Union[str, unicode]: ...
        def getTimeout(self) -> long: ...
        def getUrl(self) -> Union[str, unicode]: ...
        def getVersion(self) -> Union[str, unicode]: ...

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
    def headers(self) -> Dict[Union[str, unicode], Any]: ...
    @property
    def javaResponse(self) -> HttpResponse: ...
    @property
    def json(self) -> Dict[Union[str, unicode], Any]: ...
    @property
    def request(self) -> Response.RequestWrapper: ...
    @property
    def serverError(self) -> bool: ...
    @property
    def statusCode(self) -> int: ...
    @property
    def text(self) -> Union[str, unicode]: ...
    @property
    def url(self) -> Union[str, unicode]: ...
    def getBody(self) -> Any: ...
    def getCookieManager(self) -> CookieManager: ...
    def getHeaders(self) -> Dict[Union[str, unicode], Any]: ...
    def getJavaResponse(self) -> HttpResponse: ...
    def getJson(self, *args: Any, **kwargs: Any) -> Dict[Union[str, unicode], Any]: ...
    def getRequest(self) -> Response.RequestWrapper: ...
    def getStatusCode(self) -> int: ...
    def getText(self, *args: Any, **kwargs: Any) -> Union[str, unicode]: ...
    def getUrl(self) -> Union[str, unicode]: ...
    def isClientError(self) -> bool: ...
    def isGood(self) -> bool: ...
    def isServerError(self) -> bool: ...
