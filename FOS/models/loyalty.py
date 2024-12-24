from .user import User


class Loyalty:
    def __init__(self, user: User, amount: int):
        self.user = user
        self.amount = amount

    def loyalty_points(self) -> float:
        return self.amount * 0.05
