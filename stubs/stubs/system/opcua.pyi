from typing import Any, Dict, List, Tuple, Union

def addConnection(
    name: Union[str, unicode],
    description: Union[str, unicode],
    discoveryUrl: Union[str, unicode],
    endpointUrl: Union[str, unicode],
    securityPolicy: Union[str, unicode],
    securityMode: Union[str, unicode],
    settings: Dict[Union[str, unicode], Any],
) -> None: ...
def callMethod(
    connectionName: Union[str, unicode],
    objectId: Union[str, unicode],
    methodId: Union[str, unicode],
    inputs: List[Any],
) -> Tuple[Any, Any, Any]: ...
def removeConnection(name: Union[str, unicode]) -> bool: ...
