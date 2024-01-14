from abc import ABC, abstractmethod

from .INotifier import INotifier
from .INotification import INotification


class ICommand(INotifier):

    @abstractmethod
    def execute(self, notification: INotification) -> None:
        pass
