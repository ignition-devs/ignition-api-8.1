"""Net Functions.

The following functions give you access to interact with http services.
"""

from __future__ import print_function

__all__ = [
    "getExternalIpAddress",
    "getHostName",
    "getIpAddress",
    "getRemoteServers",
    "httpClient",
    "httpDelete",
    "httpGet",
    "httpPost",
    "httpPut",
    "openURL",
    "sendEmail",
]

import socket

from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient
from java.lang import IllegalArgumentException, String


def getExternalIpAddress():
    # type: () -> String
    """Returns the client's IP address, as it is detected by the
    Gateway.

    This means that this call will communicate with the Gateway, and the
    Gateway will tell the client what IP address its incoming traffic is
    coming from. If you have a client behind a Network Address
    Translation (NAT) router, then this address will be the Wide Area
    Network (WAN) address of the router instead of the Local Area
    Network (LAN) address of the client, which is what you'd get with
    system.net.getIpAddress.

    Returns:
        A text representation of the Client's IP address, as detected by
        the Gateway.
    """
    return "52.52.32.221"


def getHostName():
    # type: () -> String
    """Returns the host name of the computer that the script was ran
    on.

    When run in the Gateway scope, returns the Gateway hostname. When
    run in the Client scope, returns the Client hostname. On Windows,
    this is typically the "computer name". For example, might return
    EAST_WING_WORKSTATION or bobs-laptop.

    Returns:
        The hostname of the local machine.
    """
    return socket.gethostname()


def getIpAddress():
    # type: () -> String
    """Returns the IP address of the computer that the script was ran
    on.

    Returns:
        Returns the IP address of the local machine, as it sees it.
    """
    return socket.gethostbyname(str(getHostName()))


def getRemoteServers(runningOnly=True):
    # type: (Optional[bool]) -> List[String]
    """This function returns a List of Gateway Network servers that are
    visible from the local Gateway.

    Args:
        runningOnly: If set to True, only servers on the Gateway Network
            that are running will be returned. Servers that have lost
            contact with the Gateway Network will be filtered out.
            Optional.

    Returns:
        A List of strings representing Gateway Network Server IDs.
    """
    print(runningOnly)
    return []


def httpClient(
    timeout=60000,  # type: int
    bypass_cert_validation=False,  # type: bool
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    proxy=None,  # type: Optional[String]
    cookie_policy="ACCEPT_ORIGINAL_SERVER",  # type: String
    redirect_policy="NORMAL",  # type: String
    version="HTTP_2",  # type: String
    customizer=None,  # type: Optional[Callable[..., Any]]
):
    # type: (...) -> JythonHttpClient
    """Provides a general use object that can be used to send and
    receive HTTP requests.

    The object created by this function is a wrapper around Java's
    HttpClient class. Usage requires creating a JythonHttpClient object
    with a call to system.net.httpClient, then calling a method (such as
    get(), post()) on the JythonHttpClient to actually issue a request.

    Args:
        timeout: A value, in milliseconds, to set the client's connect
            timeout setting to. Defaults to 60000. Optional.
        bypass_cert_validation: A boolean indicating whether the client
            should attempt to validate the certificates of remote
            servers, if connecting via HTTPS/SSL. Defaults to False.
            Optional.
        username: A string indicating the username to use for
            authentication if the remote server requests authentication;
            specifically, by responding with a WWW-Authenticate or
            Proxy-Authenticate header. Only supports Basic
            authentication. If username is specified but not password,
            an empty string will be used for the password in the Basic
            Authentication response. Defaults to None. Optional.
        password: A string indicating the password to use for
            authentication. Defaults to None. Optional.
        proxy: The address of a proxy server, which will be used for
            HTTP and HTTPS traffic. If a port is not specified as part
            of that address, it will be assumed from the protocol in the
            URL, i.e. 80/443. Defaults to None. Optional.
        cookie_policy: A string representing this client's cookie
            policy. Accepts values "ACCEPT_ALL", "ACCEPT_NONE", and
            "ACCEPT_ORIGINAL_SERVER". Defaults to
            "ACCEPT_ORIGINAL_SERVER". Optional.
        redirect_policy: A string representing this client's redirect
            policy. Acceptable values are listed below. Defaults to
            "Normal". Optional.
        version: A string specifying either HTTP_2 or HTTP_1_1 for the
            HTTP protocol. When omitted, the previous default of HTTP_2
            is implied. Optional.
        customizer: A reference to a function. This function will be
            called with one argument (an instance of
            HttpClient.Builder). The function should operate on that
            builder instance, which allows for customization of the
            created HTTP client. Defaults to None. Optional.

    Returns:
        An object wrapped around an instance of Java's HttpClient class.
        The httpClient object has methods that can be called to execute
        HTTP requests against a server.
    """
    print(
        timeout,
        bypass_cert_validation,
        username,
        password,
        proxy,
        cookie_policy,
        redirect_policy,
        version,
        customizer,
    )
    return JythonHttpClient()


