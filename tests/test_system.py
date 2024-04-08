# pylint: skip-file
import importlib
import sys

import pytest

_MODULES = sys.modules.keys()

_SYSTEM_MODULES = [
    "system.alarm",
    "system.bacnet",
    "system.bacnet.enumerated",
    "system.bacnet.enums",
    "system.dataset",
    "system.date",
    "system.db",
    "system.dnp3",
    "system.eam",
    "system.file",
    "system.groups",
    "system.gui",
    "system.iec61850",
    "system.math",
    "system.mongodb",
    "system.mongodb.types",
    "system.nav",
    "system.net",
    "system.opc",
    "system.opchda",
    "system.opcua",
    "system.perspective",
    "system.perspective.workstation",
    "system.project",
    "system.report",
    "system.roster",
    "system.secsgem",
    "system.security",
    "system.serial",
    "system.sfc",
    "system.tag",
    "system.twilio",
    "system.user",
    "system.util",
    "system.vision",
]


def _cleanup():
    for module in sys.modules.keys():
        if module not in _MODULES:
            sys.modules.pop(module)


@pytest.mark.parametrize("test_module", _SYSTEM_MODULES)
def test_system(test_module):
    try:
        imported_module = importlib.import_module(test_module)
    except ImportError:
        assert False, "Failed to import module: {0}".format(test_module)

    assert imported_module is not None, "Module {0} is None after import.".format(
        test_module
    )

    _cleanup()
