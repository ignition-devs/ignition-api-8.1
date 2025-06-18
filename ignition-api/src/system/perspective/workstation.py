"""Perspective Workstation Functions.

The following functions offer various ways to interact with Perspective
Workstation from a Python script. Note that the functions here only work
when called from a session running in Perspective Workstation.
"""

__all__ = ["exit", "toKiosk", "toWindowed"]


def exit():
    # type: () -> None
    """When called from a session running in Workstation, this function
    will close Workstation.
    """
    pass


def toKiosk():
    # type: () -> None
    """When called from a session running in Perspective Workstation,
    attempts to put Workstation into Kiosk mode.
    """
    pass


def toWindowed():
    # type: () -> None
    """When called from a Session running in Perspective Workstation,
    attempts to put Workstation into windowed mode.
    """
    pass
