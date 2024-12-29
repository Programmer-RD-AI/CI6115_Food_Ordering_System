import unittest
from ...models.payment import Payment
from ...models.price import Price
from ...models.user import User
from .credit_card_strategy import CreditCardStrategy


class TestPayment(unittest.TestCase):
    def setUp(self):
        self.price = Price()
        self.price.price = 15.99

    def test_credit_card_payment(self):
        strategy = CreditCardStrategy()
        user = User(username="test", email="test", password="test")
        payment = Payment(self.price, user, strategy)
        self.assertTrue(payment.process_payment())


if __name__ == "__main__":
    unittest.main()
