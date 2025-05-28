__all__ = [
    "create_import_test",
    "discover_all_modules_in_path",
    "find_modules_in_path",
    "pop_imported_modules",
]

import os
import sys


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


def discover_all_modules_in_path(path):
    return list(find_modules_in_path(path))


def pop_imported_modules(modules):
    for module in list(sys.modules.keys()):
        if module not in modules:
            sys.modules.pop(module)


def create_import_test(module_name):
    def test(self):
        self.assertModuleAvailable(module_name)

    return test
