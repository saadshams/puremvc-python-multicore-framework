from abc import abstractmethod
from typing import Any

from .INotifier import INotifier


class IProxy(INotifier):

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
