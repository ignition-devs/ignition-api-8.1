"""Twilio Functions.

The following functions give you access to read info and send SMS
through Twilio. This requires the Twilio Module, which is not included
in a typical install.
"""

from __future__ import print_function

__all__ = [
    "getAccounts",
    "getAccountsDataset",
    "getPhoneNumbers",
    "getPhoneNumbersDataset",
    "sendSms",
]

from typing import List

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String


def getAccounts():
    # type: () -> List[String]
    """Return a list of Twilio accounts that have been configured in the
    Gateway.

    Returns:
        A list of configured Twilio accounts.
    """
    return ["twilio_account1", "twilio_account2"]


def getAccountsDataset():
    # type: () -> BasicDataset
    """Return a list of Twilio accounts that have been configured in the
    Gateway as a single-column Dataset.

    Returns:
        A list of configured Twilio accounts as a single-column Dataset.
    """
    return BasicDataset()


def getPhoneNumbers(accountName):
    # type: (String) -> List[String]
    """Returns a list of outgoing phone numbers for a Twilio account.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName: The Twilio account to retrieve phone numbers for.

    Returns:
        A list of phone numbers for the given Twilio account.
    """
    phoneNumbers = []  # type: List[String]
    if accountName == "Jenny":
        phoneNumbers.append("+12058675309")
    return phoneNumbers


def getPhoneNumbersDataset(accountName):
    # type: (String) -> BasicDataset
    """Return a list of outgoing phone numbers for a Twilio account as a
    single-column Dataset.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName: The Twilio account to retrieve phone numbers for.

    Returns:
        A list of phone numbers for the given Twilio account as a
        single-column Dataset.
    """
    print(accountName)
    return BasicDataset()


def sendSms(accountName, fromNumber, toNumber, message):
    # type: (String, String, String, String) -> None
    """Sends an SMS message.

    Args:
        accountName: The Twilio account to send the SMS from.
        fromNumber: The outbound phone number belonging to the Twilio
            account to use.
        toNumber: The phone number of the recipient.
        message: The body of the SMS.
    """
    print(accountName, fromNumber, toNumber, message)
