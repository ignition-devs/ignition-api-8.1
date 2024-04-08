import importlib
import pkgutil
import sys
import unittest

_SYS_MODULES = sys.modules.keys()
_MODULES = []


def _cleanup():
    for module in sys.modules.keys():
        if module not in _SYS_MODULES:
            sys.modules.pop(module)


def _create_import_test(module_name):
    def test(self):
        self.assertModuleAvailable(module_name)

    return test


def _discover_modules(package):
    for _, name, is_pkg in pkgutil.walk_packages(["src/{}".format(package)]):
        if is_pkg:
            _module = "{}.{}".format(package, name)
            _MODULES.append(_module)
            _discover_modules("{}/{}".format(package, name))
        else:
            _module = "{}.{}".format(package, name)
            _MODULES.append(_module.replace("/", "."))
    return _MODULES


class TestPackageImports(unittest.TestCase):
    modules_to_test = _discover_modules("system")

    for module_name in modules_to_test:
        test_name = "test_import_{}".format(module_name)
        locals()[test_name] = _create_import_test(module_name)
        _cleanup()

    def assertModuleAvailable(self, module_name):
        try:
            importlib.import_module(module_name)
        except ImportError:
            self.fail("Failed to import module: {}".format(module_name))


if __name__ == "__main__":
    unittest.main()
