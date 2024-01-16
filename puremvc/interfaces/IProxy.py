"""
 IProxy.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from abc import abstractmethod
from typing import Any

from .INotifier import INotifier


class IProxy(INotifier):
    """
    Get the Proxy name

    :return: The name of the proxy as a string.
    :rtype: str
    """
    @property
    @abstractmethod
    def proxy_name(self) -> str:
        """
        Get the Proxy name

        :return: The name of the proxy as a string.
        :rtype: str
        """
        pass

    @property
    @abstractmethod
    def data(self) -> Any:
        """
        Get the data object

        :return: The data of the method.
        :rtype: Any
        """
        pass

    @data.setter
    def data(self, value: Any):
        """
        Get the data object

        :param value: The value to be set for the `data` attribute.
        :type value: Any
        :return: None
        """
        pass

    @abstractmethod
    def on_register(self):
        """
        Called by the Model when the Proxy is registered.
        """
        pass

    @abstractmethod
    def on_remove(self):
        """
        Called by the Model when the Proxy is removed.
        """
        pass
