@dataclass
class User:
    favorite_pizzas: List[Pizza] = field(default_factory=list)

    def add_favorite_pizza(self, pizza: Pizza) -> None:
        if pizza not in self.favorite_pizzas:
            self.favorite_pizzas.append(pizza)

    def get_favorite_pizzas(self) -> List[Pizza]:
        return self.favorite_pizzas
