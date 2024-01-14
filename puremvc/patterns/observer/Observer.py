from typing import Any, Callable, Optional

from puremvc.interfaces import IObserver, INotification


class Observer(IObserver):
    def __init__(self, notify_method: Optional[Callable[[INotification], None]], notify_context: Any):
        self._notify_method = notify_method
        self._notify_context = notify_context

    @property
    def notify_method(self) -> Callable[[INotification], None]:
        return self._notify_method

    @notify_method.setter
    def notify_method(self, value: Callable[[INotification], None]) -> None:
        self._notify_method = value

    @property
    def notify_context(self) -> Any:
        return self._notify_context

    @notify_context.setter
    def notify_context(self, value: Any) -> None:
        self._notify_context = value

    def notify_observer(self, notification: INotification) -> None:
        if self._notify_method is not None:
            self._notify_method(notification)

    def compare_notify_context(self, obj: Any) -> bool:
        return obj == self._notify_context
