from abc import ABC, abstractmethod

from .INotifier import INotifier
from puremvc.interfaces import INotification


class ICommand(INotifier):

    @abstractmethod
    def execute(self, notification: INotification) -> None:
        pass
