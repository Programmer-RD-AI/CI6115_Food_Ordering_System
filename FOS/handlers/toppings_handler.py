from . import JSON, Dict, Pizza, PizzaCustomizationHandler


class ToppingsCustomizationHandler(PizzaCustomizationHandler):
    def __init__(
        self,
        handler_type: str | None = "Toppings",
        customization: JSON = None,
        pizza_instance: Pizza = None,
    ) -> None:
        super().__init__(handler_type, customization, pizza_instance)

    def handle_customization(
        self, data: Dict[str, list], remove_duplicates: bool = False
    ) -> Pizza:
        match_bool, check_customization_matching, available_customizations = (
            self.matching_customization_requirements(data[self.handler_type])
        )
        if not match_bool:
            raise ValueError(
                f"The specified customizations ({', '.join(check_customization_matching)}) are not available. Please choose from the following selection of customizable customization settings: \n{available_customizations}"
            )
        del data[self.handler_type]
        return (
            self.__next_handler.handle_configuration(data)
            if self.__next_handler
            else None
        )
