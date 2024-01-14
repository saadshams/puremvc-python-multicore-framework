from typing import Optional, Any

from puremvc.interfaces import IProxy
from puremvc.patterns.observer import Notifier


class Proxy(Notifier, IProxy):
    NAME = "Proxy"

    def __init__(self, proxy_name: Optional[str] = None, data: Any = None):
        super(Proxy, self).__init__()
        self._proxy_name = self.NAME if proxy_name is None else proxy_name
        self._data = data

    @property
    def proxy_name(self) -> str:
        return self._proxy_name

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        self._data = value

    def on_register(self) -> None:
        return

    def on_remove(self) -> None:
        return
