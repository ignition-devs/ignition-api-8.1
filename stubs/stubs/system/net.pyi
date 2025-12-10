from typing import Any, Callable, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient

def getExternalIpAddress() -> Union[str, unicode]: ...
def getHostName() -> Union[str, unicode]: ...
def getIpAddress() -> Union[str, unicode]: ...
def getRemoteServers(
    runningOnly: Optional[bool] = ...,
) -> List[Union[str, unicode]]: ...
def httpClient(
    timeout: int = ...,
    bypass_cert_validation: bool = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    proxy: Union[str, unicode, None] = ...,
    cookie_policy: Union[str, unicode] = ...,
    redirect_policy: Union[str, unicode] = ...,
    version: Union[str, unicode] = ...,
    customizer: Optional[Callable[..., Any]] = ...,
) -> JythonHttpClient: ...
def httpDelete(
    url: Union[str, unicode],
    contentType: Union[str, unicode, None] = ...,
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    headerValues: Optional[Dict[Union[str, unicode], Union[str, unicode]]] = ...,
    bypassCertValidation: bool = ...,
) -> Union[str, unicode]: ...
def httpGet(
    url: Union[str, unicode],
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    headerValues: Optional[Dict[Union[str, unicode], Union[str, unicode]]] = ...,
    bypassCertValidation: Optional[bool] = ...,
    useCaches: bool = ...,
    throwOnError: bool = ...,
) -> Union[str, unicode]: ...
def httpPost(
    url: Union[str, unicode], *args: Any, **kwargs: Any
) -> Union[str, unicode]: ...
def httpPut(
    url: Union[str, unicode], *args: Any, **kwargs: Any
) -> Union[str, unicode]: ...
def openURL(url: Union[str, unicode], useApplet: Optional[bool] = ...) -> None: ...
def sendEmail(
    smtp: Union[str, unicode, None] = ...,
    fromAddr: Union[str, unicode] = ...,
    subject: Union[str, unicode, None] = ...,
    body: Union[str, unicode, None] = ...,
    html: bool = ...,
    to: Optional[List[Union[str, unicode]]] = ...,
    attachmentNames: Optional[List[object]] = ...,
    attachmentData: Optional[List[object]] = ...,
    timeout: int = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    priority: Union[str, unicode] = ...,
    smtpProfile: Union[str, unicode, None] = ...,
    cc: Optional[List[Union[str, unicode]]] = ...,
    bcc: Optional[List[Union[str, unicode]]] = ...,
    retries: int = ...,
    replyTo: Optional[List[Union[str, unicode]]] = ...,
) -> None: ...
