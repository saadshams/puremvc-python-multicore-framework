"""
 INotifier.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import abstractmethod, ABC
from typing import Any


class INotifier(ABC):

    @abstractmethod
    def send_notification(self, notification_name: str, body: Any = None, note_type: str = None) -> None:
        pass

    @abstractmethod
    def initialize_notifier(self, key: str) -> None:
        pass
