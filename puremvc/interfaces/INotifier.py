from abc import ABC, abstractmethod
from typing import Any


class INotifier(ABC):

    @abstractmethod
    def send_notification(self, notification_name: str, body: Any = None, note_type: str = None) -> None:
        pass

    @abstractmethod
    def initialize_notifier(self, key: str) -> None:
        pass
