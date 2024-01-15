"""
 ICommand.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import abstractmethod

from .INotifier import INotifier
from .INotification import INotification


class ICommand(INotifier):

    @abstractmethod
    def execute(self, notification: INotification) -> None:
        pass
