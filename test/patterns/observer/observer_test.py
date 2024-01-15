"""
 observer_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest
from puremvc.interfaces import INotification
from puremvc.patterns.observer import Observer
from puremvc.patterns.observer import Notification


class ObserverTest(unittest.TestCase):

    def test_observerAccessors(self):
        observer = Observer(None, None)
        self.observer_test_var = 0

        observer.notify_context = self
        observer.notify_method = self.observer_test_method

        note = Notification("ObserverTestNote", 10)
        observer.notify_observer(note)
        self.assertTrue(self.observer_test_var == 10, "Expecting observer_test_var = 10")

    def test_observerConstructor(self):
        observer = Observer(self.observer_test_method, self)
        note = Notification("ObserverTestNote", 5)
        observer.notify_observer(note)
        self.assertTrue(self.observer_test_var == 5, "Expecting observerTestVar = 5")

    def test_compareNotifyContext(self):
        observer = Observer(self.observer_test_method, self)
        neg = object()
        self.assertFalse(observer.compare_notify_context(neg), "observer.compare_notify_context(neg) == False")
        self.assertTrue(observer.compare_notify_context(self), "observer.compare_notify_context(self) == True")

    def observer_test_method(self, notification: INotification):
        self.observer_test_var = notification.body


if __name__ == "__main__":
    unittest.main()
