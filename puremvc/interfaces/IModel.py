from abc import ABC, abstractmethod

from puremvc.interfaces import IProxy


class IModel(ABC):

    @abstractmethod
    def register_proxy(self, proxy: IProxy) -> None:
        pass

    @abstractmethod
    def retrieve_proxy(self, proxy_name: str) -> IProxy:
        pass

    @abstractmethod
    def remove_proxy(self, proxy_name: str) -> IProxy:
        pass

    @abstractmethod
    def has_proxy(self, proxy_name: str) -> bool:
        pass
