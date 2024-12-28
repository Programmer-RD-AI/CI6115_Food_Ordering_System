from ...patterns.builder.pizza_builder import PizzaBuilder
from .pizza_component import PizzaComponent


class PizzaDecorator(PizzaComponent):
    def __init__(self, builder: PizzaBuilder) -> None:
        self.__builder = builder

    def get_cheeses(self) -> list[str]:
        return self.__builder.get_cheeses()

    def set_cheeses(
        self,
        cheeses: list[str],
    ) -> None:
        self.__builder.set_cheeses(
            cheeses,
        )
        return self

    def get_packaging(self) -> list[str]:
        return self.__builder.get_packaging()

    def set_packaging(self, packaging: str):
        self.__builder.set_packaging(packaging)
        return self

    def get_builder(self):
        return self.__builder
