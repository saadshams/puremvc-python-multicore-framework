from puremvc.interfaces import INotification, ICommand
from puremvc.patterns.observer import Notifier


class SimpleCommand(Notifier, ICommand):
    def execute(self, notification: INotification) -> None:
        return
