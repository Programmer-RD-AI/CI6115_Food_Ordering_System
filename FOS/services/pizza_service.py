from ..patterns.handlers import (
    CrustsCustomizationHandler,
    SaucesCustomizationHandler,
    ToppingsCustomizationHandler,
    CheesesCustomizationHandler,
)
from ..utils.json_handler import JSON
from ..patterns.builder.pizza_builder import PizzaBuilder
from ..models.pizza import Pizza
from typing import Optional


class PizzaService:
    def __init__(
        self,
        customization_configuration_file_name: str = "pizza_customization.json",
        handlers: list = None,
        builder: Optional[PizzaBuilder] = None,
        user_configuration: dict = {},
    ) -> None:
        self.customization_data = JSON(file_name=customization_configuration_file_name)
        self.builder = builder if builder is not None else PizzaBuilder()
        self.handlers = handlers or [
            CrustsCustomizationHandler,
            SaucesCustomizationHandler,
            ToppingsCustomizationHandler,
            CheesesCustomizationHandler,
        ]
        self.user_configuration = user_configuration

    def apply_handlers(self) -> Pizza:
        prev_handler = None
        handler_instances = []
        for handler_class in self.handlers:
            handler = handler_class(
                customization=self.customization_data, builder=self.builder
            )
            if prev_handler:
                handler.set_next(prev_handler)
            prev_handler = handler
            handler_instances.append(handler)
        self.builder = handler_instances[-1].handle_customization(
            self.user_configuration
        )
        return self.builder
