from typing import Any

from puremvc.interfaces import IFacade, INotifier
from puremvc.patterns.facade import Facade


class Notifier(INotifier):
    MULTITON_MSG = "multitonKey for this Notifier not yet initialized!"

    def __init__(self):
        self.multitonKey = None

    def send_notification(self, notification_name: str, body: Any = None, note_type: str = None) -> None:
        self.facade.send_notification(notification_name, body, note_type)

    def initialize_notifier(self, key: str) -> None:
        self.multitonKey = key

    @property
    def facade(self) -> IFacade:
        if self.multitonKey is None:
            raise Exception(self.MULTITON_MSG)
        return Facade.get_instance(self.multitonKey, lambda key: Facade(key))

