import unittest
from .user import User
from .loyalty import Loyalty


class TestLoyalty(unittest.TestCase):
    def setUp(self):
        self.user = User(username="test", email="test@test.com")

    def test_loyalty_points(self):
        self.user.add_loyalty_points(Loyalty(10.0))
        self.assertEqual(self.user.get_loyalty, 0.5)  # 10% points


if __name__ == "__main__":
    unittest.main()
