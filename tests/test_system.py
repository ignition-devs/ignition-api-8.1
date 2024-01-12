# pylint: skip-file
import importlib
import sys

MODULES = sys.modules.keys()


def _cleanup():
    for module in sys.modules.keys():
        if module not in MODULES:
            sys.modules.pop(module)


def test_alarm():
    module_name = "system.alarm"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_bacnet():
    module_name = "system.bacnet"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_bacnet_enumerated():
    module_name = "system.bacnet.enumerated"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_bacnet_enums():
    module_name = "system.bacnet.enums"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_dataset():
    module_name = "system.dataset"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_date():
    module_name = "system.date"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_db():
    module_name = "system.db"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_device():
    module_name = "system.device"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_dnp3():
    module_name = "system.dnp3"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_eam():
    module_name = "system.eam"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_file():
    module_name = "system.file"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_groups():
    module_name = "system.groups"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_gui():
    module_name = "system.gui"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_iec61850():
    module_name = "system.iec61850"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_math():
    module_name = "system.math"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_mongodb():
    module_name = "system.mongodb"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_mongodb_types():
    module_name = "system.mongodb.types"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_nav():
    module_name = "system.nav"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_net():
    module_name = "system.net"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_opc():
    module_name = "system.opc"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_opcua():
    module_name = "system.opcua"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_perspective():
    module_name = "system.perspective"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_perspective_workstation():
    module_name = "system.perspective.workstation"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_project():
    module_name = "system.project"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_report():
    module_name = "system.report"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_roster():
    module_name = "system.roster"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_secsgem():
    module_name = "system.secsgem"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_security():
    module_name = "system.security"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_serial():
    module_name = "system.serial"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_sfc():
    module_name = "system.sfc"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_tag():
    module_name = "system.tag"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_twilio():
    module_name = "system.twilio"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_user():
    module_name = "system.user"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_util():
    module_name = "system.util"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()


def test_vision():
    module_name = "system.vision"

    try:
        imported_module = importlib.import_module(module_name)
    except ImportError:
        assert False, "Failed to import module: {0}".format(module_name)

    assert imported_module is not None, "Module {0} is None after import.".format(
        module_name
    )

    _cleanup()
