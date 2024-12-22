from FOS.authentication.login import Login
from FOS.authentication.register import Register
from FOS.models.user import User
from FOS.repositories.authentication_repository import AuthenticationRepository
from FOS.models.pizza import Pizza
from FOS.patterns.strategies import (
    CreditCardStrategy,
    DigitalWalletsStrategy,
    PayPalStrategy,
)


class Main(object):
    authentication_repository: AuthenticationRepository = AuthenticationRepository()
    user: User = None
    pizza: Pizza = None

    def authentication(self):
        account_exist = input("Do you have an account? (y/n): ")
        if account_exist.lower() == "y":
            username_or_email = input("Enter your email/username: ")
            password = input("Enter your password: ")
            l = Login(
                username_or_email,
                password,
                username_or_email,
                self.authentication_repository,
            )
            response = l.login()
            if response:
                return True
            else:
                print("Invalid credentials")
                return self.authentication()
        else:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")
            r = Register(username, password, email, self.authentication_repository)
            response: User = r.register()
            if response:
                return response
            else:
                print("Invalid credentials")
                return self.authentication()

    def home_page(self):
        # This would have their most ordered pizza, and such and there is an option to create a pizza
        # Also show promotions and such, they would need to be applied as required
        choice = input(
            """
        1. Order New Pizza
        2. Order Already Existing Pizza
        3. Exit
        """
        )
        if choice == "1":
            self.order_new_pizza()
        elif choice == "2":
            self.order_already_existing_pizza()
        elif choice == "3":
            print("Exiting...")
            exit(0)

    # Types of Order
    def order_new_pizza(self):
        pass

    def order_already_existing_pizza(self):
        popular_pizzas = self.user.get_popular_orders()
        for idx, popular_pizza in enumerate(popular_pizzas):
            print(f"{idx}: {popular_pizza}")
        choice = input("Enter the index of the pizza you want to order: ")
        self.pizza: Pizza = popular_pizzas[int(choice)]
        self.user.add_order(pizza)
        self.payment()

    # Payment
    def payment(self):
        # also include the payment and loyalty program.
        price = self.pizza.get_price()
        print(f"Total Price: {price}")
        print("Payment Options: ")
        print("1. Credit Card")
        print("2. Digital Wallet")
        print("3. Paypal")
        choice = input("Enter the payment option: ")
        if choice == "1":
            CreditCardStrategy().pay(price)
        elif choice == "2":
            DigitalWalletsStrategy().pay(price)
        elif choice == "3":
            PayPalStrategy().pay(price)
        else:
            print("Invalid payment option")
            self.payment()

    def real_time_tracking(self): ...
    def main(self):
        self.user: User = self.authentication()
        self.home_page()


if __name__ == "__main__":
    m = Main()
    m.main()
