from abc import ABC, abstractmethod
from ...models.enums.order_enum import OrderEnum
from typing import Optional


class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id: str, message: str, state: Optional[OrderEnum] = None):
        pass
