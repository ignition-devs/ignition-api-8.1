from __future__ import print_function

__all__ = ["TemplateManager"]

from java.lang import Object

from com.inductiveautomation.ignition.client.model import ClientContext


class TemplateManager(Object):
    def __init__(self, context):
        # type: (ClientContext) -> None
        super(TemplateManager, self).__init__()
        print(context)