def httpDelete(
    url,  # type: String
    contentType=None,  # type: Optional[String]
    connectTimeout=10000,  # type: int
    readTimeout=60000,  # type: int
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    headerValues=None,  # type: Optional[Dict[String, String]]
    bypassCertValidation=True,  # type: bool
):
    # type: (...) -> String
    """Performs an HTTP DELETE to the given URL.

    Args:
        url: The URL to send the request to.
        contentType: The MIME type used in the HTTP 'Content-type'
            header. Optional.
        connectTimeout: The timeout for connecting to the URL in
            milliseconds. Default is 10,000. Optional.
        readTimeout: The read timeout for the operation in
            milliseconds. Default is 60,000. Optional.
        username: If specified, the call will attempt to authenticate
            with basic HTTP authentication. Optional.
        password: The password used for basic HTTP authentication, if
            the username parameter is also present. Optional.
        headerValues: A dictionary of name/value pairs that will be set
            in the HTTP header. Optional.
        bypassCertValidation: If the target address in an HTTPS address,
            and this parameter is TRUE, the system will bypass all SSL
            certificate validation. This is not recommended, though is
            sometimes necessary for self-signed certificates. Optional.

    Returns:
        The content returned for the DELETE operation.
    """
    print(
        url,
        contentType,
        connectTimeout,
        readTimeout,
        username,
        password,
        headerValues,
        bypassCertValidation,
    )
    return "DELETE"


def httpGet(
    url,  # type: String
    connectTimeout=10000,  # type: int
    readTimeout=60000,  # type: int
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    headerValues=None,  # type: Optional[Dict[String, String]]
    bypassCertValidation=None,  # type: Optional[bool]
    useCaches=True,  # type: bool
    throwOnError=True,  # type: bool
):
    # type: (...) -> String
    """Retrieves the document at the given URL using the HTTP GET
    protocol.

    The document is returned as a string. For example, if you use the
    URL of a website, you'll get the same thing you'd get by going to
    that website in a browser and using the browser's "View Source"
    function.

    Args:
        url: The URL to retrieve.
        connectTimeout: The timeout for connecting to the URL. In
            milliseconds. Default is 10,000. Optional.
        readTimeout: The read timeout for the get operation. In
            milliseconds. Default is 60,000. Optional.
        username: If specified, the call will attempt to authenticate
            with basic HTTP authentication. Optional.
        password: The password used for basic HTTP authentication, if
            the username parameter is also present. Optional.
        headerValues: A dictionary of name/value pairs that will be set
            in the HTTP header. Optional.
        bypassCertValidation: If the target address is an HTTPS address,
            and this parameter is True, the system will bypass all SSL
            certificate validation. This is not recommended, though is
            sometimes necessary for self-signed certificates. Optional.
        useCaches: Will cache the information returned by the httpGet
            call. If using this for something that constantly updates
            like an rss feed, it would be better to set this to False.
            Default is True. Optional.
        throwOnError: Set to False if you wish to get the error body
            rather than a Python exception if the GET request returns an
            error code (non-200 responsive). Default is True. Optional.

    Returns:
        The content found at the given URL.
    """
    print(
        url,
        connectTimeout,
        readTimeout,
        username,
        password,
        headerValues,
        bypassCertValidation,
        useCaches,
        throwOnError,
    )
    return ""


def httpPost(url, *args, **kwargs):
    # type: (String, *Any, **Any) -> String
    """Retrieves the document at the given URL using the HTTP POST
    protocol.

    If a parameter dictionary argument is specified, the entries in the
    dictionary will encoded in "application/x-www-form-urlencoded"
    format, and then posted. You can post arbitrary data as well, but
    you'll need to specify the MIME type. The document is then returned
    as a string.

    Args:
        url: The URL to post to.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        The content returned for the POST operation.
    """
    print(url, args, kwargs)
    return ""


def httpPut(url, *args, **kwargs):
    # type: (String, *Any, **Any) -> String
    """Performs an HTTP PUT to the given URL.

    Encodes the given dictionary of parameters using
    "applications/x-www-form-urlencoded" format.

    Args:
        url: The URL to put to.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        The content returned by the PUT operation.
    """
    print(url, args, kwargs)
    return ""


