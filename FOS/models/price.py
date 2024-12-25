from dataclasses import dataclass, field

from ..utils.json_handler import JSON


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
        self, iterator_values, column_name: str, add_to_price: bool = True
    ) -> tuple[float, float]:
        price = sum(
            [
                self.data[column_name][iterator_value]
                for iterator_value in iterator_values
            ]
        )
        if add_to_price:
            self.price += price
        return self.price, price
