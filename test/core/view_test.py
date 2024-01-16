"""
 view_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest

from puremvc.core import View
from puremvc.interfaces import IView, INotification, IMediator, IObserver
from puremvc.patterns.mediator import Mediator
from puremvc.patterns.observer import Observer, Notification


class ViewTest(unittest.TestCase):
    NOTE1 = "note1"
    NOTE2 = "note2"
    NOTE3 = "note3"
    NOTE4 = "note4"
    NOTE5 = "note5"
    NOTE6 = "note6"

    def __init__(self, method_name: str = "runTest"):
        super().__init__(method_name)
        self.lastNotification = ""
        self.onRegisterCalled = False
        self.onRemoveCalled = False
        self.counter = 0

    def test_get_Instance(self):
        view: IView = View.get_instance("ViewTestKey1", lambda k: View(k))
        self.assertIsNotNone(view, "Expecting instance not None")
        self.assertIsInstance(view, IView, "Expecting instance implements IView")
        self.assertEqual(view, View.get_instance("ViewTestKey1", lambda k: View(k)))
        self.assertNotEqual(view, View.get_instance("Key123", lambda k: View(k)))

    def test_register_and_notify_observer(self):
        view: IView = View.get_instance("ViewTestKey2", lambda k: View(k))
        observer: IObserver = Observer(self.view_test_method, self)
        view.register_observer("ViewTestNote", observer)
        note: INotification = Notification("ViewTestNote", 10)
        view.notify_observers(note)

        self.assertTrue(self.viewTestVar == 10, "Expecting viewTestVar = 10")

    def view_test_method(self, note: INotification):
        self.viewTestVar = note.body

    def test_register_and_retrieve_mediator(self):
        view: IView = View.get_instance("ViewTestKey3", lambda k: View(k))
        view_test_mediator: IMediator = ViewTestMediator(self)
        view.register_mediator(view_test_mediator)

        mediator: IMediator = view.retrieve_mediator(ViewTestMediator.NAME)
        self.assertIsInstance(mediator, ViewTestMediator, "Expecting mediator is ViewTestMediator")

    def test_has_mediator(self):
        view: IView = View.get_instance("ViewTestKey4", lambda k: View(k))
        mediator: IMediator = Mediator("hasMediatorTest", self)
        view.register_mediator(mediator)

        self.assertTrue(view.has_mediator("hasMediatorTest"),
                        "Expecting view.has_mediator('hasMediatorTest') == true")

        view.remove_mediator("hasMediatorTest")
        self.assertFalse(view.has_mediator("hasMediatorTest"),
                         "Expecting view.has_mediator('has_mediator_test') == false")

    def test_register_and_remove_mediator(self):
        view: IView = View.get_instance("ViewTestKey5", lambda k: View(k))
        mediator: IMediator = Mediator("testing", self)
        view.register_mediator(mediator)

        removed_mediator: IMediator = view.remove_mediator("testing")
        self.assertTrue(removed_mediator.mediator_name == "testing",
                        "Expecting removedMediator.mediator_name == 'testing'")

        self.assertIsNone(view.retrieve_mediator("testing"),
                          "Expecting view.retrieveMediator('testing') == null )")

    def test_on_register_and_on_remove(self):
        view: IView = View.get_instance("ViewTestKey6", lambda k: View(k))
        mediator: IMediator = ViewTestMediator4(self)
        view.register_mediator(mediator)

        self.assertTrue(self.onRegisterCalled, "Expecting onRegisterCalled == true")

        view.remove_mediator(ViewTestMediator4.NAME)

        self.assertTrue(self.onRemoveCalled, "Expecting onRemoveCalled == true")

    def test_successive_register_and_remove_mediator(self):
        view: IView = View.get_instance("ViewTestKey7", lambda k: View(k))
        view.register_mediator(ViewTestMediator(self))
        self.assertIsInstance(view.retrieve_mediator(ViewTestMediator.NAME), ViewTestMediator,
                              "Expecting view.retrieveMediator(ViewTestMediator.NAME) is ViewTestMediator")
        view.remove_mediator(ViewTestMediator.NAME)

        self.assertIsNone(view.retrieve_mediator(ViewTestMediator.NAME),
                          "Expecting view.retrieve_mediator(ViewTestMediator.NAME) == None")

        view.register_mediator(ViewTestMediator(self))
        self.assertIsInstance(view.retrieve_mediator(ViewTestMediator.NAME), ViewTestMediator,
                              "Expecting view.retrieve_mediator(ViewTestMediator.NAME) is ViewTestMediator")

        view.remove_mediator(ViewTestMediator.NAME)
        self.assertIsNone(view.retrieve_mediator(ViewTestMediator.NAME),
                          "Expecting view.retrieve_mediator(ViewTestMediator.NAME) == null")

    def test_remove_mediator_and_subsequent_notify(self):
        view: IView = View.get_instance("ViewTestKey8", lambda k: View(k))
        view.register_mediator(ViewTestMediator2(self))

        view.notify_observers(Notification(ViewTest.NOTE1))
        self.assertTrue(self.lastNotification == ViewTest.NOTE1, "Expecting lastNotification == NOTE1")

        view.notify_observers(Notification(ViewTest.NOTE2))
        self.assertTrue(self.lastNotification == ViewTest.NOTE2, "Expecting lastNotification == NOTE2")

        view.remove_mediator(ViewTestMediator2.NAME)

        self.assertIsNone(view.retrieve_mediator(ViewTestMediator2.NAME),
                          "Expecting view.retrieve_mediator(ViewTestMediator2.NAME) == null")

        self.lastNotification = None

        view.notify_observers(Notification(ViewTest.NOTE1))
        self.assertTrue(self.lastNotification != ViewTest.NOTE1, "Expecting lastNotification != NOTE1")

        view.notify_observers(Notification(ViewTest.NOTE2))
        self.assertTrue(self.lastNotification != ViewTest.NOTE2, "Expecting lastNotification != NOTE2")

    def test_remove_one_of_two_mediators_and_subsequent_notify(self):
        view: IView = View.get_instance("ViewTestKey9", lambda k: View(k))
        view.register_mediator(ViewTestMediator2(self))
        view.register_mediator(ViewTestMediator3(self))

        view.notify_observers(Notification(ViewTest.NOTE1))
        self.assertTrue(self.lastNotification == ViewTest.NOTE1, "Expecting lastNotification == NOTE1")

        view.notify_observers(Notification(ViewTest.NOTE2))
        self.assertTrue(self.lastNotification == ViewTest.NOTE2, "Expecting lastNotification == NOTE2")

        view.notify_observers(Notification(ViewTest.NOTE3))
        self.assertTrue(self.lastNotification == ViewTest.NOTE3, "Expecting lastNotification == NOTE3")

        view.remove_mediator(ViewTestMediator2.NAME)

        self.assertIsNone(view.retrieve_mediator(ViewTestMediator2.NAME),
                          "Expecting view.retrieve_mediator(ViewTestMediator2.NAME) == None")

        self.lastNotification = None

        view.notify_observers(Notification(ViewTest.NOTE1))
        self.assertTrue(self.lastNotification != ViewTest.NOTE1)

        view.notify_observers(Notification(ViewTest.NOTE2))
        self.assertTrue(self.lastNotification != ViewTest.NOTE2)

        view.notify_observers(Notification(ViewTest.NOTE3))
        self.assertTrue(self.lastNotification == ViewTest.NOTE3)

    def test_mediator_reregistration(self):
        view: IView = View.get_instance("ViewTestKey10", lambda k: View(k))
        view.register_mediator(ViewTestMediator5(self))

        view.register_mediator(ViewTestMediator5(self))

        self.counter = 0
        view.notify_observers(Notification(ViewTest.NOTE5))
        self.assertEqual(self.counter, 1, "Expecting counter == 1")

        view.remove_mediator(ViewTestMediator5.NAME)
        self.assertIsNone(view.retrieve_mediator(ViewTestMediator5.NAME),
                          "Expecting view.retrieve_mediator(ViewTestMediator5.NAME) == null")

        self.counter = 0
        view.notify_observers(Notification(ViewTest.NOTE5))
        self.assertEqual(self.counter, 0, "Expecting counter == 0")

    def test_modify_observer_list_during_notification(self):
        view: IView = View.get_instance("ViewTestKey11", lambda k: View(k))

        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/1", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/2", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/3", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/4", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/5", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/6", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/7", self))
        view.register_mediator(ViewTestMediator6(ViewTestMediator6.NAME + "/8", self))

        # self.counter = 0
        # view.notify_observers(Notification(ViewTest.NOTE6))
        # self.assertEqual(self.counter, 8, "Expecting counter == 8")

        self.counter = 0
        view.notify_observers(Notification(ViewTest.NOTE6))
        self.assertEqual(self.counter, 0, "Expecting counter == 0")


class ViewTestMediator(Mediator):
    NAME = "ViewTestMediator"

    def __init__(self, view: object):
        super().__init__(ViewTestMediator.NAME, view)

    def list_notification_interests(self) -> [str]:
        return ["ABC", "DEF", "GHI"]


class ViewTestMediator2(Mediator):
    NAME = "ViewTestMediator2"

    def __init__(self, view: object):
        super().__init__(ViewTestMediator2.NAME, view)

    def list_notification_interests(self) -> [str]:
        return [ViewTest.NOTE1, ViewTest.NOTE2]

    def handle_notification(self, notification: INotification):
        self.view_component.lastNotification = notification.name


class ViewTestMediator3(Mediator):
    NAME = "ViewTestMediator3"

    def __init__(self, view: object):
        super().__init__(ViewTestMediator3.NAME, view)

    def list_notification_interests(self) -> [str]:
        return [ViewTest.NOTE3]

    def handle_notification(self, notification: INotification):
        self.view_component.lastNotification = notification.name


class ViewTestMediator4(Mediator):
    NAME = "ViewTestMediator4"

    def __init__(self, view: object):
        super().__init__(ViewTestMediator4.NAME, view)

    def on_register(self):
        self.view_component.onRegisterCalled = True

    def on_remove(self):
        self.view_component.onRemoveCalled = True


class ViewTestMediator5(Mediator):
    NAME = "ViewTestMediator5"

    def __init__(self, view: object):
        super().__init__(ViewTestMediator5.NAME, view)

    def list_notification_interests(self) -> [str]:
        return [ViewTest.NOTE5]

    def handle_notification(self, notification: INotification):
        self.view_component.counter += 1


class ViewTestMediator6(Mediator):
    NAME = "ViewTestMediator6"

    def __init(self, name: str, view: object):
        super().__init__(name, view)

    def list_notification_interests(self) -> [str]:
        return [ViewTest.NOTE6]

    def handle_notification(self, notification: INotification):
        pass
        # facade.removeMediator(self.mediator_name)

    def on_remove(self):
        self.view_component.counter += 1


if __name__ == '__main__':
    unittest.main()
