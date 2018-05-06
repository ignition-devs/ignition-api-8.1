# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,R0913

"""Net Functions
The following functions give you access to interact with http services."""

__all__ = [
    'httpGet',
    'sendEmail'
]


def httpGet(url, connectTimeout=10000, readTimeout=60000, username=None, password=None,
            headerValues=None, bypassCertValidation=None, useCaches=True, throwOnError=True):
    """Retrieves the document at the given URL using the HTTP GET protocol. The document is
    returned as a string. For example, if you use the URL of a website, you'll get the same
    thing you'd get by going to that website in a browser and using the browser's "View Source"
    function.

    Args:
        url (str): The URL to retrieve.
        connectTimeout (int): The timeout for connecting to the URL. In milliseconds. Default is
            10,000. Optional.
        readTimeout (int): The read timeout for the get operation. In milliseconds. Default is
            60,000. Optional.
        username (str): If specified, the call will attempt to authenticate with basic HTTP
            authentication. Optional.
        password (str): The password used for basic HTTP authentication, if the username
            parameter is also present. Optional.
        headerValues (dict): A dictionary of name/value pairs that will be set in the HTTP
            header. Optional.
        bypassCertValidation (bool): If the target address is an HTTPS address, and this
            parameter is True, the system will bypass all SSL certificate validation. This is not
            recommended, though is sometimes necessary for self-signed certificates. Optional.
        useCaches (bool): Will cache the information returned by the httpGet call. If using this
            for something that constantly updates like an rss feed, it would be better to set
            this to False. Default is True. Optional.
        throwOnError (bool): Set to False if you wish to get the error body rather than a Python
            exception if the GET request returns an error code (non-200 responsive). Default is
            True. Optional.

    Returns:
        str: The content found at the given URL.
    """
    print(url, connectTimeout, readTimeout, username, password, headerValues,
          bypassCertValidation, useCaches, throwOnError)
    return ''


def sendEmail(smtp, fromAddr, subject, body, html, to, priority='3'):
    """Sends an email through the given SMTP server. Note that this email is relayed first through
    the Gateway - the client host machine doesn't need network access to the SMTP server.

    Args:
        smtp (str): The address of an SMTP server to send the email through, like
            "mail.example.com". A port can be specified, like "mail.example.com:25". SSL can also
            be forced, like "mail.example.com:25:tls".
        fromAddr (str): An email address to have the email come from.
        subject (str): The subject line for the email
        body (str): The body text of the email.
        html (bool): A flag indicating whether or not to send the email as an HTML email. Will
            auto-detect if omitted.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority for the message, from "1" to "5", with "1" being highest
            priority. Defaults to "3" (normal) priority. Optional.
    """
    print(smtp, fromAddr, subject, body, html, to, priority)
