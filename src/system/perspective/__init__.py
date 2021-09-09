"""Perspective Functions.

The following functions offer various ways to interact with a
Perspective session from a Python script.
"""

from __future__ import print_function

__all__ = [
    "alterLogging",
    "closeDock",
    "closePage",
    "closePopup",
    "closeSession",
    "download",
    "getProjectInfo",
    "getSessionInfo",
    "isAuthorized",
    "login",
    "logout",
    "navigate",
    "navigateBack",
    "navigateForward",
    "openDock",
    "openPopup",
    "print",
    "refresh",
    "sendMessage",
    "setTheme",
    "toggleDock",
    "togglePopup",
    "vibrateDevice",
]

import __builtin__ as builtins

from java.lang import Object


class PyJsonObjectAdapter(Object):
    """Class PyJsonObjectAdapter."""

    def __init__(self, obj):
        builtins.print(self, obj)

    def __delitem__(self, key):
        pass

    def __findattr_ex__(self, name):
        pass

    def __finditem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def clear(self):
        pass

    def get(self, key, default=None):
        pass

    def has_key(self, key):
        pass

    def items(self):
        pass

    def iteritems(self):
        pass

    def iterkeys(self):
        pass

    def itervalues(self):
        pass

    def keys(self):
        pass

    def pop(self, key):
        pass

    def popitem(self):
        pass

    def setdefault(self, key, default):
        pass

    def update(self, *args, **kwargs):
        pass

    def values(self):
        pass


def alterLogging(
    remoteLoggingEnabled=False,
    level="info",
    remoteLoggingLevel="warn",
    sessionId="current_session",
    pageId="current_page",
):
    """Changes Perspective Session logging attributes and levels.

    All parameters are optional, with the caveat that at least one of
    them needs to be used.

    Args:
        remoteLoggingEnabled (bool): Will enable remote logging if True.
            Remote logging will send log events from the Session to the
            Gateway under the perspective.client logger if the meet the
            remoteLevel logging level requirement. Optional.
        level (str): The desired Session logging level. Possible values
            are: all, trace, debug, info, warn, error, fatal, off. The
            default is info. Optional.
        remoteLoggingLevel (str): The desired remote logging level.
            Possible values are: all, trace, debug, info, warn, error,
            fatal, off. The default is warn. Optional.
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(
        remoteLoggingEnabled, level, remoteLoggingLevel, sessionId, pageId
    )


def closeDock(id, sessionId=None, pageId=None):
    """Closes a docked view.

    Args:
        id (str): The unique, preconfigured 'Dock ID' for the docked
            View. Is specified when a View is assigned as docked for a
            particular Page (in Page Configuration).
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(id, sessionId, pageId)


def closePage(
    message=None, sessionId="current_session", pageID="current_page"
):
    """Closes the page with the given page id or the current page if no
    page id is provided.

    If a message is provided, it is displayed on the page when the page
    closes. Otherwise the default message (set in the Project
    Properties) is displayed.

    Args:
        message (str): The message to display when the page closes. If
            omitted, the default message (set in the Project Properties)
            is shown. Optional.
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageID (str): Identifier of the page to be closed. If omitted,
            the current pageId is used. Optional.
    """
    builtins.print(message, sessionId, pageID)


def closePopup(id, sessionId="current_session", pageId="current_page"):
    """Closes a popup View.

    Args:
        id (str): The unique identifier for the the popup, given to the
            popup when first opened. If given an empty string, then the
            most recently focused popup will be closed.
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(id, sessionId, pageId)


def closeSession(message=None, sessionId="current_session"):
    """Closes the Perspective Session with the given session ID or the
    current session if no ID is provided.

    If a message is provided, it is displayed on the page when the
    session closes. Otherwise the default message (set in the Project
    Properties) is displayed.

    Args:
        message (str): The message to display when the session closes.
            If omitted, the default message (set in the Project
            Properties) is shown. Optional.
        sessionId (str): Identifier of the session to be closed. If
            omitted, the current sessionId is used. Optional.
    """
    builtins.print(message, sessionId)


def download(
    filename,
    data,
    contentType=None,
    sessionId="current_session",
    pageId="current_page",
):
    """Downloads data from the gateway to a device running a session.

    Args:
        filename (str): Suggested name for the downloaded file.
        data (object): The data to be downloaded. May be a String, a
            byte[], or an InputStream. Strings will be written with in
            "utf-8" encoding.
        contentType (str): Value for the "Content-Type" header. Example:
            "text/plain; charset=utf-8". Optional.
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(filename, data, contentType, sessionId, pageId)


