from abc import ABC, abstractmethod
from typing import Optional

from ...models.enums.order_enum import OrderEnum


class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: str, message: str, state: Optional[OrderEnum] = None):
        pass
