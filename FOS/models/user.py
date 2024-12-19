from typing import Dict
from ..models.pizza import Pizza


class User:
    user_id_counter: int = 0

    def __init__(self, ordered_combinations: Dict[Pizza, int], name: str):
        self.name = name
        self.ordered_combinations: Dict[Pizza, int] = {}
        self.user_id = self.user_id_counter
        self.user_id_counter += 1

    def add_order(self, pizza: Pizza) -> None:
        if pizza in self.ordered_combinations:
            self.ordered_combinations[str(pizza)] += 1
        else:
            self.ordered_combinations[str(pizza)] = 1

    def get_order_count(self, pizza: Pizza) -> int:
        return self.ordered_combinations.get(str(pizza), 0)

    def get_popular_orders(self):
        return sorted(
            self.ordered_combinations,
            key=lambda x: self.ordered_combinations[x],
            reverse=True,
        )
