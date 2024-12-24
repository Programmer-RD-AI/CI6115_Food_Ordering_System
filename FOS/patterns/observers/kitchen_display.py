from ...models.enums.order_state import OrderState
from .order_observer import OrderObserver


class KitchenDisplay(OrderObserver):
    def update_observer(self, order_id: str, state: OrderState, message: str):
        print(f"Kitchen Update - Order {order_id}: {message} (State: {state.value})")
