import unittest

from .pizza import Pizza
from .price import Price


class TestPizza(unittest.TestCase):
    def setUp(self):
        self.pizza = Pizza()

    def test_pizza_initialization(self):
        self.assertIsInstance(self.pizza.price, Price)
        self.assertEqual(self.pizza._Pizza__crusts, [])
        self.assertEqual(self.pizza._Pizza__sauces, [])


if __name__ == "__main__":
    unittest.main()
