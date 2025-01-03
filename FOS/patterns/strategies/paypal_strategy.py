from .base_strategy import PaymentStrategy


class PayPalStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print("Payment strategy: PayPal")
        print(f"Amount: {amount}")
        print("Payment successful")
