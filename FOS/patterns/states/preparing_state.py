from ...models.enums.order_state import OrderState
from .order_state import OrderState as os


class PreparingState(os):
    def next_state(self, order) -> None:
        order.state = OrderState.BAKING
        order.notify_observers("Pizza is in the oven")
