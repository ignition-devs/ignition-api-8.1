"""Utility Functions.

The following functions give you access to view various Gateway and
Client data, as well as interact with other various systems.
"""

from __future__ import print_function, unicode_literals

__all__ = [
    "audit",
    "beep",
    "execute",
    "exit",
    "getAvailableLocales",
    "getAvailableTerms",
    "getClientId",
    "getConnectTimeout",
    "getConnectionMode",
    "getEdition",
    "getGatewayAddress",
    "getGatewayStatus",
    "getGlobals",
    "getInactivitySeconds",
    "getLocale",
    "getLogger",
    "getProjectName",
    "getProperty",
    "getReadTimeout",
    "getSessionInfo",
    "getSystemFlags",
    "getVersion",
    "invokeAsynchronous",
    "invokeLater",
    "jsonDecode",
    "jsonEncode",
    "modifyTranslation",
    "playSoundClip",
    "queryAuditLog",
    "retarget",
    "sendMessage",
    "sendRequest",
    "sendRequestAsync",
    "setConnectTimeout",
    "setConnectionMode",
    "setLocale",
    "setLoggingLevel",
    "setReadTimeout",
    "threadDump",
    "translate",
]

import getpass
import json
import os
import platform
import sys
from typing import Any, Callable, Dict, List, Optional, Union

import system.__version__ as version
import system.security
from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.model import Version
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SystemUtilities,
)
from com.inductiveautomation.ignition.common.util import LoggerEx
from java.awt import Toolkit
from java.lang import Thread
from java.util import Date

PyDataSet = DatasetUtilities.PyDataSet
RequestImpl = SystemUtilities.RequestImpl


def audit(
    action=None,  # type: Optional[Union[str, unicode]]
    actionValue=None,  # type: Optional[Union[str, unicode]]
    auditProfile="",  # type: Optional[Union[str, unicode]]
    actor=None,  # type: Optional[Union[str, unicode]]
    actorHost="localhost",  # type: Optional[Union[str, unicode]]
    originatingSystem=None,  # type: Optional[List[Union[str, unicode]]]
    eventTimestamp=None,  # type: Optional[Date]
    originatingContext=4,  # type: Optional[int]
    statusCode=0,  # type: Optional[int]
):
    # type: (...) -> None
    """Inserts a record into an audit profile.

    Args:
        action: What happened. Default is null. Optional.
        actionValue: What the action happened to. Default is null.
            Optional.
        auditProfile: Where the audit record should be stored. Defaults
            to the project's audit profile (if specified), or the
            gateway audit profile if calling in the gateway or
            perspective scope. Optional.
        actor: Who made the change. Will be populated automatically if
            omitted, assuming there is a known user. Optional.
        actorHost: The hostname of whoever made the change. Will be
            populated automatically if omitted.
        originatingSystem: An even-length list providing additional
            context to the audit event. Optional.
        eventTimestamp: When the event happened. Will be set to the
            current time if omitted. Optional.
        originatingContext: What scope the event originated from: 1
            means Gateway, 2 means Designer, 4 means Client. Will be set
            automatically if omitted. Optional.
        statusCode: A quality code to attach to the object. Defaults to
            0, indicating no special meaning. Optional.
    """
    actor = system.security.getUsername() if actor is None else actor
    print(
        action,
        actionValue,
        auditProfile,
        actor,
        actorHost,
        originatingSystem,
        eventTimestamp,
        originatingContext,
        statusCode,
    )


def beep():
    # type: () -> None
    """Tells the computer to make a "beep" sound."""
    platforms = {
        "linux1": "Linux",
        "linux2": "Linux",
        "darwin": "macOS",
        "win32": "Windows",
    }

    if "java" in sys.platform:
        Toolkit.getDefaultToolkit().beep()
    elif sys.platform in platforms:
        if platforms[sys.platform] == "Windows":
            try:
                import winsound

                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            except ImportError:
                print("Beep!")
        elif platforms[sys.platform] == "macOS":
            os.system('say "beep"')
        elif platforms[sys.platform] == "Linux":
            print("\a")
    else:
        print("Beep!")


