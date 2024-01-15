"""
 Notification.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

from typing import Any

from puremvc.interfaces import INotification


class Notification(INotification):
    def __init__(self, name: str, body: Any = None, note_type: str = None):
        self._name = name
        self._body = body
        self._type = note_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def body(self) -> Any:
        return self._body

    @body.setter
    def body(self, body: Any) -> None:
        self._body = body

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, note_type: str) -> None:
        self._type = note_type
