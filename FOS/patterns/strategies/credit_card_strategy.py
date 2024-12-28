from .base_strategy import PaymentStrategy


class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print("Payment strategy: Credit Card")
        print(f"Amount: {amount}")
        print("Payment successful")
