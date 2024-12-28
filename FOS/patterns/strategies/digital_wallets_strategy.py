from .base_strategy import PaymentStrategy


class DigitalWalletStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print("Payment strategy: Digital Wallets")
        print(f"Amount: {amount}")
        print("Payment successful")
