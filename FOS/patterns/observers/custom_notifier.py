from typing import Optional

from ...models.enums.order_state import OrderState
from .order_observer import OrderObserver


class CustomerNotifier(OrderObserver):
    def update(self, order_id: str, message: str, state: Optional[OrderState] = None):
        print(f"Customer Notification - Order {order_id}: {message} (State: {state})")
