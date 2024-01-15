"""
 IObserver.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import ABC, abstractmethod
from typing import Any, Callable

from .INotification import INotification


class IObserver(ABC):

    @property
    @abstractmethod
    def notify_method(self) -> Callable[[INotification], None]:
        pass

    @notify_method.setter
    @abstractmethod
    def notify_method(self, value: Callable[[INotification], None]) -> None:
        pass

    @property
    @abstractmethod
    def notify_context(self) -> Any:
        pass

    @notify_context.setter
    @abstractmethod
    def notify_context(self, value: Any) -> None:
        pass

    @abstractmethod
    def notify_observer(self, notification: INotification) -> None:
        pass

    @abstractmethod
    def compare_notify_context(self, obj: Any) -> bool:
        pass
