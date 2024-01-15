"""
 IView.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import ABC, abstractmethod
from typing import Any

from .IMediator import IMediator
from .INotification import INotification
from .IObserver import IObserver


class IView(ABC):

    @abstractmethod
    def register_observer(self, notification_name: str, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self, notification: INotification) -> None:
        pass

    @abstractmethod
    def remove_observer(self, notification_name: str, notify_context: Any) -> None:
        pass

    @abstractmethod
    def register_mediator(self, mediator: IMediator) -> None:
        pass

    @abstractmethod
    def retrieve_mediator(self, mediator_name: str) -> IMediator:
        pass

    @abstractmethod
    def has_mediator(self, mediator_name: str) -> bool:
        pass

    @abstractmethod
    def remove_mediator(self, mediator_name: str) -> IMediator:
        pass
