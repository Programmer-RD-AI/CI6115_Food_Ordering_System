from .pizza_decorator import PizzaDecorator
from ..handlers.base_handler import PizzaCustomizationHandler
from typing import Union


class PackagingDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler: Union[PizzaCustomizationHandler, PizzaDecorator],
        packaging: str = "Metal",
    ) -> None:
        builder = pizza_handler.get_builder()
        builder.set_packaging(packaging)
        super().__init__(builder)
