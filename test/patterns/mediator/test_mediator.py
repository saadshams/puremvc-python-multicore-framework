import unittest
from puremvc.patterns.mediator import Mediator


class TestMediator(unittest.TestCase):

    def test_nameAccessor(self):
        mediator = Mediator()
        self.assertEqual(True, mediator.mediator_name == "Mediator", "Expecting mediator.mediator_name == Mediator.NAME")

    def test_viewAccessor(self):
        view = object()
        mediator = Mediator(Mediator.NAME, view)
        self.assertIsNotNone(mediator.view_component, "Expecting mediator.view_component not null")


if __name__ == '__main__':
    unittest.main()
