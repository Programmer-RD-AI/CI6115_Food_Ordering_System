from dataclasses import dataclass, field

from .price import Price


@dataclass
class Pizza:
    __crusts: list[str] = field(default_factory=list)
    __sauces: list[str] = field(default_factory=list)
    __toppings: list[str] = field(default_factory=list)
    __cheeses: list[str] = field(default_factory=list)
    __packaging: str = field(default=None)
    name: str = field(init=False)
    price: Price = field(default_factory=Price)

    def __post_init__(self):
        self.name = f"""
        Crusts: {self.__crusts}
        Sauces: {self.__sauces}
        Toppings: {self.__toppings}
        Cheese: {self.__cheeses}
        """

    def __str__(self):
        return self.name

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
    def crusts(self) -> list[str]:
        return self.__crusts

    @crusts.setter
    def crusts(self, value: list):
        price, self.__crusts = self.set(self.__crusts, value, self.__crusts)

    @property
    def sauces(self) -> list[str]:
        return self.__sauces

    @sauces.setter
    def sauces(self, value: list):
        self.set(self.__sauces, value, self.__sauces)

    @property
    def toppings(self) -> list[str]:
        return self.__toppings

    @toppings.setter
    def toppings(self, value: list):
        self.set(self.__toppings, value, self.__toppings)

    @property
    def cheeses(self) -> list[str]:
        print(self.__cheeses)
        return self.__cheeses

    @cheeses.setter
    def cheeses(self, value: list):
        print(value)
        self.set(self.__cheeses, value, self.__cheeses)

    @property
    def packaging(self) -> str:
        return self.__packaging

    @packaging.setter
    def packaging(self, value: str):
        self.__packaging = value

    @property
    def price_total(self) -> float:
        return self.calculate_price()
