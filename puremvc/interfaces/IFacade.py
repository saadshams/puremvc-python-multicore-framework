"""
 IFacade.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import ABC, abstractmethod
from typing import Any, Callable

from .ICommand import ICommand
from .IMediator import IMediator
from .INotification import INotification
from .INotifier import INotifier
from .IProxy import IProxy


class IFacade(INotifier, ABC):

    @abstractmethod
    def register_proxy(self, proxy: IProxy) -> None:
        pass

    @abstractmethod
    def retrieve_proxy(self, proxy_name: str) -> IProxy:
        pass

    @abstractmethod
    def remove_proxy(self, proxy_name: str) -> IProxy:
        pass

    @abstractmethod
    def has_proxy(self, proxy_name: str) -> bool:
        pass

    @abstractmethod
    def register_command(self, notification_name: str, factory: Callable[[], ICommand]) -> None:
        pass

    @abstractmethod
    def has_command(self, notification_name: str) -> bool:
        pass

    @abstractmethod
    def remove_command(self, notification_name: str) -> None:
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

    @abstractmethod
    def notify_observers(self, notification: INotification) -> None:
        pass
