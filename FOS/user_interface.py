import asyncio
import os
import random

from colorama import Fore, Style, init

from .authentication import Login, Register
from .models.feedback import FeedBack
from .models.payment import Payment
from .models.pizza import Pizza
from .models.rating import Rating
from .models.user import User
from .patterns.builder.pizza_builder import PizzaBuilder
from .patterns.commands.feedback_commands import SetFeedBackCommand
from .patterns.commands.rating_commands import (
    SetFiveStarCommand,
    SetFourStarCommand,
    SetOneStarCommand,
    SetThreeStarCommand,
    SetTwoStarCommand,
)
from .patterns.decorators.extra_cheese_decorator import ExtraCheeseDecorator
from .patterns.decorators.get_pizza_for_free_decorator import GetPizzaForFreeDecorator
from .patterns.decorators.seasonal_promotions_decorator import (
    SeasonalPromotionsDecorator,
)
from .patterns.observers import CustomerNotifier, KitchenDisplay
from .patterns.states import BakingState, PlacedState, PreparingState
from .patterns.strategies import (
    CreditCardStrategy,
    DigitalWalletStrategy,
    PayPalStrategy,
)
from .patterns.strategies.tracker import (
    DeliveryTracker,
    OrderTrackingStrategy,
    PickUpTracker,
)
from .repositories import AuthenticationRepository
from .services.order_service import Order
from .services.pizza_service import PizzaService
from .utils.json_handler import JSON

init()


