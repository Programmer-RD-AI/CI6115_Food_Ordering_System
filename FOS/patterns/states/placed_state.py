from ...models.enums.order_state import OrderState
import order_state


class PlacedState(order_state.OrderState):
    def next_state(self, order) -> None:
        order.state = OrderState.PREPARING
        order.notify_observers("Order is being prepared")
