import time

from ..models.pizza import Pizza
from ..models.user import User


class Order:
    def __init__(self, user: User):
        self.user = user
        self.state = None
        self.observers = []
        self.order_id = f"ORD-{hash(user.username)}-{hash(str(time.time()))}"[:10]
        self.pizzas = []  # List to store multiple pizzas

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(self.order_id, message, self.state)

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)
