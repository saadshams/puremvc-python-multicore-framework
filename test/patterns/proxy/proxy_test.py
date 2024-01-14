import unittest
from puremvc.patterns.proxy import Proxy


class ProxyTest(unittest.TestCase):

    def test_nameAccessor(self):
        proxy = Proxy("TestProxy")
        self.assertEqual(True, proxy.proxy_name == "TestProxy", "Expecting proxy.proxy_name == 'TestProxy'")

    def test_dataAccessor(self):
        proxy = Proxy("colors")
        proxy.data = ["red", "green", "blue"]
        data = proxy.data

        self.assertEqual(True, len(data) == 3, "Expecting len(data) == 3")
        self.assertEqual(True, data[0] == "red", "Expecting data[0] == 'red'")
        self.assertEqual(True, data[1] == "green", "Expecting data[1] == 'green'")
        self.assertEqual(True, data[2] == "blue", "Expecting data[2] == 'blue'")

    def test_constructor(self):
        proxy = Proxy("colors", ["red", "green", "blue"])
        data = proxy.data

        self.assertIsNotNone(proxy, "Expecting proxy not None")
        self.assertEqual(True, len(data) == 3, "Expecting len(data) == 3")
        self.assertEqual(True, data[0] == "red", "Expecting data[0] == 'red'")
        self.assertEqual(True, data[1] == "green", "Expecting data[1] == 'green'")
        self.assertEqual(True, data[2] == "blue", "Expecting data[2] == 'blue'")


if __name__ == '__main__':
    unittest.main()
