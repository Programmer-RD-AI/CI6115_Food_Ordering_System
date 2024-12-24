import order_state

from ...models.enums.order_state import OrderState


class PreparingState(order_state.OrderState):
    def next_state(self, order) -> None:
        order.state = OrderState.BAKING
        order.notify_observers("Pizza is in the oven")
