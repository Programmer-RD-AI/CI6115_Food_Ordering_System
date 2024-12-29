import unittest
from ..builder.pizza_builder import PizzaBuilder
from .extra_cheese_decorator import ExtraCheeseDecorator


class TestDecorators(unittest.TestCase):
    def test_extra_cheese(self):
        builder = PizzaBuilder()
        builder.set_cheeses(["Mozzarella"])
        decorated = ExtraCheeseDecorator(builder).apply()
        pizza = decorated.build()
        self.assertEqual(len(pizza._Pizza__cheeses), 3)


if __name__ == "__main__":
    unittest.main()