def getProjectInfo(projectName):
    """Returns a dictionary of meta data from a Perspective Project.

    Args:
        projectName (str): The name of the project.

    Returns:
        dict: A dictionary of project meta data.
    """
    builtins.print(projectName)
    return {
        "name": "Project",
        "title": "Project",
        "description": "Project's description",
        "lastModified": "2021-04-01T13:37:00.000Z",
        "lastModifiedBy": "thecesrom",
        "views": [{"path": "Page/Home"}],
    }


def getSessionInfo(usernameFilter=None, projectFilter=None):
    """Returns information about one or more Perspective sessions.

    The information returned by this function is a combination of
    information available on the perspective sessions status page on the
    Gateway, and some session props (id and userAgent).

    Args:
        usernameFilter (str): A filter based on logged in user.
            Optional.
        projectFilter (str): A filter based on the project name.
            Optional.

    Returns:
        list[PyJsonObjectAdapter]: A list of objects
            (PyJsonObjectAdapter).
    """
    builtins.print(usernameFilter, projectFilter)
    return [PyJsonObjectAdapter(None)]


def isAuthorized(isAllOf, securityLevels, sessionId="current_session"):
    """Checks if the user in the current session is authorized against a
    target collection of security levels.

    Args:
        isAllOf (bool): True if the current user must have all of the
            given security levels to be authorized. False if the current
            user must have at least one of the given security levels to
            be authorized.
        securityLevels (list[str]): An array of string paths to a
            security level node in the form of "Path/To/Node". Each
            level in the tree is delimited by a forward slash character.
            The public node is never a part of the path.
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            Optional.

    Returns:
        bool: True if the user in the current session is authorized,
            False otherwise.
    """
    builtins.print(isAllOf, securityLevels, sessionId)
    return True


def login(sessionId="current_session", pageId="current_page", forceAuth=False):
    """Triggers a login event that will allow the user to login with the
    project's configured Identity Provider (IdP).

    For this function to work, an Identity Provider must be set in
    Perspective project properties. This is particularly useful when you
    want it to be possible to start a session without authentication and
    sign in to access certain restricted features.

    Args:
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        forceAuth (bool): Determines if Ignition should ask the Identity
            Provider to re-authenticate the user, even if the user is
            already signed into the Identity Provider. If set to True,
            then the Identity Provider will ask the user to re-enter
            their credentials. If set to False, then the Gateway will
            request that the Identity Provider use the last provided
            credentials for the session, potentially allowing
            re-authentication without requiring the user to re-type
            their credentials. Note that support for this argument is
            determined by the Identity Provider; the IdP may choose to
            ignore this request. If this parameter is omitted, then the
            function will use the re-authentication setting defined
            under Project Properties. Optional.
    """
    builtins.print(sessionId, pageId, forceAuth)


