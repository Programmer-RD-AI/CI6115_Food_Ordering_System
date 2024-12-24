from typing import Dict, List
from ..models.pizza import Pizza
from ..utils.json_handler import JSON
from .loyalty import Loyalty


class User:
    user_id_counter: int = JSON("users.json").get_data()["user_ids"][-1]

    def __init__(
        self,
        username: str,
        password: str,
        email: str,
        ordered_combinations: Dict[Pizza, int] = {},
    ):
        self.user_id_counter += 1
        self.username = username
        self.password = password
        self.email = email
        self.user_id = self.user_id_counter
        self.ordered_combinations: Dict[Pizza, int] = {}
        self.loyalty_collection: List[Loyalty] = []

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

    @property
    def get_username(self):
        return self.username

    @get_username.setter
    def set_username(self, new_username):
        self.username = new_username

    @property
    def get_password(self):
        return self.password

    @get_password.setter
    def set_password(self, new_password):
        self.password = new_password

    @property
    def get_email(self):
        return self.email

    @get_email.setter
    def set_email(self, new_email):
        self.email = new_email

    @property
    def get_user_id(self):
        return self.user_id

    @get_user_id.setter
    def set_user_id(self, new_user_id):
        self.user_id = new_user_id

    @property
    def get_loyalty(self) -> List[Loyalty]:
        return self.loyalty_collection

    @get_loyalty.setter
    def set_loyalty(self, loyalty: Loyalty, update: bool = True):
        self.loyalty_collection.append(loyalty) if update else [loyalty]
