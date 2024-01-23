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
    """
    :class: ICommand

    The interface definition for a PureMVC Command

    @see: `INotification<puremvc.interfaces.INotification>`
    """
    @abstractmethod
    def execute(self, notification: INotification):
        """
        Execute the `ICommand`'s logic to handle a given `INotification`.

        :param notification: An `INotification` to handle.
        :type notification: INotification
        :return: None
        """
        pass
