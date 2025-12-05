from typing import List, Union

def loadFromFile(
    filePath: Union[str, unicode], projectName: Union[str, unicode], mode: int
) -> None: ...
def removeGroups(
    projectName: Union[str, unicode], paths: List[Union[str, unicode]]
) -> None: ...
