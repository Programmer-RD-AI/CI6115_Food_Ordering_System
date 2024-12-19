from ..patterns.handlers import (
    CheesesCustomizationHandler,
    CrustsCustomizationHandler,
    SaucesCustomizationHandler,
    ToppingsCustomizationHandler,
)
from ..utils.json_handler import JSON


class PizzaService:
    def __init__(
        self,
        customization_configuration_file_name: str = "pizza_customization.json",
        handlers: list = None,
    ) -> None:
        self.customization_data = JSON(file_name=customization_configuration_file_name)
        self.handlers = handlers or [
            CrustsCustomizationHandler,
            SaucesCustomizationHandler,
            ToppingsCustomizationHandler,
            CheesesCustomizationHandler,
        ]

    def apply_handlers(self):
        prev_handler = None
        handler_instances = []
        for handler_class in self.handlers:
            handler = handler_class(
                customization=self.customization_data,
            )
            if prev_handler:
                handler.set_next(prev_handler)
            prev_handler = handler
            handler_instances.append(handler)
        return handler_instances[0].handle_customization(self.user_configuration)
