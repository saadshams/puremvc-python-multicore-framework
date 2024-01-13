import unittest

from puremvc.interfaces import INotification
from puremvc.patterns.command import SimpleCommand
from puremvc.patterns.observer import Notification


class TestSimpleCommand(unittest.TestCase):

    def test_simple_command_execute(self):
        vo = SimpleCommandTestVO(5)
        note = Notification("SimpleCommandTestNote", vo)
        command = SimpleCommandTestCommand()
        command.execute(note)

        self.assertTrue(vo.result == 10, "Expecting vo.result == 10")


class SimpleCommandTestVO:

    def __init__(self, input: int):
        self.input = input
        self.result = 0


class SimpleCommandTestCommand(SimpleCommand):

    def execute(self, notification: INotification):
        vo = notification.body

        # Fabricate a result
        vo.result = 2 * vo.input


if __name__ == '__main__':
    unittest.main()
