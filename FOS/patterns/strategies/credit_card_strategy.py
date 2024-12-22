from .base_strategy import *


class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print("Payment strategy: Credit Card")
        print(f"Amount: {amount}")
        print("Payment successful")
