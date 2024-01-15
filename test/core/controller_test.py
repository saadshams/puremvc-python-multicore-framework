"""
 controller_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest

from puremvc.core import Controller, View
from puremvc.interfaces import IController, INotification, IView
from puremvc.patterns.command import SimpleCommand
from puremvc.patterns.observer import Notification


class ControllerTest(unittest.TestCase):
    def test_get_instance(self):
        controller: IController = Controller.get_instance("ControllerTestKey1", lambda k: Controller(k))
        self.assertIsNotNone(controller, "Expecting instance not null")
        self.assertIsInstance(controller, IController, "Expecting instance implements IController")

    def test_register_and_execute_command(self):
        controller: IController = Controller.get_instance("ControllerTestKey2", lambda k: Controller(k))
        controller.register_command("ControllerTest", lambda: ControllerTestCommand())
        vo = ControllerTestVO(12)
        note = Notification("ControllerTest", vo)

        controller.execute_command(note)
        self.assertTrue(vo.result == 24, "Expecting vo.result == 24")

    def test_register_and_remove_command(self):
        controller: IController = Controller.get_instance("ControllerTestKey3", lambda k: Controller(k))
        controller.register_command("ControllerRemoveTest", lambda: ControllerTestCommand())

        vo = ControllerTestVO(12)
        note = Notification("ControllerRemoveTest", vo)

        controller.execute_command(note)

        self.assertTrue(vo.result == 24, "Expecting vo.result == 24")

        vo.result = 0

        controller.remove_command("ControllerRemoveTest")

        controller.execute_command(note)

        self.assertTrue(vo.result == 0, "Expecting vo.result == 0")

    def test_has_command(self):
        controller: IController = Controller.get_instance("ControllerTestKey4", lambda k: Controller(k))
        controller.register_command("hasCommandTest", lambda: ControllerTestCommand())

        self.assertTrue(controller.has_command("hasCommandTest"),
                        "Expecting controller.has_command('hasCommandTest') == true")

        controller.remove_command("hasCommandTest")
        self.assertFalse(controller.has_command("hasCommandTest"),
                         "Expecting controller.has_command('hasCommandTest') == false")

    def test_re_register_and_execute_command(self):
        controller: IController = Controller.get_instance("ControllerTestKey5", lambda k: Controller(k))
        controller.register_command("ControllerTestKey2", lambda: ControllerTestCommand2())

        controller.remove_command("ControllerTest2")

        controller.register_command("ControllerTest2", lambda: ControllerTestCommand2())

        vo = ControllerTestVO(12)
        note = Notification("ControllerTest2", vo)

        view: IView = View.get_instance("ControllerTestKey5", lambda k: View(k))
        view.notify_observers(note)

        self.assertTrue(vo.result == 24, "Expecting vo.result == 24")
        view.notify_observers(note)

        self.assertTrue(vo.result == 48, "Expecting vo.result == 48")


class ControllerTestCommand(SimpleCommand):
    def execute(self, notification: INotification) -> None:
        vo: ControllerTestVO = notification.body
        vo.result = 2 * vo.input


class ControllerTestCommand2(SimpleCommand):
    def execute(self, notification: INotification) -> None:
        vo: ControllerTestVO = notification.body
        vo.result = vo.result + (2 * vo.input)


class ControllerTestVO:
    def __init__(self, input: int):
        self.input = input
        self.result = 0


if __name__ == '__main__':
    unittest.main()