def openURL(url, useApplet=False):
    # type: (String, Optional[bool]) -> None
    """Opens the given URL or URI scheme outside of the currently
    running Client in whatever application the host operating system
    deems appropriate.

    Args:
        url: The URL to open in a web browser.
        useApplet: If set to True, and the client is running as an
            Applet, then the browser instance that launched the applet
            will be used to open the URL. Optional.
    """
    print(url, useApplet)


def _sendEmail(
    smtpSettings,  # type: Optional[String]
    fromAddr,  # type: String
    subject=None,  # type: Optional[String]
    body=None,  # type: Optional[String]
    html=False,  # type: bool
    to=None,  # type: Optional[List[String]]
    attachmentNames=None,  # type: Optional[List[object]]
    attachmentData=None,  # type: Optional[List[object]]
    timeout=300000,  # type: int
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    priority="3",  # type: String
    cc=None,  # type: Optional[List[String]]
    bcc=None,  # type: Optional[List[String]]
    retries=0,  # type: int
    replyTo=None,  # type: Optional[List[String]]
):
    # type: (...) -> None
    _to = [] if to is None else to
    _cc = [] if cc is None else cc
    _bcc = [] if bcc is None else bcc
    recipients = _to + _cc + _bcc
    if smtpSettings and fromAddr and len(recipients) > 0:
        print(
            smtpSettings,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            username,
            password,
            priority,
            cc,
            bcc,
            retries,
            replyTo,
        )
    else:
        raise IllegalArgumentException(
            "Cannot send email without SMTP host, from address and recipient list."
        )


def sendEmail(
    smtp=None,  # type: Optional[String]
    fromAddr="",  # type: String
    subject=None,  # type: Optional[String]
    body=None,  # type: Optional[String]
    html=False,  # type: bool
    to=None,  # type: Optional[List[String]]
    attachmentNames=None,  # type: Optional[List[object]]
    attachmentData=None,  # type: Optional[List[object]]
    timeout=300000,  # type: int
    username=None,  # type: Optional[String]
    password=None,  # type: Optional[String]
    priority="3",  # type: String
    smtpProfile=None,  # type: Optional[String]
    cc=None,  # type: Optional[List[String]]
    bcc=None,  # type: Optional[List[String]]
    retries=0,  # type: int
    replyTo=None,  # type: Optional[List[String]]
):
    # type: (...) -> None
    """Sends an email through the given SMTP server.

    Note that this email is relayed first through the Gateway - the
    client host machine doesn't need network access to the SMTP server.

    Args:
        smtp: The address of an SMTP server to send the email through,
            like "mail.example.com". A port can be specified, like
            "mail.example.com:25". SSL can also be forced, like
            "mail.example.com:25:tls".
        fromAddr: An email address to have the email come from.
        subject: The subject line for the email. Optional.
        body: The body text of the email. Optional.
        html: A flag indicating whether or not to send the email as an
            HTML email. Will auto-detect if omitted. Optional.
        to: A list of email addresses to send to.
        attachmentNames: A list of attachment names. Attachment names
            must have the correct extension for the file type or an
            error will occur. Optional.
        attachmentData: A list of attachment data, in binary format.
        timeout: A timeout for the email, specified in milliseconds.
            Defaults to 5 minutes (60,000*5). Optional.
        username: If specified, will be used to authenticate with the
            SMTP host. Optional.
        password: If specified, will be used to authenticate with the
            SMTP host. Optional.
        priority: Priority for the message, from "1" to "5", with "1"
            being highest priority. Defaults to "3" (normal) priority.
            Optional.
        smtpProfile: If specified, the named SMTP profile defined
            in the Gateway will be used. If this keyword is present, the
            smtp, username, and password keywords will be ignored.
            Optional.
        cc: A list of email addresses to carbon copy. Only available if
            a smtpProfile is used. Optional.
        bcc: A list of email addresses to blind carbon copy. Only
            available if a smtpProfile is used. Optional.
        retries: The number of additional times to retry sending on
            failure. Defaults to 0. Only available if a smtpProfile is
            used. Optional.
        replyTo: An optional list of addresses to have the recipients
            reply to. If omitted, this defaults to the from address.
            Optional.
    """
    if not smtpProfile:
        _sendEmail(
            smtp,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            username,
            password,
            priority,
            retries=retries,
            replyTo=replyTo,
        )
    else:
        _sendEmail(
            smtpProfile,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            priority=priority,
            cc=cc,
            bcc=bcc,
            retries=retries,
            replyTo=replyTo,
        )
