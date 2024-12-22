from abc import ABC, abstractmethod
from typing import Any


class OrderObserver(ABC):
    @abstractmethod
    def update_observer(self, data: Any) -> None: ...
