from ..patterns.handlers import (
    CrustsCustomizationHandler,
    SaucesCustomizationHandler,
    ToppingsCustomizationHandler,
    CheesesCustomizationHandler,
)
from ..utils.json_handler import JSON
from ..patterns.pizza_builder import PizzaBuilder
from ..models.pizza import Pizza


class PizzaService:
    def __init__(
        self,
        customization_configuration_file_name: str = "pizza_customization.json",
        handlers: list = None,
        builder: PizzaBuilder = None,
    ) -> None:
        self.customization_data = JSON(file_name=customization_configuration_file_name)
        self.builder = builder or PizzaBuilder()
        self.handlers = handlers or [
            CrustsCustomizationHandler,
            SaucesCustomizationHandler,
            ToppingsCustomizationHandler,
            CheesesCustomizationHandler,
        ]

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
        self.builder = handler_instances[0].handle_customization(
            self.user_configuration
        )
        return self.builder
