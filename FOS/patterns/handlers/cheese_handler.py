from . import Pizza, JSON, PizzaCustomizationHandler, Dict


class CheesesCustomizationHandler(PizzaCustomizationHandler):
    def __init__(
        self,
        handler_type: str | None = "Cheeses",
        customization: JSON = None,
    ) -> None:
        super().__init__(handler_type, customization)

    def handle_customization(
        self, data: Dict[str, list], remove_duplicates: bool = False
    ):
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