def execute(commands):
    # type: (List[Union[str, unicode]]) -> None
    """Executes the given commands via the operating system, in a
    separate process.

    The commands argument is an array of strings. The first string is
    the program to execute, with subsequent strings being the arguments
    to that command.

    Args:
        commands: A list containing the command (1st entry) and
            associated arguments (remaining entries) to execute.
    """
    print(commands)


def exit(force=False):
    # type: (Optional[bool]) -> None
    """Exits the running client, as long as the shutdown intercept
    script doesn't cancel the shutdown event.

    Set force to True to not give the shutdown intercept script a chance
    to cancel the exit. Note that this will quit the Client completely.
    You can use system.security.logout() to return to the login screen.

    Args:
        force: If True (1), the shutdown-intercept script will be
            skipped. Default is False (0). Optional.
    """
    print(force)


def getAvailableLocales():
    # type: () -> List[Union[str, unicode]]
    """Returns a collection of strings representing the Locales added
    to the Translation Manager, such as 'en' for English.

    Returns:
        A collection of strings representing the Locales added to the
        Translation Manager.
    """
    return ["en_US", "es_MX"]


def getAvailableTerms():
    # type: () -> List[Union[str, unicode]]
    """Returns a collection of available terms defined in the
    translation system.

    Returns:
         A collection of all of the terms available from the Translation
         Manager.
    """
    return ["term1", "term2"]


def getClientId():
    # type: () -> Union[str, unicode]
    """Returns a hex-string that represents a number unique to the
    running client's session.

    You are guaranteed that this number is unique between all running
    clients.

    Returns:
        A special code representing the client's session in a unique
        way.
    """
    return "92247003"


def getConnectTimeout():
    # type: () -> int
    """Returns the connect timeout in milliseconds for all
    client-to-gateway communication.

    This is the maximum amount of time that communication operations to
    the Gateway will be given to connect. The default is 10,000ms (10
    seconds).

    Returns:
        The current connect timeout, in milliseconds. Default is 10,000
        (ten seconds).
    """
    return 10000


def getConnectionMode():
    # type: () -> int
    """Retrieves this client session's current connection mode.

    3 is read/write, 2 is read-only, and 1 is disconnected.

    Returns:
        The current connection mode for the client.
    """
    return 3


def getEdition():
    # type: () -> Union[str, unicode]
    """Returns the "edition" of the Vision client - "standard",
    "limited", or "panel".

    Returns:
        The edition of the Vision module that is running the client.
    """
    return "standard"


def getGatewayAddress():
    # type: () -> Union[str, unicode]
    """Returns the address of the gateway that the client is currently
    communicating with.

    Returns:
        The address of the Gateway that the client is communicating
        with.
    """
    return "http://localhost:8088/"


def getGatewayStatus(
    gatewayAddress,  # type: Union[str, unicode]
    connectTimeoutMillis=None,  # type: Optional[int]
    socketTimeoutMillis=None,  # type: Optional[int]
):
    # type: (...) -> Union[str, unicode]
    """Returns a string that indicates the status of the Gateway.

    A status of RUNNING means that the Gateway is fully functional.
    Thrown exceptions return "ERROR" with the error message appended to
    the string.

    Args:
        gatewayAddress: The gateway address to ping, in the form of
            ADDR:PORT/main.
        connectTimeoutMillis: The maximum time in milliseconds to
            attempt to initially contact a Gateway. Optional.
        socketTimeoutMillis: The maximum time in milliseconds to wait
            for a response from a Gateway after initial connection has
            been established. Optional.

    Returns:
        A string that indicates the status of the Gateway. A status of
        RUNNING means that the Gateway is fully functional.
    """
    print(gatewayAddress, connectTimeoutMillis, socketTimeoutMillis)
    return "RUNNING"


