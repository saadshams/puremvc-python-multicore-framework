"""
 Controller.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import threading
from typing import Dict, Callable

from .View import View
from puremvc.interfaces import IController, ICommand, IView, INotification
from puremvc.patterns.observer import Observer


class Controller(IController):
    instanceMap: Dict[str, IController] = dict()
    instanceMapLock: threading.Lock = threading.Lock()

    MULTITON_MSG = "Controller multiton instance for this key is already constructed!"

    def __init__(self, key: str):
        if Controller.instanceMap.get(key) is not None:
            raise Exception(Controller.MULTITON_MSG)
        self.multitonKey: str = key
        Controller.instanceMap[key] = self
        self.commandMap: Dict[str, Callable[[], ICommand]] = dict()
        self.view = None
        self.initialize_controller()

    def initialize_controller(self):
        self.view: IView = View.get_instance(self.multitonKey, lambda key: View(key))

    @classmethod
    def get_instance(cls, key: str, factory: Callable[[str], IController]) -> IController:
        with cls.instanceMapLock:
            if key not in cls.instanceMap:
                cls.instanceMap[key] = factory(key)
        return cls.instanceMap.get(key)

    def register_command(self, notification_name: str, factory: Callable[[], ICommand]) -> None:
        if self.commandMap.get(notification_name) is None:
            self.view.register_observer(notification_name, Observer(self.execute_command, self))
        self.commandMap[notification_name] = factory

    def execute_command(self, notification: INotification) -> None:
        factory = self.commandMap.get(notification.name)
        if factory is None:
            return
        command = factory()
        command.initialize_notifier(self.multitonKey)
        command.execute(notification)

    def has_command(self, notification_name: str) -> bool:
        return self.commandMap.get(notification_name) is not None

    def remove_command(self, notification_name: str) -> None:
        if self.has_command(notification_name):
            self.view.remove_observer(notification_name, self)
            del self.commandMap[notification_name]

    @classmethod
    def remove_controller(cls, key: str) -> None:
        with cls.instanceMapLock:
            del cls.instanceMap[key]
