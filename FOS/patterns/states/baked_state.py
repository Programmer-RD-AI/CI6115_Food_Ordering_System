from ...models.enums.order_enum import OrderEnum
from .order_state import OrderState


class BakingState(OrderState):
    def next_state(self, order) -> None:
        order.state = OrderEnum.READY_FOR_DELIVERY
