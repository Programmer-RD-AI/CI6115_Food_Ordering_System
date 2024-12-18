from ..utils.json_handler import JSON
from ..models.pizza import Pizza
from ..handlers import (
    PizzaCustomizationHandler,
    CheesesCustomizationHandler,
    CrustsCustomizationHandler,
    SaucesCustomizationHandler,
    ToppingsCustomizationHandler,
)
from typing import Dict


class PizzaCustomizationService(object):
    def __init__(
        self,
        customization_configuration_file_name: str = "pizza_customization.json",
        user_configuration: dict[str : str | list] = None,
        pizza_instance: Pizza = None,
    ):
        self.customization_data = JSON(file_name=customization_configuration_file_name)
        self.user_configuration = self.get_standard_user_configuration_structure(
            user_configuration
        )
        self.pizza_instance: Pizza = Pizza() if not pizza_instance else pizza_instance
        self.__handlers_order = [
            CrustsCustomizationHandler,
            SaucesCustomizationHandler,
            ToppingsCustomizationHandler,
            CheesesCustomizationHandler,
        ]

    @property
    def __getHandleOrders(self) -> list[PizzaCustomizationHandler]:
        return self.__handlers_order

    @__getHandleOrders.setter
    def __setHandleOrders(self, handle_order: list[PizzaCustomizationHandler]) -> None:
        self.__handlers_order = handle_order

    @staticmethod
    def get_standard_user_configuration_structure(
        user_configuration: Dict[str, list[str] | str]
    ) -> dict[str : list[str]]:
        return {
            key: value if type(value) is list else [value]
            for key, value in user_configuration.items()
        }

    def apply_customizations(self) -> Pizza:
        prev_handler = None
        handler_instances = []
        for handler_class in self.__handlers_order:
            handler = handler_class(
                pizza_instance=self.pizza_instance,
                customization=self.customization_data,
            )
            if prev_handler:
                handler.set_next(prev_handler)
            prev_handler = handler
            handler_instances.append(handler)
        return handler_instances[0].handle_customization(self.user_configuration)


# TODO: Make sure any one can give a data structure as the following

"""
```python
data = {
    "Crusts": "Thin",
    "Sauces": ["Mayo", "Tomato"],
    "Toppings": ["Pepperoni", "Sausage", "Mushrooms"],
    "Cheese": "Mozzarella"
}
```
"""
