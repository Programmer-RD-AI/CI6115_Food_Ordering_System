from .pizza_decorator import PizzaDecorator
from ..handlers.base_handler import PizzaCustomizationHandler
from typing import Union


class GetPizzaForFreeDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler: Union[PizzaCustomizationHandler, PizzaDecorator],
        factor_of_free: int = 1,
    ) -> None:
        self.factor_of_free = factor_of_free
        builder = pizza_handler.get_builder()
        super().__init__(builder)

    def apply(self):
        self.__builder .set_(self.packaging)
        return self.get_builder()
