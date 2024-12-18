from . import ABC, JSON, Dict, Pizza, abstractmethod, find_excluded_options


class PizzaCustomizationHandler(ABC):
    def __init__(
        self,
        handler_type: str | None = None,
        customization: JSON = None,
        pizza_instance: Pizza = None,
    ) -> None:
        self.handler_type = handler_type
        self.__pizza_instance: Pizza = pizza_instance
        self.customization = customization
        self.__next_handler: Optional[PizzaCustomizationHandler] = None

    def set_next(self, handler):
        self.__next_handler = handler
        self.__next_handler.__set_pizza_instance(self.__pizza_instance)
        return handler

    def __set_pizza_instance(self, pizza_instance: Pizza) -> None:
        self.__pizza_instance = pizza_instance

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
