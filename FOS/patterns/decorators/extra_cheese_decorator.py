from .pizza_decorator import PizzaDecorator


class ExtraCheeseDecorator(PizzaDecorator):
    def __init__(
        self,
        pizza_handler,
        factor_of_extra_cheese: int = 2,
    ) -> None:
        self.new_cheeses = []
        self.factor_of_extra_cheese = factor_of_extra_cheese
        super().__init__(pizza_handler)

    def apply(self):
        self.new_cheeses.extend(
            [self.__builder.get_cheeses()] * self.factor_of_extra_cheese
        )
        self.__builder.set_cheeses(self.new_cheeses)
        return self.get_builder()
