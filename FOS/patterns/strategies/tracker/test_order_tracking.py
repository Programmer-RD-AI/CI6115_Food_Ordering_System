import unittest

from .delivery import DeliveryTracker


class TestOrderTracking(unittest.TestCase):
    def test_delivery_tracking(self):
        store = (0.0, 0.0)
        delivery = (1.0, 1.0)
        tracker = DeliveryTracker(store, delivery)
        statuses = list(tracker.track())
        self.assertTrue(len(statuses) > 0)


if __name__ == "__main__":
    unittest.main()
