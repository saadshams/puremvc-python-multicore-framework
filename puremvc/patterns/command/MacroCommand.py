from typing import List, Callable

from puremvc.interfaces import ICommand, INotification


class MacroCommand:
    def __init__(self):
        self._subcommands: List[Callable[[], ICommand]] = []
        self.initialize_macro_command()

    def initialize_macro_command(self) -> None:
        pass

    def add_subcommand(self, factory: Callable[[], ICommand]) -> None:
        self._subcommands.append(factory)

    def execute(self, notification: INotification) -> None:
        for factory in self._subcommands[:]:
            command = factory()
            # instance.initializeNotifier(self.multitonKey)
            command.execute(notification)
