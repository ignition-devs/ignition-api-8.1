from __future__ import print_function

from typing import Any

from java.lang import Object


class ProjectTagManager(Object):
    def __init__(self, parent):
        # type: (Any) -> None
        super(ProjectTagManager, self).__init__()
        print(parent)
