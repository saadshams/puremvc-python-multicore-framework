from typing import Optional, Any

from puremvc.interfaces import IMediator, INotification


class Mediator(IMediator):
    NAME = "Mediator"

    def __init__(self, mediator_name: Optional[str] = None, view_component: Any = None):
        self._mediator_name = self.NAME if mediator_name is None else mediator_name
        self._view_component = view_component

    @property
    def mediator_name(self) -> str:
        return self._mediator_name

    @property
    def view_component(self) -> Any:
        return self._view_component

    @view_component.setter
    def view_component(self, value: Any) -> None:
        self._view_component = value

    def list_notification_interests(self) -> [str]:
        return []

    def handle_notification(self, notification: INotification) -> None:
        pass

    def on_register(self) -> None:
        pass

    def on_remove(self) -> None:
        pass
