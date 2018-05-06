# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Net module."""

__all__ = [
    'send_high_priority_email',
    'send_html_email'
]

import system.net

SMTP = 'mail.mycompany.com:25'
SENDER = 'no-reply@mycompany.com'


def _send_email(subject, body, html, to, priority):
    """Sends an email through the given SMTP server.

    Args:
        subject (str): The subject line for the email.
        body (str): The body text of the email.
        html (bool): A flag indicating whether or not to send the email as an HTML email. Will
            auto-detect if omitted.
        to (list[str]): A list of email addresses to send to.
        priority (str): Priority for the message.
    """
    try:
        system.net.sendEmail(smtp=SMTP, fromAddr=SENDER, subject=subject, body=body, html=html,
                             to=to, priority=priority)
    finally:
        pass


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
        to (list[str]): A List of email addresses to send to.
        priority (str): Priority of the message, from "1" to "5", with "1" being highest
            priority. Defaults to "3" (normal) priority. Optional.
    """
    _send_email(subject, body, True, to, priority)
