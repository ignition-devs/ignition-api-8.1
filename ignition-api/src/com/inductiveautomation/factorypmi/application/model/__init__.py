from __future__ import print_function

__all__ = ["TemplateManager"]

from com.inductiveautomation.ignition.client.model import ClientContext
from java.lang import Object


class TemplateManager(Object):
    def __init__(self, context):
        # type: (ClientContext) -> None
        super(TemplateManager, self).__init__()
        print(context)