def getGlobals():
    # type: () -> Dict[Union[str, unicode], Any]
    """This method returns a dictionary that provides access to the
    legacy global namespace.

    As of version 7.7.0, most new scripts use the modern style of
    scoping, which makes the 'global' keyword act very differently. Most
    importantly, the modern scoping rules mean that variables declared
    as 'global' are only global within that one module. The
    system.util.getGlobals() method can be used to interact with older
    scripts that used the old meaning of the 'global' keyword.

    Returns:
        The global namespace, as a dictionary.
    """
    return {"foo": "bar"}


def getInactivitySeconds():
    # type: () -> long
    """Returns the number of seconds since any keyboard or mouse
    activity.

    Note - this function will always return zero in the Designer.

    Returns:
        The number of seconds the mouse and keyboard have been inactive
        for this client.
    """
    return long(0)


def getLocale():
    # type: () -> Union[str, unicode]
    """Returns the current string representing the user's Locale, such
    as 'en' for English.

    Returns:
        The current Locale.
    """
    return "en_US"


def getLogger(name):
    # type: (Union[str, unicode]) -> LoggerEx
    """Returns a Logger object that can be used to log messages to the
    console.

    Args:
        name: The name of a logger to create.

    Returns:
        A new Logger object used to log informational and error
        messages.
    """
    print(name)
    return LoggerEx()


def getProjectName():
    # type: () -> Union[str, unicode]
    """Returns the name of the project that is currently being run.

    Returns:
        The name of the currently running project.
    """
    return "MyProject"


def getProperty(propertyName):
    # type: (Union[str, unicode]) -> Optional[Union[str, unicode]]
    r"""Retrieves the value of a named system property.

    Some of the available properties are:

        file.separator. The system file separator character. (for
            example, "/" (unix) or "\" (windows))
        line.separator. The system line separator string. (for example,
            "\r\n" (carriage return, newline))
        os.arch. Operating system architecture. (for example, "x86")
        os.name. Operating system name. (for example, "Windows XP")
        os.version. Operating system version. (for example, "5.1")
        user.home. User's home directory.
        user.name. User's account name.

    Args:
        propertyName: The name of the system property to get.

    Returns:
        The value for the named property.
    """
    ret = None

    if propertyName == "file.separator":
        ret = os.sep
    elif propertyName == "line.separator":
        ret = os.linesep
    elif propertyName == "os.arch":
        ret = platform.machine()
    elif propertyName == "os.name":
        ret = platform.system()
    elif propertyName == "os.version":
        ret = platform.release()
    elif propertyName == "user.home":
        ret = os.path.expanduser(str("~"))
    elif propertyName == "user.name":
        ret = getpass.getuser()

    return ret


def getReadTimeout():
    # type: () -> int
    """Returns the read timeout in milliseconds for all
    client-to-gateway communication.

    This is the maximum amount of time allowed for a communication
    operation to complete. The default is 60,000 ms (1 minute).

    Returns:
         The current read timeout, in milliseconds. Default is 60,000 ms
         (one minute).
    """
    return 60000


