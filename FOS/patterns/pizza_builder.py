from ..models.pizza import Pizza


class PizzaBuilder:
    def __init__(
        self,
        pizza: Pizza | None = None,
    ) -> None:
        self.pizza = pizza or Pizza()
        self.quantity: int = 1

    def set_crusts(self, crusts: list[str], **kwargs) -> None:
        self.pizza.set_crusts(crusts, **kwargs)
        return self

    def set_sauces(self, sauces: list[str], **kwargs) -> None:
        self.pizza.set_sauces(sauces, **kwargs)
        return self

    def set_toppings(self, toppings: list[str], **kwargs) -> None:
        self.pizza.set_toppings(toppings, **kwargs)
        return self

    def set_cheeses(self, cheeses: list[str], **kwargs) -> None:
        self.pizza.set_cheeses(cheeses, **kwargs)
        return self

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        return self

    def build(self):
        return [self.pizza * self.quantity]
