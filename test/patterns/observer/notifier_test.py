"""
 notifier_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest

from puremvc.interfaces import INotification
from puremvc.patterns.command import SimpleCommand
from puremvc.patterns.facade import Notifier


class NotifierTest(unittest.TestCase):
    def test_register_command_and_send_notification(self):
        notifier = Notifier()
        notifier.initialize_notifier("NotifierTestKey1")
        notifier.facade.register_command("NotifierTestNote", lambda: NotifierTestCommand())

        vo = NotifierTestVO(32)
        notifier.send_notification("NotifierTestNote", vo)
        self.assertTrue(vo.result == 64, "Expecting vo.result == 64")


class NotifierTestCommand(SimpleCommand):
    def execute(self, notification: INotification) -> None:
        vo = notification.body
        vo.result = 2 * vo.input


class NotifierTestVO:
    def __init__(self, data: int):
        self.input = data
        self.result = None


if __name__ == '__main__':
    unittest.main()
