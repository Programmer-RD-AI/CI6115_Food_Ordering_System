from typing import Union

from ..builder.pizza_builder import PizzaBuilder
from ..handlers.base_handler import PizzaCustomizationHandler
from .pizza_decorator import PizzaDecorator


class GetPizzaForFreeDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler: Union[PizzaBuilder, PizzaCustomizationHandler, PizzaDecorator],
        factor_of_free: int = 1,
    ) -> None:
        # Handle both PizzaBuilder and decorated objects
        if isinstance(pizza_handler, PizzaBuilder):
            builder = pizza_handler
        else:
            builder = pizza_handler.get_builder()

        super().__init__(builder)
        self.factor_of_free = factor_of_free

    def apply(self):
        # Set pizza as free
        self._builder.pizza.price.amount = 0
        self._builder.set_packaging("🎉 FREE PIZZA - Thank you for your loyalty! 🎉")
        return self._builder
