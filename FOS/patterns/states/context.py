from typing import Protocol

from .base_state import OrderTrackingState


class OrderTrackingContext(Protocol):
    state: OrderTrackingState

    def set_state(self, state: OrderTrackingState):
        self.state = state

    def order_placed(self): ...

    def order_in_preparation(self): ...

    def order_out_for_delivery(self): ...
