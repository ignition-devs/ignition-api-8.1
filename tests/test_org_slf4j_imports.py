# pylint: skip-file
import importlib
import os
import sys
import unittest

_SYS_MODULES = sys.modules.keys()


def find_modules_in_path(path):
    modules = []

    for root, _, files in os.walk(path):
        for file_ in files:
            if file_.endswith(".py"):
                module_path = os.path.relpath(os.path.join(root, file_), path)
                module_name = os.path.splitext(module_path.replace(os.sep, "."))[0]
                _module = "{}.{}".format(
                    path.replace("src/", "").replace("/", "."),
                    module_name.replace(".__init__", ""),
                )
                modules.append(_module)

    return modules


def create_import_test(module_name):
    def test(self):
        self.assertModuleAvailable(module_name)

    return test


def discover_all_modules_in_path(path):
    return list(find_modules_in_path(path))


def pop_imported_modules():
    for module in sys.modules.keys():
        if module not in _SYS_MODULES:
            sys.modules.pop(module)


class TestPackageImports(unittest.TestCase):
    modules_to_test = discover_all_modules_in_path("src/org/slf4j")

    for module_name in modules_to_test:
        test_name = "test_import_{}".format(module_name)
        locals()[test_name] = create_import_test(module_name)
        pop_imported_modules()

    def assertModuleAvailable(self, module_name):
        try:
            importlib.import_module(module_name)
        except ImportError:
            self.fail("Failed to import module: {}".format(module_name))


if __name__ == "__main__":
    unittest.main()
