from typing import Optional

from ...models.enums.order_enum import OrderEnum
from .order_observer import OrderObserver


class CustomerNotifier(OrderObserver):
    def update(self, order_id: str, message: str, state: Optional[OrderEnum] = None):
        print(f"Customer Notification - Order {order_id}: {message} (State: {state})")
