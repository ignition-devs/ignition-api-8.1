# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Net module."""

__all__ = [
    'send_high_priority_email',
    'send_html_email',
    'send_plain_text_email'
]

import system.net
from incendium import constants

HTML_ESCAPE_TABLE = {
    '&': '&amp;',
    '"': '&quot;',
    "'": '&apos;',
    '>': '&gt;',
    '<': '&lt;',
    '\n': '<br />',
    '\t': '&nbsp;' * 4
}


def _html_escape(text):
    """Produce entities within text."""
    return "".join(HTML_ESCAPE_TABLE.get(c, c) for c in text)


def _send_email(subject, body, html, to, priority):
    """Sends an email through the given SMTP server.

    Args:
        subject (str): The subject line for the email.
        body (str): The body text of the email.
        html (bool): A flag indicating whether or not to send the
            email as an HTML email. Will auto-detect if omitted.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority for the message.
    """
    try:
        system.net.sendEmail(
            smtp=constants.SMTP,
            fromAddr=constants.SENDER,
            subject=subject,
            body=body,
            html=html,
            to=to,
            priority=priority
        )
    finally:
        pass


def report_error(subject, message, details, to):
    """Sends an Error Report email message.

    Args:
        subject (str): The subject line for the email.
        message (str): The error message.
        details (str): The error details.
        to (list[str]): A list of emails addresses to send to.
    """
    body = constants.ERROR_REPORT % (message, _html_escape(details))
    send_high_priority_email(subject, body, to)


def send_high_priority_email(subject, body, to):
    """Sends a High Priority email.

    Args:
        subject (str): The subject line for the email.
        body (str): The body text of the email.
        to (list[str]): A list of email addresses to send to.
    """
    send_html_email(subject, body, to, '1')


def send_html_email(subject, body, to, priority='3'):
    """Sends an email in HTML format.

    Args:
        subject (str): The subject line for the email.
        body (str): The body text of the email in HTML format.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority of the message, from "1" to "5",
            with "1" being highest priority. Defaults to "3" (normal)
            priority. Optional.
    """
    _send_email(subject, body, True, to, priority)


def send_plain_text_email(subject, body, to, priority='3'):
    """Sends an email in plain text format.

    Args:
        subject (str): The subject line for the email.
        body (str): The body text of the email in HTML format.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority of the message, from "1" to "5",
            with "1" being highest priority. Defaults to "3" (normal)
            priority. Optional.
    """
    _send_email(subject, body, False, to, priority)