class UI:
    def __init__(self):
        self.custom_notifier = CustomerNotifier()
        self.kitchen_display = KitchenDisplay()
        self.order = None
        self.authentication_repository = AuthenticationRepository()
        self.BORDER = "═" * 50
        self.MENU_BORDER = "─" * 50
        self.LOGO = """
        🍕 PIZZA ORDERING SYSTEM 🍕
        """

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def print_header(self, text: str):
        self.clear_screen()
        print(f"\n{self.BORDER}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}{text.center(50)}{Style.RESET_ALL}")
        print(f"{self.BORDER}\n")

    def authentication(self) -> User:
        self.print_header(self.LOGO)
        print(f"{Fore.CYAN}Welcome! Please authenticate to continue.{Style.RESET_ALL}")
        account_exist = input(
            f"\n{Fore.GREEN}Do you have an account? (y/n):{Style.RESET_ALL} "
        )

        if account_exist.lower() == "y":
            print(f"\n{Fore.BLUE}═══ LOGIN ═══{Style.RESET_ALL}")
            username_or_email = input(f"{Fore.WHITE}Email/Username:{Style.RESET_ALL} ")
            password = input(f"{Fore.WHITE}Password:{Style.RESET_ALL} ")
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
            username = input(f"{Fore.WHITE}Username:{Style.RESET_ALL} ")
            password = input(f"{Fore.WHITE}Password:{Style.RESET_ALL} ")
            email = input(f"{Fore.WHITE}Email:{Style.RESET_ALL} ")
            r = Register(username, password, email, self.authentication_repository)
            response: User = r.register()
            if response:
                return response
            else:
                print("Invalid credentials")
                return self.authentication()

    def home_page(self, user: User):
        # This would have their most ordered pizza, and such and there is an option to create a pizza
        # Also show promotions and such, they would need to be applied as required
        self.print_header(f"Welcome back, {user.username}!")
        print(f"{Fore.YELLOW}Your Loyalty Points:{Style.RESET_ALL} {user.get_loyalty}")

        choice = input(
            f"""
        {Fore.GREEN}Please select an option:{Style.RESET_ALL}

        1. 🆕 Order New Pizza
        2. 📋 Order from Previous Orders
        3. 🚪 Exit

        {Fore.CYAN}Choice:{Style.RESET_ALL} """
        )
        if choice == "1":
            return self.create_pizza_config()
        elif choice == "2":
            return self.order_already_existing_pizza(user)
        elif choice == "3":
            print("Exiting...")
            exit(0)

    def create_pizza_config(self):
        pizza_customization_data = JSON(file_name="pizza_customization.json").get_data()

        def display_options(category, options):
            print(f"\n{Fore.YELLOW}【 {category} Options 】{Style.RESET_ALL}")
            print(self.MENU_BORDER)
            for i, option in enumerate(options, 1):
                print(f"{Fore.CYAN}{i}.{Style.RESET_ALL} {option}")
            print(f"{Fore.GREEN}0.{Style.RESET_ALL} Done selecting")
            print(self.MENU_BORDER)

            selections = []
            while True:
                if selections:
                    print(f"\n{Fore.YELLOW}Current selections:{Style.RESET_ALL}")
                    for item in selections:
                        print(f"• {item}")

                try:
                    choice = int(
                        input(f"\nSelect {category} (0 to finish, 1-{len(options)}): ")
                    )
                    if choice == 0:
                        if not selections:
                            print(
                                f"{Fore.RED}Please select at least one option{Style.RESET_ALL}"
                            )
                            continue
                        return selections
                    if 1 <= choice <= len(options):
                        selections.append(options[choice - 1])
                        print(
                            f"{Fore.GREEN}Added {options[choice - 1]}{Style.RESET_ALL}"
                        )
                    else:
                        print(
                            f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}"
                        )
                except ValueError:
                    print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")

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

        if not popular_pizzas:
            print(f"{Fore.YELLOW}No previous orders found!{Style.RESET_ALL}")
            return self.create_pizza_config()

        print(f"\n{Fore.CYAN}Your Previous Orders:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        for idx, pizza in enumerate(popular_pizzas, 1):
            print(f"{Fore.GREEN}{idx}.{Style.RESET_ALL} {pizza}")
        print(self.MENU_BORDER)

        while True:
            try:
                choice = int(input(f"\nSelect pizza (1-{len(popular_pizzas)}): "))
                if 1 <= choice <= len(popular_pizzas):
                    return PizzaBuilder(popular_pizzas[choice - 1])
                print(
                    f"{Fore.RED}Invalid choice. Please enter 1-{len(popular_pizzas)}{Style.RESET_ALL}"
                )
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
                return self.create_pizza_config()

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
        self.print_header("Payment")
        print(f"{Fore.GREEN}Total Amount:{Style.RESET_ALL} ${pizza.price.price:.2f}")
        print(
            f"{Fore.YELLOW}Available Loyalty Points:{Style.RESET_ALL} {user.get_loyalty}"
        )

        print(f"\n{Fore.CYAN}Payment Methods:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        print("1. 💳 Credit Card")
        print("2. 📱 Digital Wallet")
        print("3. 🌐 PayPal")
        print(self.MENU_BORDER)
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

    def get_tracker(self) -> OrderTrackingStrategy:
        form_of_order = input("Will you delivery your order? (y/n)").lower()
        if form_of_order == "y":
            print("\nEnter your delivery coordinates:")
            delivery_lat = float(input("Latitude (eg: 7.2906): "))
            delivery_lon = float(input("Longitude (eg: 80.6337): "))
            delivery_coords = (delivery_lat, delivery_lon)

            # Generate nearby store coordinates (0-10km difference)
            import random

            store_lat = delivery_lat - random.uniform(0, 0.1)  # ~0-10km
            store_lon = delivery_lon - random.uniform(0, 0.1)  # ~0-10km
            store_coords = (store_lat, store_lon)
            tracker = DeliveryTracker(store_coords, delivery_coords)
        else:
            tracker = PickUpTracker()
        return tracker

    async def tracking(self, order: Order, order_tracker: OrderTrackingStrategy):
        self.print_header("Order Tracking")

        # Attach observers
        order.attach(self.custom_notifier)
        order.attach(self.kitchen_display)

        # Order placed
        placed_state = PlacedState()
        placed_state.next_state(order)
        order.notify_observers("Order has been placed!")
        await asyncio.sleep(random.randint(1, 3))

        # Preparing
        preparing_state = PreparingState()
        preparing_state.next_state(order)
        order.notify_observers("Your order is being prepared by our chefs!")
        await asyncio.sleep(random.randint(2, 4))

        # Baking
        baking_state = BakingState()
        baking_state.next_state(order)
        order.notify_observers("Your pizza is in the oven!")
        await asyncio.sleep(random.randint(3, 5))

        print(f"\n{Fore.YELLOW}Delivery Status:{Style.RESET_ALL}")
        for status in order_tracker.track():
            order.notify_observers(status)
            print(f"\n{Fore.CYAN}[{status}]{Style.RESET_ALL}")
            await asyncio.sleep(random.randint(2, 4))

    def feedback(self):
        # Initialize rating and feedback
        rating = Rating()
        feedback = FeedBack()

        ratings = {
            1: "⭐            Poor",
            2: "⭐⭐          Fair",
            3: "⭐⭐⭐        Good",
            4: "⭐⭐⭐⭐      Excellent",
            5: "⭐⭐⭐⭐⭐    Outstanding",
        }

        print(f"{Fore.YELLOW}Please rate your experience:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        for rating_idx, description in ratings.items():
            print(f"{rating_idx}. {description}")
        print(self.MENU_BORDER)
        while True:
            try:
                user_rating = int(input("\nEnter your rating (1-5): "))
                if 1 <= user_rating <= 5:
                    break
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Create and execute rating command based on user input
        rating_commands = {
            1: SetOneStarCommand(rating),
            2: SetTwoStarCommand(rating),
            3: SetThreeStarCommand(rating),
            4: SetFourStarCommand(rating),
            5: SetFiveStarCommand(rating),
        }
        rating_commands[user_rating].execute()

        # Get user feedback
        print("\nPlease share your experience with us:")
        user_feedback = input("> ")

        # Execute feedback command
        set_feedback = SetFeedBackCommand()
        set_feedback.set_feedback(feedback)
        set_feedback.execute(user_feedback)

        print("\nThank you for your feedback!")
        print(f"Your rating: {'⭐' * user_rating}")
        print(f"Your comment: {user_feedback}")
        return user_rating

    async def main(self):
        while True:
            user = self.authentication()
            self.order = Order(user)
            pizza = self.add_on_decorators(self.home_page(user)).build()
            user.add_order(pizza)
            tracker = self.get_tracker()
            self.pay(pizza, user)
            print(f"\n{Fore.GREEN}Payment successful!{Style.RESET_ALL}")
            tracking = asyncio.create_task(self.tracking(self.order, tracker))
            tracking = await tracking
            self.feedback()
            if input("Order Another Pizza?").lower().lower() == "n":
                break
