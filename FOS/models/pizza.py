from dataclasses import dataclass, field

from .price import Price


@dataclass
class Pizza:
    __crusts: list[str] = field(default_factory=list)
    __sauces: list[str] = field(default_factory=list)
    __toppings: list[str] = field(default_factory=list)
    __cheeses: list[str] = field(default_factory=list)
    __packaging: str = field(default=None)
    name: str = f"""
    Crusts: {__crusts}\n
    Sauces: {__sauces}\n
    Toppings: {__toppings}\n
    Cheese: {__cheeses}\n
    """
    price: Price = field(default_factory=Price())

    def __str__(self):
        return self.name

    def calculate_price(self) -> float:
        self.price.price_calculator_for_cheeses(self.__cheeses)
        self.price.price_calculator_for_crusts(self.__crusts)
        self.price.price_calculator_for_sauces(self.__sauces)
        self.price.price_calculator_for_toppings(self.__toppings)
        return self.price.get_price()

    def set(self, current_data, new_data, object_data, expand: bool = True):
        if expand and current_data != []:
            object_data.extend(new_data)
        else:
            object_data = new_data
        return self.calculate_price()

    @property
    def get_crusts(self) -> list[str]:
        return self.__crusts

    @get_crusts.setter
    def set_crusts(self, crusts: list, expand: bool = True):
        return self.set(self.get_crusts(), crusts, self.__crusts)

    @property
    def get_sauces(self) -> list[str]:
        return self.__sauces

    @get_sauces.setter
    def set_sauces(self, sauces: list, expand: bool = True):
        return self.set(self.get_sauces(), sauces, self.__sauces)

    @property
    def get_toppings(self) -> list[str]:
        return self.__toppings

    @get_toppings.setter
    def set_toppings(self, toppings: list, expand: bool = True):
        return self.set(self.get_toppings(), toppings, self.__toppings)

    @property
    def get_cheeses(self) -> list[str]:
        return self.__cheese

    @get_cheeses.setter
    def set_cheeses(self, cheese: list, expand: bool = True):
        return self.set(self.get_cheeses(), cheese, self.__cheeses)

    @property
    def get_price(self) -> float:
        return self.calculate_price()

    @property
    def get_packaging(self) -> str:
        return self.__packaging

    @get_packaging.setter
    def set_packaging(self, packaging: str):
        self.__packaging = packaging
