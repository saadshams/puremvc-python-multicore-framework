import unittest
from typing import List

from puremvc.core import Model
from puremvc.interfaces import IModel
from puremvc.patterns.proxy import Proxy


class ModelTest(unittest.TestCase):
    def test_get_instance(self):
        model = Model.get_instance("ModelTestKey1", lambda k: Model(k))
        self.assertIsNotNone(model, "Expecting instance not None")
        self.assertIsInstance(model, IModel, "Expecting instance implements IModel")
        self.assertEqual(model, Model.get_instance("ModelTestKey1", lambda k: Model(k)))
        self.assertNotEqual(model, Model.get_instance("Key123", lambda k: Model(k)))

    def test_register_and_retrieve_proxy(self):
        model = Model.get_instance("ModelTestKey2", lambda k: Model(k))
        model.register_proxy(Proxy("colors", ["red", "green", "blue"]))
        proxy = model.retrieve_proxy("colors")
        data: List[str] = proxy.data

        self.assertIsNotNone(data, "Expecting data not None")
        self.assertTrue(isinstance(data, List), "")
        self.assertTrue(len(data) == 3, "Expecting len(data) == 3")
        self.assertTrue(data[0] == "red", "Expecting data[0] == 'red'")
        self.assertTrue(data[1] == "green", "Expecting data[1] == 'green'")
        self.assertTrue(data[2] == "blue", "Expecting data[2] == 'blue'")

    def test_register_and_remove_proxy(self):
        model = Model.get_instance("ModelTestKey3", lambda k: Model(k))
        proxy = Proxy("sizes", ["7", "13", "21"])
        model.register_proxy(proxy)

        removed_proxy = model.remove_proxy("sizes")
        self.assertTrue(removed_proxy.proxy_name == "sizes", "Expecting removed_proxy.proxy_name == 'sizes'")

        proxy = model.retrieve_proxy("colors")
        self.assertIsNone(proxy, "Expecting proxy is None")

    def test_has_proxy(self):
        model = Model.get_instance("ModelTestKey4", lambda k: Model(k))
        proxy = Proxy("aces", ["clubs", "spades", "hearts", "diamonds"])
        model.register_proxy(proxy)

        self.assertTrue(model.has_proxy("aces"), "Expecting model.has_proxy('aces') == true")
        model.remove_proxy("aces")

        self.assertFalse(model.has_proxy("aces"), "Expecting model.has_proxy('aces') == false")

    def test_on_register_and_on_Remove(self):
        model = Model.get_instance("ModelTestKey5", lambda k: Model(k))
        proxy = ModelTestProxy()
        model.register_proxy(proxy)

        self.assertTrue(proxy.data == ModelTestProxy.ON_REGISTER_CALLED,
                        "Expecting proxy.data == ModelTestProxy.ON_REGISTER_CALLED")

        model.remove_proxy(ModelTestProxy.NAME)
        self.assertTrue(proxy.data == ModelTestProxy.ON_REMOVE_CALLED,
                        "Expecting proxy.data == ModelTestProxy.ON_REMOVE_CALLED")


class ModelTestProxy(Proxy):
    NAME = "ModelTestProxy"
    ON_REGISTER_CALLED = "onRegister Called"
    ON_REMOVE_CALLED = "onRemove Called"

    def __init__(self):
        super().__init__(ModelTestProxy.NAME)

    def on_register(self) -> None:
        self.data = ModelTestProxy.ON_REGISTER_CALLED

    def on_remove(self) -> None:
        self.data = ModelTestProxy.ON_REMOVE_CALLED


if __name__ == '__main__':
    unittest.main()
