from typing import Dict

from ...models.pizza import Pizza
from ...utils.json_handler import JSON
from ..builder.pizza_builder import PizzaBuilder
from .base_handler import PizzaCustomizationHandler


class SaucesCustomizationHandler(PizzaCustomizationHandler):
    def __init__(
        self,
        handler_type: str | None = "Sauces",
        customization: JSON = None,
    ) -> None:
        super().__init__(
            handler_type,
            customization,
        )

    # @override
    def handle_customization(
        self,
        data: Dict[str, list],
        builder: PizzaBuilder,
        remove_duplicates: bool = False,
    ) -> Pizza:
        match_bool, check_customization_matching, available_customizations = (
            self.matching_customization_requirements(data[self.handler_type])
        )
        if not match_bool:
            raise ValueError(
                f"The specified customizations ({', '.join(check_customization_matching)}) are not available. Please choose from the following selection of customizable customization settings: \n{available_customizations}"
            )
        builder = builder.set_sauces(data[self.handler_type])
        # del data[self.handler_type]
        next_handler = self.get_next_handler()
        return (
            next_handler.handle_customization(data, builder)
            if next_handler
            else builder
        )
