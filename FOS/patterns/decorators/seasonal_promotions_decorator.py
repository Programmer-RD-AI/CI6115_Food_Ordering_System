from datetime import datetime
from typing import Union

from ...models.pizza import Pizza
from ..builder.pizza_builder import PizzaBuilder
from ..handlers.base_handler import PizzaCustomizationHandler
from .pizza_decorator import PizzaDecorator


class SeasonalPromotionsDecorator(PizzaDecorator):
    def __init__(
        self, pizza_handler: Union[PizzaBuilder, PizzaCustomizationHandler, str, Pizza]
    ) -> None:
        if pizza_handler is None:
            raise ValueError("Pizza handler cannot be None")

        # Convert string/Pizza to PizzaBuilder if needed
        if isinstance(pizza_handler, (str, Pizza)):
            builder = PizzaBuilder(pizza_handler)
        # Handle both PizzaBuilder and decorated objects
        elif isinstance(pizza_handler, PizzaBuilder):
            builder = pizza_handler
        elif hasattr(pizza_handler, "get_builder"):
            builder = pizza_handler.get_builder()
        else:
            raise ValueError(f"Invalid pizza handler type: {type(pizza_handler)}")

        super().__init__(builder)
        self.holiday_seasons = {
            (12, 1, 12, 31): 20,  # Christmas/New Year
            (11, 20, 11, 30): 15,  # Black Friday
            (2, 1, 2, 14): 10,  # Valentine's
            (7, 1, 7, 31): 25,  # Summer Special
        }

    def is_holiday_season(self):
        current_date = datetime.now()
        current_month = current_date.month
        current_day = current_date.day

        for (
            start_month,
            start_day,
            end_month,
            end_day,
        ), discount in self.holiday_seasons.items():
            if start_month <= current_month <= end_month and (
                (start_month == current_month and current_day >= start_day)
                or (end_month == current_month and current_day <= end_day)
                or (start_month < current_month < end_month)
            ):
                return discount
        return 0

    def apply(self, Fore, Style):
        """Apply seasonal discount if applicable"""
        try:
            builder = self.get_builder()
            if not isinstance(builder, PizzaBuilder):
                builder = PizzaBuilder(builder)

            discount_percentage = self.is_holiday_season()
            if discount_percentage > 0:
                original_price = float(
                    builder.pizza.price.price
                )  # Use .price instead of .amount
                discount = (discount_percentage / 100) * original_price
                builder.pizza.price.price = (
                    original_price - discount
                )  # Set using .price
                print(
                    f"{Fore.GREEN}Applied {discount_percentage}% seasonal discount!{Style.RESET_ALL}"
                )

            return builder

        except Exception as e:
            print(
                f"{Fore.RED}Could not apply seasonal discount: {str(e)}{Style.RESET_ALL}"
            )
            if hasattr(self, "_builder"):
                return self._builder
            return builder
