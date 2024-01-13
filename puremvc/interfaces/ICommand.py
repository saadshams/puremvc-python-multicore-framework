from abc import ABC, abstractmethod

from puremvc.interfaces import INotification


class ICommand(ABC):

    @abstractmethod
    def execute(self, notification: INotification) -> None:
        pass
