from typing import Dict

from ..handlers import (
    CheesesCustomizationHandler,
    CrustsCustomizationHandler,
    PizzaCustomizationHandler,
    SaucesCustomizationHandler,
    ToppingsCustomizationHandler,
)
from ..models.pizza import Pizza
from ..utils.json_handler import JSON


class PizzaCustomizationService(object):
    def __init__(
        self,
        pizza_instance: Pizza = None,
    ):
        self.pizza_instance: Pizza = Pizza() if not pizza_instance else pizza_instance

    @property
    def __getHandleOrders(self) -> list[PizzaCustomizationHandler]:
        return self.__handlers_order

    @__getHandleOrders.setter
    def __setHandleOrders(self, handle_order: list[PizzaCustomizationHandler]) -> None:
        self.__handlers_order = handle_order

    @staticmethod
    def get_standard_user_configuration_structure(
        user_configuration: Dict[str, list[str] | str],
    ) -> dict[str : list[str]]:
        return {
            key: value if type(value) is list else [value]
            for key, value in user_configuration.items()
        }

    def apply_customizations(self) -> Pizza:
        pass


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
