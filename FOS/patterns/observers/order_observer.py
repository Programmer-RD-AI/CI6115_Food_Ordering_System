from abc import ABC, abstractmethod
from typing import Optional

from ...models.enums.order_state import OrderState


class OrderObserver(ABC):
    @abstractmethod
    def update(
        self, order_id: str, message: str, state: Optional[OrderState] = None
    ) -> None: ...
