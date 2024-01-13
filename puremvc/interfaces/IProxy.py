from abc import ABC, abstractmethod
from typing import Any


class IProxy(ABC):

    @property
    @abstractmethod
    def proxy_name(self) -> str:
        pass

    @property
    @abstractmethod
    def data(self) -> Any:
        pass

    @abstractmethod
    def on_register(self) -> None:
        pass

    @abstractmethod
    def on_remove(self) -> None:
        pass
