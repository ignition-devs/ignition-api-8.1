from typing import Any, Dict, List, Tuple

from dev.coatl.helper.types import AnyStr

def addConnection(
    name: AnyStr,
    description: AnyStr,
    discoveryUrl: AnyStr,
    endpointUrl: AnyStr,
    securityPolicy: AnyStr,
    securityMode: AnyStr,
    settings: Dict[AnyStr, Any],
) -> None: ...
def callMethod(
    connectionName: AnyStr, objectId: AnyStr, methodId: AnyStr, inputs: List[Any]
) -> Tuple[Any, Any, Any]: ...
def removeConnection(name: AnyStr) -> bool: ...
