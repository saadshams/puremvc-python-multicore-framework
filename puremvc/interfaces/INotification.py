"""
 INotification.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import ABC, abstractmethod
from typing import Any


class INotification(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def body(self) -> Any:
        pass

    @body.setter
    @abstractmethod
    def body(self, body: Any) -> None:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @type.setter
    @abstractmethod
    def type(self, note_type: str) -> None:
        pass
