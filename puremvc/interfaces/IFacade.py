from abc import ABC
from typing import Any


class IFacade(ABC):

    def send_notification(self, name: str, body: Any = None, note_type: str = None) -> None:
        pass
