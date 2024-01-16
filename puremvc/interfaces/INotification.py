"""
 INotification.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import ABC, abstractmethod
from typing import Any


class INotification(ABC):
    """
    :class: INotification

    The interface definition for a PureMVC Notification.

    PureMVC does not rely upon underlying event models such
    as the one provided with Flash, and ActionScript 3 does
    not have an inherent event model.

    The Observer Pattern as implemented within PureMVC exists
    to support event-driven communication between the
    application and the actors of the MVC triad.

    Notifications are not meant to be a replacement for Events
    in Flex/Flash/AIR. Generally, `IMediator` implementors
    place event listeners on their view components, which they
    then handle in the usual way. This may lead to the broadcast of `Notification`s to
    trigger `ICommand`s or to communicate with other `IMediators`. `IProxy` and `ICommand`
    instances communicate with each other and `IMediator`s by broadcasting `INotification`s.

    A key difference between Flash `Event`s and PureMVC
    `Notification`s is that `Event`s follow the
    'Chain of Responsibility' pattern, 'bubbling' up the display hierarchy
    until some parent component handles the `Event`, while
    PureMVC `Notification`s follow a 'Publish/Subscribe'
    pattern. PureMVC classes need not be related to each other in a
    parent/child relationship to communicate with one another
    using `Notification`s.

    @see: `IView<puremvc.interfaces.IView>`
    @see: `IObserver<puremvc.interfaces.IObserver>`
    """
    @property
    @abstractmethod
    def name(self) -> str:
        """
        Get the name of the `INotification` instance.
        No setter, it should be set by constructor only

        :return: The name of the object.
        """
        pass

    @property
    @abstractmethod
    def body(self) -> Any:
        """
        Get the body of the `INotification` instance

        :return: The body of the method.
        :rtype: Any
        """
        pass

    @body.setter
    @abstractmethod
    def body(self, body: Any):
        """
        Set the body of the `INotification` instance

        :param body: The new body value to set for the method
        :type body: Any
        :return: None
        """
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        """
        Get the type of the `INotification` instance

        :return: The type of the object.
        :rtype: str
        """
        pass

    @type.setter
    @abstractmethod
    def type(self, _type: str):
        """
        Set the type of the `INotification` instance

        :param _type: The type of the note.
        :type _type: str
        :return: None
        """
        pass

    def __repr__(self):
        """
        Get the string representation of the `INotification` instance

        :return: The string representation of the object.
        :rtype: str
        """
        pass
