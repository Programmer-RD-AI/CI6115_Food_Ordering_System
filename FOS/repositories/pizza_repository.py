from typing import Dict

from ..models.pizza import Pizza


class PizzaRepository(object):
    def __init__(self, initial_datastore: Dict[str, Pizza] = {}):
        self.pizza_repository = initial_datastore or {}

    def add_pizza(self, name: str, pizza: Pizza) -> None:
        self.pizza_repository[name] = pizza

    def get_pizza(self, name: str) -> Pizza:
        return self.pizza_repository.get(name)

    def remove_pizza(self, name: str) -> Pizza:
        return self.pizza_repository.pop(name)

    def get_all_pizzas(self) -> tuple:
        return self.pizza_repository.values()

    def get_pizza_names(self) -> tuple:
        return self.pizza_repository.keys()

    def update_pizza(self, name: str, pizza: Pizza) -> Pizza:
        self.pizza_repository[name] = pizza
        return pizza

    def clear_pizzas(self) -> None:
        self.pizza_repository.clear()
