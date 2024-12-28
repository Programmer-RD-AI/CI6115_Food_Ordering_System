from FOS.patterns.commands.feedback_commands import (
    ClearFeedBackCommand,
    SetFeedBackCommand,
)
from FOS.patterns.commands.rating_commands import (
    ClearStarCommand,
    SetFiveStarCommand,
    SetFourStarCommand,
)

from ..authentication import Login, Register
from ..models.feedback import FeedBack
from ..models.pizza import Pizza
from ..models.rating import Rating
from ..models.user import User
from ..patterns.builder.pizza_builder import PizzaBuilder
from ..patterns.decorators.extra_cheese_decorator import ExtraCheeseDecorator
from ..patterns.decorators.get_pizza_for_free_decorator import GetPizzaForFreeDecorator
from ..patterns.decorators.seasonal_promotions_decorator import (
    SeasonalPromotionsDecorator,
)
from ..patterns.observers import CustomerNotifier, KitchenDisplay
from ..patterns.payment import Payment
from ..patterns.strategies import (
    CreditCardStrategy,
    DigitalWalletStrategy,
    PayPalStrategy,
)
from ..services.order_service import Order
from ..services.pizza_service import PizzaService
from ..utils.json_handler import JSON


class UI:
    def __init__(self):
        self.custom_notifier = CustomerNotifier()
        self.kitchen_display = KitchenDisplay()
        self.order = Order()

    def authentication(self) -> User:
        account_exist = input("Do you have an account? (y/n): ")
        if account_exist.lower() == "y":
            username_or_email = input("Enter your email/username: ")
            password = input("Enter your password: ")
            login = Login(
                username_or_email,
                password,
                username_or_email,
                self.authentication_repository,
            )
            response = login.login()
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
            return self.create_pizza_config()
        elif choice == "2":
            return self.order_already_existing_pizza()
        elif choice == "3":
            print("Exiting...")
            exit(0)

    def create_pizza_config(self):
        pizza_customization_data = JSON(file_name="pizza_customization.json").get_data()

        def display_options(category, options):
            print(f"\nSelect {category}:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            while True:
                try:
                    choice = int(
                        input(f"Enter number for {category} (1-{len(options)}): ")
                    )
                    if 1 <= choice <= len(options):
                        return [options[choice - 1]]
                except ValueError:
                    pass
                print("Invalid choice. Please try again.")

        pizza_builder = PizzaService(
            user_configuration={
                "Crusts": display_options("Crust", pizza_customization_data["Crusts"]),
                "Sauces": display_options("Sauce", pizza_customization_data["Sauces"]),
                "Toppings": display_options(
                    "Topping", pizza_customization_data["Toppings"]
                ),
                "Cheeses": display_options(
                    "Cheese", pizza_customization_data["Cheeses"]
                ),
            }
        ).apply_handlers()
        return pizza_builder

    def order_already_existing_pizza(self, user: User):
        popular_pizzas = user.get_popular_orders()
        for idx, popular_pizza in enumerate(popular_pizzas):
            print(f"{idx}: {popular_pizza}")
        choice = input("Enter the index of the pizza you want to order: ")
        return PizzaBuilder(popular_pizzas[int(choice)])

    def add_on_decorators(self, pizza_builder):
        # Always apply seasonal promotions
        pizza_builder = SeasonalPromotionsDecorator(pizza_builder).apply()

        # Ask for extra cheese
        if input("\nWould you like extra cheese? (y/n): ").lower() == "y":
            pizza_builder = ExtraCheeseDecorator(pizza_builder).apply()

        # Ask about free pizza promotion
        if (
            input(
                "\nWould you like to check if you're eligible for a free pizza? (y/n): "
            ).lower()
            == "y"
        ):
            pizza_builder = GetPizzaForFreeDecorator(pizza_builder).apply()

        return pizza_builder

    def pay(self, pizza: Pizza, user: User):
        print(f"\nTotal amount to pay: ${pizza.price.price:.2f}")

        # Display payment options
        print("\nPayment Methods:")
        print("1. Credit Card Payment")
        print("2. Digital Wallets Payment")
        print("3. PayPal Payment")
        # Get payment choice
        payment_strategies = {
            1: CreditCardStrategy(),
            2: DigitalWalletStrategy(),
            3: PayPalStrategy(),
        }

        while True:
            try:
                choice = int(input("\nSelect payment method (1-3): "))
                if choice in payment_strategies:
                    break
                print("Invalid choice. Please select 1-3.")
            except ValueError:
                print("Please enter a number between 1-3.")

        # Initialize payment with selected strategy
        payment = Payment(pizza.price, user, payment_strategies[choice])

        use_loyalty = (
            input("Do you want to use your loyalty points? (y/n)").lower() == "y"
        )
        payment.process_payment(use_loyalty)
        return True

    def tracking(self):
        placed_state = PlacedState()
        preparing_state = PreparingState()
        baking_state = BakingState()
        placed_state.next_state(order)
        preparing_state.next_state(order)
        baking_state.next_state(order)

        # Delivery / Pick Up
        delivery_tracker = DeliveryTracker()
        delivery_tracker.track()
        pickup_tracker = PickUpTracker()
        pickup_tracker.track()

    def feedback(self):
        # Rating using Command pattern
        rating = Rating()
        five_star = SetFiveStarCommand(rating)
        four_star = SetFourStarCommand(rating)

        # Execute rating commands
        five_star.execute()
        four_star.execute()
        print("Current average rating:", rating.get_average_rating())

        # Feedback using Command pattern
        feedback = FeedBack()
        set_feedback = SetFeedBackCommand()
        set_feedback.set_feedback(feedback)

        # Execute feedback commands
        set_feedback.execute("Delicious pizza, fast service!")
        print("Feedback list:", feedback.get_feedbacks())

        # Optional: Clear commands
        clear_rating = ClearStarCommand(rating)
        clear_feedback = ClearFeedBackCommand()
        clear_feedback.set_feedback(feedback)

    def main(self):
        user = self.authentication()
        pizza = self.add_on_decorators(self.home_page()).build()
        user.add_order(pizza)
        self.pay(pizza, user)
