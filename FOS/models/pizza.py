from .price import Price
from dataclasses import dataclass, field
from typing import List


@dataclass
class Pizza:
    __crusts: List[str] = field(default_factory=list)
    __sauces: List[str] = field(default_factory=list)
    __toppings: List[str] = field(default_factory=list)
    __cheeses: List[str] = field(default_factory=list)
    __packaging: str = field(default=None)
    name: str = field(init=False)
    price: Price = field(default_factory=Price)

    def __str__(self):
        return f"""
        Crusts: {self.__crusts}
        Sauces: {self.__sauces}
        Toppings: {self.__toppings}
        Cheese: {self.__cheeses}
        """

    @classmethod
    def from_string(cls, pizza_str: str) -> "Pizza":
        """Create Pizza instance from string representation"""
        pizza = cls()
        try:
            # Clean and split the string
            components = pizza_str.strip().split("\n")

            for component in components:
                component = component.strip()
                if component.startswith("Crusts:"):
                    pizza.__crusts = eval(component.replace("Crusts:", "").strip())
                elif component.startswith("Sauces:"):
                    pizza.__sauces = eval(component.replace("Sauces:", "").strip())
                elif component.startswith("Toppings:"):
                    pizza.__toppings = eval(component.replace("Toppings:", "").strip())
                elif component.startswith("Cheese:"):
                    pizza.__cheeses = eval(component.replace("Cheese:", "").strip())

            # Calculate price based on components
            pizza.calculate_price()
            return pizza

        except Exception as e:
            raise ValueError(f"Invalid pizza string format: {e}")

    def calculate_price(self) -> float:
        self.price.price_calculator_for_cheeses(self.__cheeses)
        self.price.price_calculator_for_crusts(self.__crusts)
        self.price.price_calculator_for_sauces(self.__sauces)
        self.price.price_calculator_for_toppings(self.__toppings)
        return self.price.get_price()

    def set(
        self, current_data: list, new_data: list, object_ref: list, expand: bool = True
    ) -> float:
        if expand and current_data:
            object_ref.extend(new_data)
        else:
            object_ref.clear()
            object_ref.extend(new_data)
        return self.calculate_price(), object_ref

    @property
    def crusts(self) -> List[str]:
        return self.__crusts

    @crusts.setter
    def crusts(self, value: List[str]):
        price, self.__crusts = self.set(self.__crusts, value, self.__crusts)

    @property
    def sauces(self) -> List[str]:
        return self.__sauces

    @sauces.setter
    def sauces(self, value: List[str]):
        price, self.__sauces = self.set(self.__sauces, value, self.__sauces)

    @property
    def toppings(self) -> List[str]:
        return self.__toppings

    @toppings.setter
    def toppings(self, value: List[str]):
        price, self.__toppings = self.set(self.__toppings, value, self.__toppings)

    @property
    def cheeses(self) -> List[str]:
        return self.__cheeses

    @cheeses.setter
    def cheeses(self, value: List[str]):
        price, self.__cheeses = self.set(self.__cheeses, value, self.__cheeses)

    @property
    def packaging(self) -> str:
        return self.__packaging

    @packaging.setter
    def packaging(self, value: str):
        self.__packaging = value

    @property
    def price_total(self) -> float:
        return self.calculate_price()
