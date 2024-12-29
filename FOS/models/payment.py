# ...existing code...
from FOS.models.price import Price
from .user import User
from .loyalty import Loyalty
from ..patterns.strategies.base_strategy import PaymentStrategy


class Payment:
    def __init__(self, price: Price, user: User, strategy: PaymentStrategy):
        self.price = price
        self.user = user
        self.strategy = strategy

    def apply_loyalty_points(self):
        """Apply loyalty points discount to the price."""
        self.price.price -= self.user.get_loyalty
        return self.price.price

    def process_payment(self, apply_loyalty: bool = False):
        """Process the payment, applying any relevant discounts."""
        self.apply_loyalty_points() if apply_loyalty else None
        self.strategy.pay(self.price.price)
        self.user.add_loyalty_points(
            loyalty=Loyalty(self.price.price)
        ) if not apply_loyalty else None
        print(f"Payment processed for amount: {self.price.price}")
