from typing import Dict

from puremvc.interfaces import IController


class Controller:
    instanceMap: Dict[str, IController] = dict()
