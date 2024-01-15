import threading
from typing import Dict, List, Callable, Any

from puremvc.interfaces import IView, IMediator, IObserver, INotification
from puremvc.patterns.observer import Observer


class View(IView):
    instanceMap: Dict[str, IView] = dict()
    instanceMapLock: threading.Lock = threading.Lock()

    MULTITON_MSG = "View multiton instance for this key is already constructed!"

    def __init__(self, key: str):
        if View.instanceMap.get(key) is not None:
            raise Exception(View.MULTITON_MSG)
        self.multitonKey: str = key
        View.instanceMap[key] = self
        self.mediatorMap: Dict[str, IMediator] = dict()
        self.observerMap: Dict[str, List[IObserver]] = dict()
        self.initialize_view()

    @classmethod
    def get_instance(cls, key: str, factory: Callable[[str], IView]) -> IView:
        with cls.instanceMapLock:
            if key not in cls.instanceMap:
                cls.instanceMap[key] = factory(key)
        return cls.instanceMap.get(key)

    def initialize_view(self) -> None:
        return

    def register_observer(self, notification_name: str, observer: IObserver) -> None:
        if notification_name in self.observerMap:
            self.observerMap[notification_name].append(observer)
        else:
            self.observerMap[notification_name] = [observer]

    def notify_observers(self, notification: INotification) -> None:
        observers = self.observerMap.get(notification.name)
        if observers:
            for observer in observers[:]:
                observer.notify_observer(notification)

    def remove_observer(self, notification_name: str, notify_context: Any) -> None:
        observers = self.observerMap.get(notification_name)

        for i, observer in enumerate(observers):
            if observer.compare_notify_context(notify_context):
                observers.pop(i)
                break

        if len(observers) == 0:
            del self.observerMap[notification_name]

    def register_mediator(self, mediator: IMediator) -> None:
        if self.mediatorMap.get(mediator.mediator_name):
            return
        mediator.initialize_notifier(self.multitonKey)
        self.mediatorMap[mediator.mediator_name] = mediator

        interests = mediator.list_notification_interests()
        if interests:
            observer = Observer(mediator.handle_notification, mediator)
            for interest in interests:
                self.register_observer(interest, observer)
        mediator.on_register()

    def retrieve_mediator(self, mediator_name: str) -> IMediator:
        return self.mediatorMap.get(mediator_name)

    def has_mediator(self, mediator_name: str) -> bool:
        return self.mediatorMap.get(mediator_name) is not None

    def remove_mediator(self, mediator_name: str) -> IMediator:
        mediator = self.mediatorMap.get(mediator_name)
        if mediator:
            for interest in mediator.list_notification_interests():
                self.remove_observer(interest, mediator)

            del self.mediatorMap[mediator_name]
            mediator.on_remove()

        return mediator

    @classmethod
    def remove_view(cls, key: str) -> None:
        with cls.instanceMapLock:
            del cls.instanceMap[key]
