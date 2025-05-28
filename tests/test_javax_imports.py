# pylint: skip-file
# sourcery skip: dont-import-test-modules
import importlib
import sys
import unittest

from tests import test_utils

_PATH_TO_MODULES = "src/javax"
_SYS_MODULES = set(sys.modules.keys())


class TestPackageImports(unittest.TestCase):
    modules_to_test = test_utils.discover_all_modules_in_path(_PATH_TO_MODULES)

    for module_name in modules_to_test:
        test_name = "test_import_{}".format(module_name)
        locals()[test_name] = test_utils.create_import_test(module_name)
        test_utils.pop_imported_modules(_SYS_MODULES)

    def assertModuleAvailable(self, module_name):
        try:
            importlib.import_module(module_name)
        except ImportError:
            self.fail("Failed to import module: {}".format(module_name))


if __name__ == "__main__":
    unittest.main()
