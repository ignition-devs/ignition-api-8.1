from typing import Union

from java.awt import Container

class JTextComponent(Container):
    def getText(self, *args: int) -> Union[str, unicode]: ...
    def setText(self, t: Union[str, unicode]) -> None: ...
