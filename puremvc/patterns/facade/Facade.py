import threading
from typing import Dict, Callable, Any

from puremvc.interfaces import IFacade


class Facade(IFacade):
    instanceMap: Dict[str, IFacade] = dict()
    instanceMapLock = threading.Lock()

    MULTITON_MSG = "Facade instance for this Multiton key already constructed!"

    def __init__(self, key: str):
        if Facade.instanceMap.get(key) is not None:
            raise Exception(Facade.MULTITON_MSG)
        self.multitonKey: str = key

    @classmethod
    def get_instance(cls, key: str, factory: Callable[[str], IFacade]) -> IFacade:
        with cls.instanceMapLock:
            cls.instanceMap[key] = factory(key)
        return cls.instanceMap.get(key)

    def send_notification(self, notification_name: str, body: Any = None, note_type: str = None) -> None:
        pass
