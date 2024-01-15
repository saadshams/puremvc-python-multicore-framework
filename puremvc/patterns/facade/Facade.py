import threading
from typing import Dict, Callable, Any

from puremvc.core import Controller, Model, View
from puremvc.interfaces import IFacade, INotification, ICommand, IProxy, IMediator, IController, IModel, IView
from puremvc.patterns.observer import Notification


class Facade(IFacade):
    instanceMap: Dict[str, IFacade] = dict()
    instanceMapLock = threading.Lock()

    MULTITON_MSG = "Facade instance for this Multiton key already constructed!"

    def __init__(self, key: str):
        if Facade.instanceMap.get(key) is not None:
            raise Exception(Facade.MULTITON_MSG)
        self.multitonKey = None
        self.controller = None
        self.model = None
        self.view = None
        self.initialize_notifier(key)
        Facade.instanceMap[key] = self
        self.initialize_facade()

    def initialize_facade(self) -> None:
        self.initialize_model()
        self.initialize_controller()
        self.initialize_view()

    @classmethod
    def get_instance(cls, key: str, factory: Callable[[str], IFacade]) -> IFacade:
        with cls.instanceMapLock:
            if key not in cls.instanceMap:
                cls.instanceMap[key] = factory(key)
        return cls.instanceMap.get(key)

    def initialize_controller(self) -> None:
        self.controller: IController = Controller.get_instance(self.multitonKey, lambda k: Controller(k))

    def initialize_model(self) -> None:
        self.model: IModel = Model.get_instance(self.multitonKey, lambda k: Model(k))

    def initialize_view(self) -> None:
        self.view: IView = View.get_instance(self.multitonKey, lambda k: View(k))

    def register_command(self, notification_name: str, factory: Callable[[str], ICommand]) -> None:
        self.controller.register_command(notification_name, factory)

    def has_command(self, notification_name: str) -> bool:
        return self.controller.has_command(notification_name)

    def remove_command(self, notification_name: str) -> None:
        self.controller.remove_command(notification_name)

    def register_proxy(self, proxy: IProxy) -> None:
        self.model.register_proxy(proxy)

    def retrieve_proxy(self, proxy_name: str) -> IProxy:
        return self.model.retrieve_proxy(proxy_name)

    def has_proxy(self, proxy_name: str) -> bool:
        return self.model.has_proxy(proxy_name)

    def remove_proxy(self, proxy_name: str) -> IProxy:
        return self.model.remove_proxy(proxy_name)

    def register_mediator(self, mediator: IMediator) -> None:
        self.view.register_mediator(mediator)

    def retrieve_mediator(self, mediator_name: str) -> IMediator:
        return self.view.retrieve_mediator(mediator_name)

    def has_mediator(self, mediator_name: str) -> bool:
        return self.view.has_mediator(mediator_name)

    def remove_mediator(self, mediator_name: str) -> IMediator:
        return self.view.remove_mediator(mediator_name)

    def send_notification(self, notification_name: str, body: Any = None, note_type: str = None) -> None:
        self.notify_observers(Notification(notification_name, body, note_type))

    def notify_observers(self, notification: INotification) -> None:
        self.view.notify_observers(notification)

    def initialize_notifier(self, key: str) -> None:
        self.multitonKey = key

    @classmethod
    def has_core(cls, key: str) -> bool:
        return cls.instanceMap.get(key) is not None

    @classmethod
    def remove_core(cls, key: str) -> None:
        if cls.instanceMap.get(key) is None:
            return
        Model.remove_model(key)
        View.remove_view(key)
        Controller.remove_controller(key)
        del cls.instanceMap[key]
