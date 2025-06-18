from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient
from dev.coatl.helper.types import AnyStr

def getExternalIpAddress() -> AnyStr: ...
def getHostName() -> AnyStr: ...
def getIpAddress() -> AnyStr: ...
def getRemoteServers(runningOnly: Optional[bool] = ...) -> List[AnyStr]: ...
def httpClient(
    timeout: int = ...,
    bypass_cert_validation: bool = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    proxy: Optional[AnyStr] = ...,
    cookie_policy: AnyStr = ...,
    redirect_policy: AnyStr = ...,
    version: AnyStr = ...,
    customizer: Optional[Callable[..., Any]] = ...,
) -> JythonHttpClient: ...
def httpDelete(
    url: AnyStr,
    contentType: Optional[AnyStr] = ...,
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    headerValues: Optional[Dict[AnyStr, AnyStr]] = ...,
    bypassCertValidation: bool = ...,
) -> AnyStr: ...
def httpGet(
    url: AnyStr,
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    headerValues: Optional[Dict[AnyStr, AnyStr]] = ...,
    bypassCertValidation: Optional[bool] = ...,
    useCaches: bool = ...,
    throwOnError: bool = ...,
) -> AnyStr: ...
def httpPost(url: AnyStr, *args: Any, **kwargs: Any) -> AnyStr: ...
def httpPut(url: AnyStr, *args: Any, **kwargs: Any) -> AnyStr: ...
def openURL(url: AnyStr, useApplet: Optional[bool] = ...) -> None: ...
def sendEmail(
    smtp: Optional[AnyStr] = ...,
    fromAddr: AnyStr = ...,
    subject: Optional[AnyStr] = ...,
    body: Optional[AnyStr] = ...,
    html: bool = ...,
    to: Optional[List[AnyStr]] = ...,
    attachmentNames: Optional[List[object]] = ...,
    attachmentData: Optional[List[object]] = ...,
    timeout: int = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    priority: AnyStr = ...,
    smtpProfile: Optional[AnyStr] = ...,
    cc: Optional[List[AnyStr]] = ...,
    bcc: Optional[List[AnyStr]] = ...,
    retries: int = ...,
    replyTo: Optional[List[AnyStr]] = ...,
) -> None: ...
