from ..utils.json_handler import JSON
from dataclasses import dataclass, field


@dataclass
class Price:
    file_name: str = field(default="pricing.json")
    currency: str = field(default="USD")
    price: float = field(default=0.0)

    def __post_init__(self):
        self.json_instance = JSON(file_name=self.file_name)
        self.data = self.json_instance.get_data()

    def __str__(self):
        return f"{self.price:.2f} {self.currency}"

    def get_price(self):
        return self.price

    def price_calculator_for_crusts(self, crusts: list[str]) -> tuple[float, float]:
        return self.__price_calculator(crusts, "Crusts")

    def price_calculator_for_sauces(self, sauces: list[str]) -> tuple[float, float]:
        return self.__price_calculator(sauces, "Sauces")

    def price_calculator_for_toppings(self, toppings: list[str]) -> tuple[float, float]:
        return self.__price_calculator(toppings, "Toppings")

    def price_calculator_for_cheeses(self, chesses: list[str]) -> tuple[float, float]:
        return self.__price_calculator(chesses, "Cheeses")

    def __price_calculator(
        self, values, column_name: str, add_to_price: bool = True
    ) -> tuple[float, float]:
        """
        Calculate price based on values from a specific column.

        Args:
            values: Single value or list of values (can be nested)
            column_name: Name of the price column to use
            add_to_price: Whether to add the calculated price to the running total

        Returns:
            tuple: (total_price, current_calculation)
        """
        # Handle single value case
        if not isinstance(values, list):
            values = [values]

        # Flatten list and filter valid values in one pass
        valid_prices = [
            self.data[column_name][val]
            for val in values
            if isinstance(val, str) and val in self.data[column_name]
        ]

        # Calculate price
        calculated_price = sum(valid_prices)

        # Update total price if requested
        if add_to_price:
            self.price += calculated_price

        return self.price, calculated_price
