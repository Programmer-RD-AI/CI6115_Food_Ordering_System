from typing import Dict, List
from ..models.pizza import Pizza
from ..utils.json_handler import JSON

from .loyalty import Loyalty
from dataclasses import dataclass, field


@dataclass
class User:
    user_id_counter: int = field(default=0, init=False)
    user_id: int = field(init=False)
    username: str = field(default=None)
    password: str = field(default=None)
    email: str = field(default=None)
    ordered_combinations: Dict[Pizza, int] = field(default_factory=dict)
    loyalty_collection: List[Loyalty] = field(default_factory=list)

    def __post_init__(self):
        try:
            json_data = JSON(file_name="users.json").get_data()
            user_ids = json_data.get("user_ids", [])
            self.user_id_counter = user_ids[-1] if user_ids else 0
        except (IndexError, KeyError, FileNotFoundError):
            self.user_id_counter = 0
        self.user_id_counter += 1
        self.user_id = self.user_id_counter

    def add_order(self, pizza: Pizza) -> None:
        pizza = str(pizza)
        if pizza in self.ordered_combinations.keys():
            self.ordered_combinations[pizza] += 1
        else:
            self.ordered_combinations[pizza] = 1

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
    def get_loyalty(self) -> float:
        return sum([loyalty.loyalty_points() for loyalty in self.loyalty_collection])

    @get_loyalty.setter
    def set_loyalty(self, loyalty: Loyalty, update: bool = True):
        self.loyalty_collection.append(loyalty) if update else [loyalty]

    def __str__(self):
        return f"""{self.user_id} \n {self.username} \n {self.password} \n {self.email} \n {self.ordered_combinations} \n {self.loyalty_collection}"""
