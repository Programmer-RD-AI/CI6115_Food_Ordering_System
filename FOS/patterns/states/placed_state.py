from ...models.enums.order_state import OrderState
from .order_state import OrderState as os


class PlacedState(os):
    def next_state(self, order) -> None:
        order.state = OrderState.PREPARING
        order.notify_observers("Order is being prepared")
