from ...models.pizza import Pizza


class PizzaBuilder:
    def __init__(
        self,
        pizza: Pizza | None = None,
    ) -> None:
        self.pizza = pizza or Pizza()
        self.quantity: int = 1

    def get_crusts(self) -> list[str]:
        return self.pizza.get_crusts()

    def set_crusts(self, crusts: list[str], **kwargs) -> None:
        self.pizza.set_crusts(crusts, **kwargs)
        return self

    def get_sauces(self) -> list[str]:
        return self.pizza.get_sauces()

    def set_sauces(self, sauces: list[str], **kwargs) -> None:
        self.pizza.set_sauces(sauces, **kwargs)
        return self

    def get_toppings(self) -> list[str]:
        return self.pizza.get_toppings()

    def set_toppings(self, toppings: list[str], **kwargs) -> None:
        self.pizza.set_toppings(toppings, **kwargs)
        return self

    def get_cheeses(self) -> list[str]:
        return self.pizza.get_cheeses()

    def set_cheeses(self, cheeses: list[str], **kwargs) -> None:
        self.pizza.set_cheeses(cheeses, **kwargs)
        return self

    def get_quantity(self) -> list[str]:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        return self

    def get_packaging(self) -> list[str]:
        return self.pizza.get_packaging()

    def set_packaging(self, packaging: str):
        self.pizza.set_packaging(packaging)
        return self

    def build(self, list=False):
        return [self.pizza * self.quantity] if list else self.pizza
