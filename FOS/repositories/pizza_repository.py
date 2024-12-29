from typing import Dict

from ..models.pizza import Pizza
from ..utils.json_handler import JSON


class PizzaRepository(object):
    def __init__(self, initial_datastore: Dict[Pizza, float] = None):
        self.json_handler = JSON(file_name="pizza_ratings.json")

        if initial_datastore is not None:
            self.pizza_repository = initial_datastore
        else:
            # Load existing ratings or start empty
            try:
                self.pizza_repository = self.json_handler.get_data()
            except:
                self.pizza_repository = {}
                self.json_handler.set_data({})

    def add_pizza_rating(self, pizza: Pizza, rating: float):
        pizza_key = str(pizza)  # Convert Pizza object to string for JSON
        if pizza_key not in self.pizza_repository:
            self.pizza_repository[pizza_key] = rating
        else:
            self.pizza_repository[pizza_key] = (
                self.pizza_repository[pizza_key] + rating
            ) / 2

        # Save updated ratings
        self.json_handler.set_data(self.pizza_repository)

    def get_most_popular_pizzas(self, top_n: int = 5) -> Dict[str, float]:
        if not self.pizza_repository:
            return {}

        sorted_pizzas = dict(
            sorted(
                self.pizza_repository.items(), key=lambda item: item[1], reverse=True
            )
        )

        if top_n is not None:
            return dict(list(sorted_pizzas.items())[:top_n])
        return sorted_pizzas

    def clear_pizzas(self) -> None:
        self.pizza_repository.clear()
        self.json_handler.set_data({})
