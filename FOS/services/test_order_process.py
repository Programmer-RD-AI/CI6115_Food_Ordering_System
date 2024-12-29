import unittest
from ..models.user import User
from .order_service import Order


class TestOrderProcess(unittest.TestCase):
    def setUp(self):
        self.user = User(username="test", email="test@test.com")
        self.order = Order(self.user)

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)


if __name__ == "__main__":
    unittest.main()
