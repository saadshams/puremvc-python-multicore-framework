from abc import ABC, abstractmethod
from typing import Callable

from .ICommand import ICommand
from .INotification import INotification


class IController(ABC):

    @abstractmethod
    def register_command(self, notification_name: str, factory: Callable[[], ICommand]) -> None:
        pass

    @abstractmethod
    def execute_command(self, notification: INotification) -> None:
        pass

    @abstractmethod
    def has_command(self, notification_name: str) -> bool:
        pass

    @abstractmethod
    def remove_command(self, notification_name: str) -> None:
        pass