def logout(sessionId="current_session", pageId="current_page"):
    """Triggers a logout event, which will log the user out.

    For this function to work, an Identity Provider must be set in the
    Perspective project properties.

    Args:
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def navigate(
    page,
    url=None,
    view=None,
    params=None,
    sessionId="current_session",
    pageId="current_page",
    newTab=False,
):
    """Navigate the session to a specified view or mounted page.

    The function can be used in three different ways, depending on which
    parameter is specified:
        page: navigates to a perspective-page
        url: navigates to a web address, so the function can be used to
            navigate the user to a web portal, search engine, or other
            website. This parameter is specified via keyword argument
        view: navigates to a view. Note that using this parameter does
            not modify the web browser's address bar, so the browser's
            history will not contain a listing for the new view. This
            parameter is specified via keyword argument

    Args:
        page (str): The URL of a Perspective page to navigate to.
        url (str): The URL of a web address to navigate to. If the page
            or view parameters are specified, then this parameter is
            ignored.
        view (str): If specified, will navigate to a specific view.
            Navigating to a view via this parameter does not change the
            address in the web browser. Thus the web browser's back
            button will not be able to return the user to the previous
            view. If the page parameter is specified, then this
            parameter is ignored. Optional.
        params (dict): Used only in conjunction with the view parameter,
            Dictionary of values to pass to any parameters on the view.
            Optional.
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        newTab (bool): If True, opens the contents in a new tab.
            Optional.
    """
    builtins.print(page, url, view, params, sessionId, pageId, newTab)


def navigateBack(sessionId=None, pageId=None):
    """Navigate the session to a specified view or mounted page.

    This is similar to a browser's "back" function.

    Args:
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            Optional.
        pageId (str): Identifier of the page to target. If omitted, the
            current page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def navigateForward(sessionId=None, pageId=None):
    """Navigate the session to a specified view or mounted page.

    This is similar to a browser's "forward" function.

    Args:
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the page to target. If omitted, the
            current page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def openDock(
    id, sessionId="current_session", pageId="current_page", params=None
):
    """Opens a docked View.

    Requires the preconfigured dock ID for the view.

    Args:
        id (str): The unique, preconfigured 'Dock ID' for the docked
            View. Is specified when a View is assigned as docked for a
            particular Page (in Page Configuration).
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        params (dict): Parameters that can be passed into the docked
            view. Must match the docked views View Parameters. Optional.
    """
    builtins.print(id, sessionId, pageId, params)


def openPopup(
    id,
    view,
    params=None,
    title="",
    position=None,
    showCloseIcon=True,
    draggable=True,
    resizable=False,
    modal=False,
    overlayDismiss=False,
    sessionId="current_session",
    pageId="current_page",
    viewPortBound=False,
):
    """Open a popup view over the given page.

    Args:
        id (str): A unique popup string. Will be used to close the popup
            from other popup or script actions.
        view (str): The path to the View to use in the popup.
        params (dict): Dictionary of key-value pairs to us as input
            parameters to the View. Optional.
        title (str): Text to display in the title bar. If no value or an
            empty string are given, the title bar will not be displayed.
            Defaults to an empty string. Optional.
        position (dict): Dictionary of key-value pairs to use for
            position. Possible position keys are: left, top, right,
            bottom, width, height. Defaults to the center of the window.
            Optional.
        showCloseIcon (bool): Will show the close icon if True. Defaults
            to True. Optional.
        draggable (bool): Will allow the popup to be dragged if True.
            Defaults to True. Optional.
        resizable (bool): Will allow the popup to be resized if True.
            Defaults to False. Optional.
        modal (bool): Will make the popup modal if True. A modal popup
            is the only view the user can interact with. Defaults to
            False. Optional.
        overlayDismiss (bool): Will allow the user to dismiss and close
            a modal popup by clicking outside of it if True. Defaults to
            False. Optional.
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        viewPortBound (bool): If True, popups will be "shifted" to open
            within the bounds of the viewport. If the popup would be
            larger than the viewport, then it will be resized to fit
            within the bounds. Default is False. Optional.
    """
    builtins.print(
        id,
        view,
        params,
        title,
        position,
        showCloseIcon,
        draggable,
        resizable,
        modal,
        overlayDismiss,
        sessionId,
        pageId,
        viewPortBound,
    )


def print(
    message,
    sessionId="current_session",
    pageId="current_page",
    destination="client",
):
    """Sends print statements to the scripting console when in the
    Designer.

    When in a Session, sends print statements to the output console.
    This function makes scripting diagnostics easier.

    Args:
        message (str): The print statement that will be displayed on the
            console.
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        destination (str): Where the message should be printed. If
            specified, must be "client", "gateway", or "all". Default is
            "client". Optional.
    """
    builtins.print(message, sessionId, pageId, destination)


def refresh(sessionId="current_session", pageId="current_page"):
    """Triggers a refresh of the page.

    Args:
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(sessionId, pageId)


