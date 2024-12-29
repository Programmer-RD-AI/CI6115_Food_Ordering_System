from ...models.enums.order_enum import OrderEnum
from .order_state import OrderState


class PreparingState(OrderState):
    def next_state(self, order) -> None:
        order.state = OrderEnum.BAKING
