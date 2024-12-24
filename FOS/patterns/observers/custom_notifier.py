from .order_observer import OrderObserver
from ...models.enums.order_state import OrderState


class CustomerNotifier(OrderObserver):
    def update_observer(self, order_id: str, state: OrderState, message: str):
        print(
            f"Customer Notification - Order {order_id}: {message} (State: {state.value})"
        )