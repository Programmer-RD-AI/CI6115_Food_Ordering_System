from abc import ABC, abstractmethod
from typing import Dict, Optional

from ...utils.helper_functions import find_excluded_options
from ...utils.json_handler import JSON
from ..builder.pizza_builder import PizzaBuilder


class PizzaCustomizationHandler(ABC):
    def __init__(
        self,
        handler_type: str | None = None,
        customization: JSON = None,
        builder: PizzaBuilder = None,
    ) -> None:
        self.handler_type = handler_type
        self.customization = customization
        self.builder = builder or PizzaBuilder()
        self.__next_handler: Optional[PizzaCustomizationHandler] = None

    def set_next(self, handler):
        self.__next_handler = handler
        return handler

    def get_next_handler(self):
        return self.__next_handler

    def matching_customization_requirements(self, handler_type_data: list) -> bool:
        available_customizations: list = self.customization.get_data()[
            self.handler_type
        ]
        check_customization_matching: list = find_excluded_options(
            handler_type_data, available_customizations
        )
        if check_customization_matching:
            return False, check_customization_matching, available_customizations
        return True, check_customization_matching, available_customizations

    @abstractmethod
    def handle_customization(self, data: Dict[str, list]) -> str: ...

    def get_builder(self):
        return self.builder
