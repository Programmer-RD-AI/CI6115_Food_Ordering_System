from ...patterns.builder.pizza_builder import PizzaBuilder
from .pizza_component import PizzaComponent


class PizzaDecorator(PizzaComponent):
    def __init__(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def get_cheeses(self) -> list[str]:
        return self._builder.get_cheeses()

    def set_cheeses(self, cheeses: list[str]) -> None:
        self._builder.set_cheeses(cheeses)
        return self

    def get_packaging(self) -> str:
        return self._builder.get_packaging()

    def set_packaging(self, packaging: str) -> None:
        self._builder.set_packaging(packaging)
        return self

    def get_builder(self):
        return self._builder
