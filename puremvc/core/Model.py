"""
 Model.py
 PureMVC Python Multicore

 Copyright(c) 2023 Saad Shams <saad.shams@puremvc.org>
 Your reuse is governed by the BSD License
"""

import threading
from typing import Callable, Dict

from puremvc.interfaces import IModel, IProxy


class Model(IModel):
    instanceMap: Dict[str, IModel] = dict()
    instanceMapLock: threading.Lock = threading.Lock()

    MULTITON_MSG = "Model multiton instance for this key is already constructed!"

    def __init__(self, key: str):
        if Model.instanceMap.get(key) is not None:
            raise Exception(Model.MULTITON_MSG)
        self.multitonKey: str = key
        Model.instanceMap[key] = self
        self.proxyMap: Dict[str, IProxy] = dict()
        self.proxyMapLock = threading.Lock()
        self.initialize_model()

    def initialize_model(self) -> None:
        return

    @classmethod
    def get_instance(cls, key: str, factory: Callable[[str], IModel]) -> IModel:
        with cls.instanceMapLock:
            if key not in cls.instanceMap:
                cls.instanceMap[key] = factory(key)
        return cls.instanceMap.get(key)

    def register_proxy(self, proxy: IProxy) -> None:
        proxy.initialize_notifier(self.multitonKey)
        self.proxyMap[proxy.proxy_name] = proxy
        proxy.on_register()

    def retrieve_proxy(self, proxy_name: str) -> IProxy:
        return self.proxyMap.get(proxy_name)

    def has_proxy(self, proxy_name: str) -> bool:
        return self.proxyMap.get(proxy_name) is not None

    def remove_proxy(self, proxy_name: str) -> IProxy:
        proxy = self.proxyMap.get(proxy_name)
        if proxy:
            del self.proxyMap[proxy_name]
            proxy.on_remove()
        return proxy

    @classmethod
    def remove_model(cls, key: str) -> None:
        with cls.instanceMapLock:
            del cls.instanceMap[key]
