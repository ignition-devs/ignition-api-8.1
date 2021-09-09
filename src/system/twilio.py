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

from system.dataset import Dataset


def getAccounts():
    """Return a list of Twilio accounts that have been configured in the
    Gateway.

    Returns:
        list[str]: A list of configured Twilio accounts.
    """
    return ["twilio_account1", "twilio_account2"]


def getAccountsDataset():
    """Return a list of Twilio accounts that have been configured in the
    Gateway as a single-column Dataset.

    Returns:
        Dataset: A list of configured Twilio accounts as a single-column
            Dataset.
    """
    return Dataset()


def getPhoneNumbers(accountName):
    """Returns a list of outgoing phone numbers for a Twilio account.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName (str): The Twilio account to retrieve phone numbers
            for.

    Returns:
        list[str]: A list of phone numbers for the given Twilio account.
    """
    phoneNumbers = []
    if accountName == "Jenny":
        phoneNumbers.append("+12058675309")
    return phoneNumbers


def getPhoneNumbersDataset(accountName):
    """Return a list of outgoing phone numbers for a Twilio account as a
    single-column Dataset.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName (str): The Twilio account to retrieve phone numbers
            for.

    Returns:
        Dataset: A list of phone numbers for the given Twilio account as
            a single-column Dataset.
    """
    print(accountName)
    return Dataset()


def sendSms(accountName, fromNumber, toNumber, message):
    """Sends an SMS message.

    Args:
        accountName (str): The Twilio account to send the SMS from.
        fromNumber (str): The outbound phone number belonging to the
            Twilio account to use.
        toNumber (str): The phone number of the recipient.
        message (str): The body of the SMS.
    """
    print(accountName, fromNumber, toNumber, message)
