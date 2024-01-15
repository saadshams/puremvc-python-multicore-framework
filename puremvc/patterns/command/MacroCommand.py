"""
 MacroCommand.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from typing import List, Callable

from puremvc.interfaces import ICommand, INotification
from puremvc.patterns.facade import Notifier


class MacroCommand(Notifier, ICommand):
    def __init__(self):
        super().__init__()
        self._subcommands: List[Callable[[], ICommand]] = []

    def initialize_macro_command(self) -> None:
        return

    def add_subcommand(self, factory: Callable[[], ICommand]) -> None:
        self._subcommands.append(factory)

    def execute(self, notification: INotification) -> None:
        self.initialize_macro_command()
        while self._subcommands:
            factory = self._subcommands.pop(0)
            command = factory()
            command.initialize_notifier(self.multitonKey)
            command.execute(notification)
