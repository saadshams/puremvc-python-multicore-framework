from puremvc.interfaces import INotification, ICommand


class SimpleCommand(ICommand):

    def execute(self, notification: INotification) -> None:
        pass