def sendMessage(
    messageType,
    payload,
    scope="page",
    sessionId="current_session",
    pageId="current_page",
):
    """Send a message to a message handler within the same session.

    Args:
        messageType (str): The message type that will be invoked.
            Message handlers configured within the project are listening
            for messages of a specific messageType.
        payload (dict): A python dictionary representing any parameters
            that will be passed to the message handler.
        scope (str): The scope that the message should be delivered to.
            Valid values are "session", "page", or "view". If omitted,
            "page" will be used. Optional.
        sessionId (str): Identifier of the Session to target. If
            omitted, the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(messageType, payload, scope, sessionId, pageId)


def setTheme(name, sessionId="current_session", pageId="current_page"):
    """Changes the theme in a page to the specified theme.

    Note that this function only changes the theme for a single page,
    not the entire session. To change the theme for a session, write
    directly to the session.theme property instead.

    Args:
        name (str): The theme name to switch to. Possible values are
            "dark" or "light".
        sessionId (str): Identifier of the Session to target. If
            omitted the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
    """
    builtins.print(name, sessionId, pageId)


def toggleDock(
    id, sessionId="current_session", pageId="current_page", params=None
):
    """Toggles a docked View.

    Args:
        id (str): The unique, preconfigured 'Dock ID' for the docked
            View. Is specified when a View is assigned as docked for a
            particular Page (in Page Configuration).
        sessionId (str): Identifier of the Session to target. If
            omitted the current Session will be used automatically.
            When targeting a different session, then the pageId
            parameter must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        params (dict): Parameters that can be passed into the docked
            view. Must match the docked views View Parameters. Optional.
    """
    builtins.print(id, sessionId, pageId, params)


def togglePopup(
    id,
    view,
    params,
    title="",
    position=None,
    showCloseIcon=True,
    draggable=True,
    resizable=False,
    modal=False,
    overlayDismiss=False,
    sessionId="current_session",
    pageId="current_page",
    viewPortBound=False,
):
    """Toggles a popup.

    Will open up the popup if it has not been opened yet. Otherwise, it
    will close the currently opened popup.

    Args:
        id (str): A unique popup string. Will be used to close the popup
            from other popup or script actions.
        view (str): The path to the View to use in the popup.
        params (dict): Dictionary of key-value pairs to us as input
            parameters to the View. Optional.
        title (str): Text to display in the title bar. If no value or an
            empty string are given, the title bar will not be displayed.
            Defaults to an empty string. Optional.
        position (dict): Dictionary of key-value pairs to use for
            position. Possible position keys are: left, top, right,
            bottom, width, height. Defaults to the center of the window.
            Optional.
        showCloseIcon (bool): Will show the close icon if True. Defaults
            to True. Optional.
        draggable (bool): Will allow the popup to be dragged if True.
            Defaults to True. Optional.
        resizable (bool): Will allow the popup to be resized if True.
            Defaults to False. Optional.
        modal (bool): Will make the popup modal if True. A modal popup
            is the only view the user can interact with. Defaults to
            False. Optional.
        overlayDismiss (bool): Will allow the user to dismiss and close
            a modal popup by clicking outside of it if True. Defaults to
            False. Optional.
        sessionId (str): Identifier of the Session to target. If omitted
            the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
        pageId (str): Identifier of the Page to target. If omitted, the
            current Page will be used automatically. Optional.
        viewPortBound (bool): If True, popups will be "shifted" to open
            within the bounds of the viewport. If the popup would be
            larger than the viewport, then it will be resized to fit
            within the bounds. Default is False. Optional.
    """
    builtins.print(
        id,
        view,
        params,
        title,
        position,
        showCloseIcon,
        draggable,
        resizable,
        modal,
        overlayDismiss,
        sessionId,
        pageId,
        viewPortBound,
    )


def vibrateDevice(duration, sessionId="current_session"):
    """When called from the Perspective mobile app, will cause the
    device to vibrate for the specified number of milliseconds.

    Args:
        duration (int): The duration in milliseconds to vibrate the
            device.
        sessionId (str): Identifier of the Session to target. If
            omitted the current Session will be used automatically. When
            targeting a different session, then the pageId parameter
            must be included in the call. Optional.
    """
    builtins.print(duration, sessionId)
