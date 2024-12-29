from .pizza_decorator import PizzaDecorator
from ..builder.pizza_builder import PizzaBuilder


class ExtraCheeseDecorator(PizzaDecorator):
    def __init__(
        self, pizza_handler: PizzaBuilder, factor_of_extra_cheese: int = 2
    ) -> None:
        super().__init__(pizza_handler)
        self.factor_of_extra_cheese = factor_of_extra_cheese

    def apply(self):
        current_cheeses = self.get_cheeses()
        new_cheeses = []
        for _ in range(self.factor_of_extra_cheese):
            new_cheeses.extend(current_cheeses)
        self.set_cheeses(new_cheeses)
        return self.get_builder()
