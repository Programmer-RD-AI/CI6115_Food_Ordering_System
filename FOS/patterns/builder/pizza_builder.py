from typing import List, Optional

from ...models.pizza import Pizza


class PizzaBuilder:
    def __init__(self, pizza: Optional[Pizza] = None) -> None:
        if isinstance(pizza, str):
            pizza = Pizza().from_string(pizza)
        self.pizza = pizza if pizza is not None else Pizza()
        self.quantity: int = 1

    def get_crusts(self) -> List[str]:
        return self.pizza.crusts

    def set_crusts(self, crusts: List[str]) -> None:
        self.pizza.crusts = crusts
        return self

    def get_sauces(self) -> List[str]:
        return self.pizza.sauces

    def set_sauces(self, sauces: List[str]) -> None:
        self.pizza.sauces = sauces
        return self

    def get_toppings(self) -> List[str]:
        return self.pizza.toppings

    def set_toppings(self, toppings: List[str]) -> None:
        self.pizza.toppings = toppings
        return self

    def get_cheeses(self) -> List[str]:
        return self.pizza.cheeses

    def set_cheeses(self, cheeses: List[str]) -> None:
        self.pizza.cheeses = cheeses
        return self

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity
        return self

    def get_packaging(self) -> str:
        return self.pizza.packaging

    def set_packaging(self, packaging: str) -> None:
        self.pizza.packaging = packaging
        return self

    def build(self, list=False):
        return self.pizza
