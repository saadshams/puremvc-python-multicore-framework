"""
 facade_test.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import unittest
from typing import List

from puremvc.interfaces import IFacade, INotification, IProxy
from puremvc.patterns.command import SimpleCommand
from puremvc.patterns.facade import Facade
from puremvc.patterns.mediator import Mediator
from puremvc.patterns.proxy import Proxy


class FacadeTest(unittest.TestCase):
    def test_get_instance(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey1", lambda k: Facade(k))
        self.assertIsNotNone(facade, "Expecting instance not null")
        self.assertIsInstance(facade, IFacade, "Expecting instance implements IFacade")

    def test_register_command_and_send_notification(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey2", lambda k: Facade(k))
        facade.register_command("FacadeTestNote", lambda: FacadeTestCommand())
        vo = FacadeTestVO(32)
        facade.send_notification("FacadeTestNote", vo)

        self.assertTrue(vo.result == 64, "Expecting vo.result == 64")

    def test_register_and_remove_command_and_send_notification(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey3", lambda k: Facade(k))
        facade.register_command("FacadeTestNote", lambda: FacadeTestCommand())
        facade.remove_command("FacadeTestNote")

        vo = FacadeTestVO(32)
        facade.send_notification("FacadeTestNote", vo)

        self.assertTrue(vo.result != 64, "Expecting vo.result != 64")

    def test_register_and_retrieve_proxy(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey4", lambda k: Facade(k))
        facade.register_proxy(Proxy("colors", ["red", "green", "blue"]))
        proxy = facade.retrieve_proxy("colors")

        self.assertIsInstance(proxy, IProxy, "Expecting proxy is IProxy")
        data: [str] = proxy.data

        self.assertIsNotNone(data, "Expecting data not null")
        self.assertIsInstance(data, List, "Expecting data is List")
        self.assertTrue(len(data) == 3, "Expecting len(data) == 3")
        self.assertTrue(data[0] == "red", "Expecting data[0] == 'red'")
        self.assertTrue(data[1] == "green", "Expecting data[1] == 'green'")
        self.assertTrue(data[2] == "blue", "Expecting data[2] == 'blue'")

    def test_register_and_remove_proxy(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey5", lambda k: Facade(k))
        proxy = Proxy("sizes", ["7", "13", "21"])
        facade.register_proxy(proxy)

        removed_proxy = facade.remove_proxy("sizes")

        self.assertTrue(removed_proxy.proxy_name == "sizes",
                        "Expecting removed_proxy.proxy_name() == 'sizes'")

        proxy = facade.retrieve_proxy("sizes")
        self.assertIsNone(proxy, "Expecting proxy is None")

    def test_register_retrieve_and_remove_mediator(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey6", lambda k: Facade(k))
        facade.register_mediator(Mediator(Mediator.NAME, object()))

        self.assertIsNotNone(facade.retrieve_mediator(Mediator.NAME), "Expecting mediator is not None")

        removed_mediator = facade.remove_mediator(Mediator.NAME)

        self.assertTrue(removed_mediator.mediator_name == Mediator.NAME,
                        "Expecting removed_mediator.mediator_name == Mediator.NAME")

        self.assertIsNone(facade.retrieve_mediator(Mediator.NAME),
                          "Expecting facade.retrieve_mediator(Mediator.NAME) == null")

    def test_has_proxy(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey7", lambda k: Facade(k))
        facade.register_proxy(Proxy("hasProxyTest", [1, 2, 3]))

        self.assertTrue(facade.has_proxy("hasProxyTest"), "Expecting facade.has_proxy('hasProxyTest') == true")

    def test_has_mediator(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey8", lambda k: Facade(k))
        facade.register_mediator(Mediator("facadeHasMediatorTest", object()))
        self.assertTrue(facade.has_mediator("facadeHasMediatorTest"),
                        "Expecting facade.has_mediator('facadeHasMediatorTest') == true")

        facade.remove_mediator("facadeHasMediatorTest")
        self.assertFalse(facade.has_mediator("facadeHasMediatorTest"),
                         "Expecting facade.has_mediator('facadeHasMediatorTest') == false")

    def test_has_command(self):
        facade: IFacade = Facade.get_instance("FacadeTestKey10", lambda k: Facade(k))
        facade.register_command("facadeHasCommandTest", lambda: FacadeTestCommand())

        self.assertTrue(facade.has_command("facadeHasCommandTest"),
                        "Expecting facade.has_command('facadeHasCommandTest') == true")

        facade.remove_command("facadeHasCommandTest")
        self.assertFalse(facade.has_command("facadeHasCommandTest"),
                         "Expecting facade.has_command('facadeHasCommandTest') == false")

    def test_has_core_and_remove_core(self):
        self.assertFalse(Facade.has_core("FacadeTestKey11"),
                         "Expecting facade.has_core('FacadeTestKey11') == false")

        Facade.get_instance("FacadeTestKey11", lambda k: Facade(k))

        self.assertTrue(Facade.has_core("FacadeTestKey11"),
                        "Expecting facade.hasCore('FacadeTestKey11') == true")

        Facade.remove_core("FacadeTestKey11")

        self.assertFalse(Facade.has_core("FacadeTestKey11"),
                         "Expecting facade.has_core('FacadeTestKey11') == false")


class FacadeTestCommand(SimpleCommand):
    def execute(self, notification: INotification):
        vo: FacadeTestVO = notification.body
        vo.result = 2 * vo.input


class FacadeTestVO:
    def __init__(self, data: int):
        self.input = data
        self.result = 0


if __name__ == '__main__':
    unittest.main()
