from abc import ABC, abstractclassmethod
from typing import List
from .enum import HealthCheckStatusEnum


class HealthCheckInterface(ABC):
    _connectionUri: str
    _alias: str
    #_service: str
    _tags: List[str]

    @abstractclassmethod
    def setConnectionUri(self, value: str) -> None:
        """ConnectionUri will be the value that is requested to check the health of an endpoint."""
        pass

    @abstractclassmethod
    def setName(self, value: str) -> None:
        """The Name is the friendly name of the health object."""
        pass

    @abstractclassmethod
    def getService(self) -> str:
        """The Service is a definition of what kind of endpoint we are checking on."""
        pass

    @abstractclassmethod
    def getTags(self) -> List[str]:
        pass

    @abstractclassmethod
    def __checkHealth__(self) -> HealthCheckStatusEnum:
        """Requests data from the endpoint to validate health."""
        pass
    


