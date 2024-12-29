import unittest

from .custom_notifier import CustomerNotifier
from .kitchen_display import KitchenDisplay


class TestObservers(unittest.TestCase):
    def test_observer_creation(self):
        notifier = CustomerNotifier()
        display = KitchenDisplay()
        self.assertIsInstance(notifier, CustomerNotifier)
        self.assertIsInstance(display, KitchenDisplay)


if __name__ == "__main__":
    unittest.main()
