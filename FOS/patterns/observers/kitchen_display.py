from typing import Optional

from ...models.enums.order_state import OrderState
from .order_observer import OrderObserver


class KitchenDisplay(OrderObserver):
    def update(self, order_id: str, message: str, state: Optional[OrderState] = None):
        print(f"Kitchen Update - Order {order_id}: {message} (State: {state})")
