import unittest
from .order_state import OrderState
from .placed_state import PlacedState
from ..observers.custom_notifier import CustomerNotifier


class TestOrderStates(unittest.TestCase):
    def test_state_transition(self):
        notifier = CustomerNotifier()
        state = PlacedState()
        self.assertIsInstance(state, OrderState)
        self.assertIsInstance(notifier, CustomerNotifier)


if __name__ == "__main__":
    unittest.main()
