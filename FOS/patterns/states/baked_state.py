from ...models.enums.order_state import OrderState


class BakingState(OSError):
    def next_state(self, order) -> None:
        order.state = OrderState.READY_FOR_DELIVERY
        order.notify_observers("Pizza is ready for delivery")