def getSessionInfo(
    usernameFilter=None,  # type: Optional[Union[str, unicode]]
    projectFilter=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> PyDataSet
    """Returns a PyDataSet holding information about all of the sessions
    (logged-in users) on the Gateway.

    Optional regular-expression based filters can be provided to filter
    the username or the username and the project returned.

    Args:
        usernameFilter: A regular-expression based filter string to
            restrict the list by username. Optional.
        projectFilter: A regular-expression based filter string to
            restrict the list by project. Optional.

    Returns:
        A dataset representing the Gateway's current sessions.
    """
    print(usernameFilter, projectFilter)
    return PyDataSet()


def getSystemFlags():
    # type: () -> int
    """Returns an integer that represents a bit field containing
    information about the currently running system.

    Each bit corresponds to a specific flag as defined in the bitmask
    below. The integer return will be a total of all of the bits that
    are currently active.

    Returns:
        A total of all the bits that are currently active. A full screen
        client launched from the gateway webpage with no SSL will have a
        value of 44 (Fullscreen flag + Webstart Flag + Client Flag).
    """
    return 1


def getVersion():
    # type: () -> Version
    """Returns the Ignition version number that is currently being run.

    Returns:
        The currently running Ignition version number, as a Version
        object.
    """
    major, minor, rev = [int(i) for i in version.__version__.split(".")]
    build = int(version.__build__)
    return Version(major=major, minor=minor, rev=rev, build=build)


def invokeAsynchronous(
    function,  # type: Callable
    args=None,  # type: Optional[List[Any]]
    kwargs=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    description=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> Thread
    """Invokes (calls) the given Python function on a different thread.

    This means that calls to invokeAsynchronous will return immediately,
    and then the given function will start executing asynchronously on a
    different thread. This is useful for long-running data intensive
    functions, where running them synchronously (in the GUI thread)
    would make the GUI non-responsive for an unacceptable amount of
    time.

    Args:
        function: A Python function object that will get invoked with no
            arguments in a separate thread.
        args: A list or tuple of Python objects that will be provided to
            the called function as arguments. Equivalent to the *
            operator. Optional.
        kwargs: A dictionary of keyword argument names to Python object
            values that will be provided to the called function as
            keyword arguments. Equivalent to the ** operator. Optional.
        description: A description to use for the asynchronous thread.
            Will be displayed on the current scope's diagnostic view for
            scripts. For Vision and the Designer, this would be the
            "Scripts" tab of the Diagnostics popup. For Perspective and
            the Gateway scope, this would be the Gateway's Running
            Scripts status page. Optional.

    Returns:
        The executing thread.
    """
    print(function, args, kwargs, description)
    return Thread()


def invokeLater(function, delay=0):
    # type: (Callable, Optional[int]) -> None
    """Invokes (calls) the given Python function object after all of the
    currently processing and pending events are done being processed,
    or after a specified delay.

    The function will be executed on the GUI, or event dispatch, thread.
    This is useful for events like propertyChange events, where the
    script is called before any bindings are evaluated.

    If you specify an optional time argument (number of milliseconds),
    the function will be invoked after all currently processing and
    pending events are processed plus the duration of that time.

    Args:
        function: A Python function object that will be invoked later,
            on the GUI, or event-dispatch, thread with no arguments.
        delay: A delay, in milliseconds, to wait before the function is
            invoked. The default is 0, which means it will be invoked
            after all currently pending events are processed. Optional.
    """
    print(function, delay)


def jsonDecode(jsonString):
    # type: (Union[str, unicode]) -> Any
    """Takes a json String and converts it into a Python object such as
    a list or a dict.

    If the input is not valid json, a string is returned.

    Args:
        jsonString: The JSON string to decode into a Python object.

    Returns:
        The decoded Python object.
    """
    return json.loads(jsonString)


def jsonEncode(pyObj, indentFactor=4):
    """Takes a Python object such as a list or dict and converts into a
    json string.

    Args:
        pyObj: The Python object to encode into JSON such as a Python
            list or dictionary.
        indentFactor: The number of spaces to add to each level of
            indentation for prettyprinting. Optional.

    Returns:
        The encoded JSON string.
    """
    return json.dumps(pyObj, indent=indentFactor)


def modifyTranslation(
    term,  # type: Union[str, unicode]
    translation,  # type: Union[str, unicode]
    locale="es_MX",  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> None
    """This function allows you to add or modify a global translation.

    Args:
        term: The key term to translate.
        translation: The translated value to store.
        locale: If specified, the locale code (such as "es") identifying
            the language of the translation. Otherwise, the currently
            set language is used. Optional.
    """
    print(term, translation, locale)


def playSoundClip(wav, volume=1.0, wait=False):
    # type: (Any, Optional[float], Optional[bool]) -> None
    """Plays a sound clip from a wav file to the system's default audio
    device.

    The wav file can be specified as a filepath, a URL, or directly as a
    raw byte[].

    Args:
        wav: A byte list of a wav file or filepath or URL that
            represents a wav file.
        volume: The clip's volume, represented as a floating point
            number between 0.0 and 1.0. Optional.
        wait: A boolean flag indicating whether or not the call to
            playSoundClip should wait for the clip to finish before it
            returns. Optional.
    """
    print(wav, volume, wait)


def queryAuditLog(
    auditProfileName,  # type: Union[str, unicode]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    actorFilter=None,  # type: Optional[Union[str, unicode]]
    actionFilter=None,  # type: Optional[Union[str, unicode]]
    targetFilter=None,  # type: Optional[Union[str, unicode]]
    valueFilter=None,  # type: Optional[Union[str, unicode]]
    systemFilter=None,  # type: Optional[Union[str, unicode]]
    contextFilter=None,  # type: Optional[int]
):
    # type: (...) -> BasicDataset
    """Queries an audit profile for audit history.

    Returns the results as a dataset.

    Args:
        auditProfileName: The name of the audit profile to pull the
            history from.
        startDate: The earliest audit event to return. If omitted, the
            current time - 8 hours will be used. Optional.
        endDate: The latest audit event to return. If omitted, the
            current time will be used. Optional.
        actorFilter: A filter string used to restrict the results by
            actor. Optional.
        actionFilter: A filter string used to restrict the results by
            action. Optional.
        targetFilter: A filter string used to restrict the results by
            target. Optional.
        valueFilter: A filter string used to restrict the results by
            value. Optional.
        systemFilter: A filter string used to restrict the results by
            system. Optional.
        contextFilter: A bitmask used to restrict the results by
            context. 0x01 = Gateway, 0x02 = Designer, 0x04 = Client.
            Optional.

    Returns:
        A dataset with the audit events from the specified profile that
        match the filter arguments.
    """
    print(
        auditProfileName,
        startDate,
        endDate,
        actorFilter,
        actionFilter,
        targetFilter,
        valueFilter,
        systemFilter,
        contextFilter,
    )
    return BasicDataset()


def retarget(
    project,  # type: Union[str, unicode]
    addresses=None,  # type: Optional[Union[Union[str, unicode], List[Union[str, unicode]]]]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    windows=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> None
    """This function allows you to programmatically 'retarget' the
    Client to a different project and/or different Gateway.

    You can have it switch to another project on the same Gateway, or
    another gateway entirely, even across a WAN. This feature makes the
    vision of a seamless, enterprise-wide SCADA application a reality.

    The retarget feature will attempt to transfer the current user
    credentials over to the new project / Gateway. If the credentials
    fail on that project, the user will be prompted for a valid username
    and password. Once valid authentication has been achieved, the
    currently running project is shut down, and the new project is
    loaded.

    You can pass any information to the other project through the
    parameters dictionary. All entries in this dictionary will be set in
    the global scripting namespace in the other project. Even if you
    don't specify any parameters, the system will set the variable
    _RETARGET_FROM_PROJECT to the name of the current project and
    _RETARGET_FROM_GATEWAY to the address of the current Gateway.

    Args:
        project: The name of the project to retarget to.
        addresses: The address of the Gateway that the project resides
            on. Format is host:port when not using SSL/TLS, or
            https://host:port when SSL/TLS is enabled on the target
            gateway. This can be a list of strings. When using a list,
            the function will try each address in order, waiting for the
            timeout period between each address attempt. Optional.
        params: A dictionary of parameters that will be passed to the
            new project. They will be set as global variables in the new
            project's Python scripting environment. Optional.
        windows: A list of window paths to use as the startup windows.
            If omitted, the project's normal startup windows will be
            opened. If specified, the project's normal startup windows
            will be ignored, and this list will be used instead.
            Optional.
    """
    print(project, addresses, params, windows)


def sendMessage(
    project,  # type: Union[str, unicode]
    messageHandler,  # type: Union[str, unicode]
    payload=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    scope=None,  # type: Optional[Union[str, unicode]]
    clientSessionId=None,  # type: Optional[Union[str, unicode]]
    user=None,  # type: Optional[Union[str, unicode]]
    hasRole=None,  # type: Optional[Union[str, unicode]]
    hostName=None,  # type: Optional[Union[str, unicode]]
    remoteServers=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> List[Union[str, unicode]]
    """This function sends a message to clients running under the
    Gateway, or to a project within the Gateway itself.

    To handle received messages, you must set up event script message
    handlers within a project. These message handlers run Jython code
    when a message is received. You can add message handlers under the
    "Message" section of the client/Gateway event script configuration
    dialogs.

    Args:
        project: The name of the project containing the message handler.
        messageHandler: The name of the message handler that will fire
            upon receiving a message.
        payload: A PyDictionary which will get passed to the message
            handler. Use "payload" in the message handler to access
            dictionary variables. Optional.
        scope: Limits the scope of the message delivery to "C"
            (clients), "G" (Gateway), or "CG" for clients and the
            Gateway. Defaults to "C" if the user name, role or host name
            parameters are set, and to "CG" if none of these parameters
            are set. Optional.
        clientSessionId: Limits the message delivery to a client with
            the specified session ID. Optional.
        user: Limits the message delivery to clients where the specified
            user has logged in. Optional.
        hasRole: Limits the message delivery to any client where the
            logged in user has the specified user role. Optional.
        hostName: Limits the message delivery to the client that has the
            specified network host name. Optional.
        remoteServers: A list of Strings representing Gateway Server
            names. The message will be delivered to each server in the
            list. Upon delivery, the message is distributed to the local
            Gateway and clients as per the other parameters. Optional.

    Returns:
        A List of Strings containing information about each system that
        was selected for delivery, where each List item is
        comma-delimited.
    """
    print(
        project,
        messageHandler,
        payload,
        scope,
        clientSessionId,
        user,
        hasRole,
        hostName,
        remoteServers,
    )
    return ["information about the system"]


def sendRequest(
    project,  # type: Union[str, unicode]
    messageHandler,  # type: Union[str, unicode]
    payload=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    hostName=None,  # type: Optional[Union[str, unicode]]
    remoteServer=None,  # type: Optional[Union[str, unicode]]
    timeoutSec=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> Any
    """This function sends a message to the Gateway, working in a
    similar manner to the sendMessage function, except sendRequest
    expects a response to the message.

    To handle received messages, you must set up Gateway Event Script
    message handlers within a project. These message handlers run Jython
    code when a message is received. You can then place a return at the
    end of the code to return something to where the sendRequest was
    originally called from. You can add message handlers under the
    "Message" section of the Gateway Event Script configuration dialog.

    Args:
        project: The name of the project containing the message handler.
        messageHandler: The name of the message handler that will fire
            upon receiving a message.
        payload: A PyDictionary which will get passed to the message
            handler. Use "payload" in the message handler to access
            dictionary variables. Optional.
        hostName: Limits the message delivery to the client that has the
            specified network host name. Optional.
        remoteServer: A string representing a target Gateway Server
            name. The message will be delivered to the remote Gateway
            over the Gateway Network. Upon delivery, the message is
            distributed to the local Gateway and clients as per the
            other parameters. Optional.
        timeoutSec: The number of seconds before the sendRequest call
            times out. Optional.

    Returns:
        The return from the message handler.
    """
    print(
        project,
        messageHandler,
        payload,
        hostName,
        remoteServer,
        timeoutSec,
    )


def sendRequestAsync(
    project,  # type: Union[str, unicode]
    messageHandler,  # type: Union[str, unicode]
    payload=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    hostName=None,  # type: Optional[Union[str, unicode]]
    remoteServer=None,  # type: Optional[Union[str, unicode]]
    timeoutSec=None,  # type: Optional[int]
    onSuccess=None,  # type: Optional[Callable]
    onError=None,  # type: Optional[Callable]
):
    # type: (...) -> RequestImpl
    """This function sends a message to the Gateway and expects a
    response.

    Works in a similar manner to the sendRequest function, except
    sendRequestAsync will send the request and then immediately return a
    handle for it.

    Args:
        project: The name of the project containing the message handler.
        messageHandler: The name of the message handler that will fire
            upon receiving a message.
        payload: A PyDictionary which will get passed to the message
            handler. Use "payload" in the message handler to access
            dictionary variables. Optional.
        hostName: Limits the message delivery to the client that has the
            specified network host name. Optional.
        remoteServer: A string representing the target Gateway Server
            name. The message will be delivered to the remote Gateway
            over the Gateway Network. Upon delivery, the message is
            distributed to the local Gateway and clients as per the
            other parameters. Optional.
        timeoutSec: The number of seconds before the sendRequest call
            times out. Optional.
        onSuccess: Should take one argument, which will be the result
            from the message handler. Callback functions will be
            executed on the GUI thread, similar to
            system.util.invokeLater. Optional.
        onError: Should take one argument, which will be the exception
            encountered. Callback functions will be executed on the GUI
            thread, similar to system.util.invokeLater. Optional.

    Returns:
        The Request object that can be used while waiting for the
        message handler callback.
    """
    print(
        project,
        messageHandler,
        payload,
        hostName,
        remoteServer,
        timeoutSec,
        onSuccess,
        onError,
    )
    return RequestImpl(1000)


def setConnectTimeout(connectTimeout):
    # type: (int) -> None
    """Sets the connect timeout for client-to-gateway communication.

    Specified in milliseconds.

    Args:
        connectTimeout: The new connect timeout, specified in
            milliseconds.
    """
    print(connectTimeout)


def setConnectionMode(mode):
    # type: (int) -> None
    """Sets the connection mode for the client session.

    Normally a client runs in mode 3, which is read-write. You may wish
    to change this to mode 2, which is read-only, which will only allow
    reading and subscribing to tags, and running SELECT queries. Tag
    writes and INSERT / UPDATE / DELETE queries will not function. You
    can also set the connection mode to mode 1, which is disconnected,
    all tag and query features will not work.

    Args:
        mode: The new connection mode. 1 = Disconnected, 2 = Read-only,
            3 = Read/Write.
    """
    print(mode)


def setLocale(locale):
    # type: (Union[str, unicode]) -> None
    """Sets the user's current Locale.

    Any valid Java locale code (case-insensitive) can be used as a
    parameter, including ones that have not yet been added to the
    Translation Manager.

    Args:
        locale: A locale code, such as 'en_US' for US English.

    Raises:
        IllegalArgumentException: If passed an invalid local code.
    """
    print(locale)


def setLoggingLevel(loggerName, loggerLevel):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Sets the logging level on the given logger.

    This can be a logger you create, or a logger already defined in the
    system.

    Args:
        loggerName: The unique name of the logger to change the logging
            level on, for example "Tags.Client".
        loggerLevel: The level you want to change to logger to: "trace",
            "debug", "info", "warn" or "error".
    """
    print(loggerName, loggerLevel)


def setReadTimeout(readTimeout):
    # type: (int) -> None
    """Sets the read timeout for client-to-gateway communication.

    Specified in milliseconds.

    Args:
        readTimeout: The new read timeout, specified in
            milliseconds.
    """
    print(readTimeout)


def threadDump():
    # type: () -> Union[str, unicode]
    """Creates a thread dump of the current running JVM.

    Returns:
        The dump of the current running JVM.
    """
    return "Ignition version: {}...".format(getVersion())


def translate(
    term,  # type: Union[str, unicode]
    locale=None,  # type: Optional[Union[str, unicode]]
    strict=False,  # type: Optional[bool]
):
    # type: (...) -> Union[str, unicode]
    """This function allows you to retrieve the global translation of a
    term from the translation database using the current locale.

    Args:
        term: The term to look up.
        locale: Which locale to translate against. Useful when there are
            multiple locales defined for a single term. If omitted, the
            function attempts to use the current locale (as defined by
            the client, session, or Designer). Optional.
        strict: If False, the function will return the passed term
            (param 1) if it could not find a defined translation for the
            locale: meaning, if you pass a term that hasn't been
            configured, the function will just send the term back to
            you. If True, then the function will return a None when it
            fails to find a defined translation. Default is False.
            Optional.

    Returns:
        The translated term.
    """
    print(term, locale, strict)
    return term
