from typing import Union

from ..handlers.base_handler import PizzaCustomizationHandler
from .pizza_decorator import PizzaDecorator


class PackagingDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler: Union[PizzaCustomizationHandler, PizzaDecorator],
        packaging: str = "Metal",
    ) -> None:
        builder = pizza_handler.get_builder()
        builder.set_packaging(packaging)
        super().__init__(builder)
