import unittest
from .pizza_builder import PizzaBuilder


class TestPizzaCustomization(unittest.TestCase):
    def setUp(self):
        self.builder = PizzaBuilder()

    def test_pizza_creation(self):
        pizza = (
            self.builder.set_crusts(["Thin"])
            .set_sauces(["Tomato"])
            .set_toppings(["Pepperoni"])
            .set_cheeses(["Mozzarella"])
            .build()
        )
        self.assertEqual(pizza._Pizza__crusts, ["Thin"])
        self.assertEqual(pizza._Pizza__sauces, ["Tomato"])


if __name__ == "__main__":
    unittest.main()
