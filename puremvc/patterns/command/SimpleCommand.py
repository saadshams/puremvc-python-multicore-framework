"""
 SimpleCommand.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from puremvc.interfaces import INotification, ICommand
from puremvc.patterns.facade import Notifier


class SimpleCommand(Notifier, ICommand):
    def execute(self, notification: INotification) -> None:
        return
