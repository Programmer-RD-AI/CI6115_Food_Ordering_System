from datetime import datetime
from typing import Union

from ..handlers.base_handler import PizzaCustomizationHandler
from .pizza_decorator import PizzaDecorator


class SeasonalPromotionsDecorator(PizzaDecorator):
    def __init__(self, pizza_builder: Union[PizzaDecorator, PizzaCustomizationHandler]):
        self.pizza_builder = pizza_builder
        self.holiday_seasons = {
            # (start_month, start_day, end_month, end_day): discount_percentage
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

    def apply(self):
        discount_percentage = self.is_holiday_season()
        if discount_percentage > 0:
            original_price = self.pizza_builder.pizza.price.price
            discount = (discount_percentage / 100) * original_price
            self.pizza_builder.pizza.price.amount = original_price - discount
            print(f"Applied {discount_percentage}% seasonal discount!")
        return self.pizza_builder
