from .order_observer import OrderObserver
from ...models.enums.order_state import OrderState
from typing import Optional


class CustomerNotifier(OrderObserver):
    def update(self, order_id: str, message: str, state: Optional[OrderState] = None):
        print(f"Customer Notification - Order {order_id}: {message} (State: {state})")
