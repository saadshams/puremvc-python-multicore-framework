"""
 notification_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest
from puremvc.patterns.observer import Notification


class NotificationTest(unittest.TestCase):

    def test_nameAccessor(self):
        note = Notification("TestNote")
        self.assertTrue(note.name == "TestNote", "Expecting note.name == 'TestNote'")

    def test_testBodyAccessors(self):
        note = Notification("TestNote")
        note.body = 5
        self.assertTrue(note.body == 5, "Expecting note.body == 5")

    def test_constructor(self):
        note = Notification("TestNote", 5, "TestNoteType")

        self.assertTrue(note.name == "TestNote", "Expecting note.name == 'TestNote'")
        self.assertTrue(note.body == 5, "Expecting note.body == 5")
        self.assertTrue(note.type == "TestNoteType", "Expecting note.type == 'TestNoteType'")


if __name__ == '__main__':
    unittest.main()
