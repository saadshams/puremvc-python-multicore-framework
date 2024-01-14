import unittest

from puremvc.interfaces import INotification
from puremvc.patterns.command import SimpleCommand, MacroCommand
from puremvc.patterns.observer import Notification


class MacroCommandTest(unittest.TestCase):

    def test_macro_command_execute(self):
        vo = MacroCommandTestVO(5)
        note = Notification("MacroCommandTest", vo)
        command = MacroCommandTestCommand()
        command.execute(note)

        self.assertTrue(vo.result1 == 10)
        self.assertTrue(vo.result2 == 25)


class MacroCommandTestCommand(MacroCommand):

    def initialize_macro_command(self) -> None:
        self.add_subcommand(lambda: MacroCommandTestSub1Command())
        self.add_subcommand(lambda: MacroCommandTestSub2Command())


class MacroCommandTestSub1Command(SimpleCommand):

    def execute(self, notification: INotification) -> None:
        vo = notification.body
        vo.result1 = 2 * vo.input


class MacroCommandTestSub2Command(SimpleCommand):

    def execute(self, notification: INotification) -> None:
        vo = notification.body
        vo.result2 = vo.input * vo.input


class MacroCommandTestVO:

    def __init__(self, data: int):
        self.input = data
        self.result1 = 0
        self.result2 = 0


if __name__ == '__main__':
    unittest.main()
