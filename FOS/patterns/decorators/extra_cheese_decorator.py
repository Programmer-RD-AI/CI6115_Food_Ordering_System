from typing import Union

from ..handlers.base_handler import PizzaCustomizationHandler
from .pizza_decorator import PizzaDecorator


class ExtraCheeseDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler: Union[PizzaCustomizationHandler, PizzaDecorator],
        factor_of_extra_cheese: int = 2,
    ) -> None:
        builder = pizza_handler.get_builder()
        new_cheeses = []
        new_cheeses.extend([builder.get_cheeses()] * factor_of_extra_cheese)
        builder.set_cheeses(new_cheeses)
        super().__init__(builder)
