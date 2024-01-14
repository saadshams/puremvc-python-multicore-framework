from abc import ABC, abstractmethod
from typing import Any

from .INotifier import INotifier
from puremvc.interfaces.INotification import INotification


class IMediator(INotifier):

    @property
    @abstractmethod
    def mediator_name(self) -> str:
        pass

    @property
    @abstractmethod
    def view_component(self) -> Any:
        pass

    @abstractmethod
    def list_notification_interests(self) -> [str]:
        pass

    @abstractmethod
    def handle_notification(self, notification: INotification) -> None:
        pass

    @abstractmethod
    def on_register(self) -> None:
        pass

    @abstractmethod
    def on_remove(self) -> None:
        pass
