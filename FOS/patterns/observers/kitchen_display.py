from .order_observer import OrderObserver
from ...models.enums.order_state import OrderState
from typing import Optional


class KitchenDisplay(OrderObserver):
    def update(self, order_id: str, message: str, state: Optional[OrderState] = None):
        print(f"Kitchen Update - Order {order_id}: {message} (State: {state})")
