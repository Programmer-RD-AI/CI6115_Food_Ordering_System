from .patterns.observers import CustomerNotifier, KitchenDisplay
from .authentication import Login, Register
from .models.user import User
from .models.pizza import Pizza
from .utils.json_handler import JSON
from .services.pizza_service import PizzaService
from .patterns.decorators.seasonal_promotions_decorator import (
    SeasonalPromotionsDecorator,
)
from .patterns.decorators.extra_cheese_decorator import ExtraCheeseDecorator
from .patterns.decorators.get_pizza_for_free_decorator import GetPizzaForFreeDecorator
from .patterns.builder.pizza_builder import PizzaBuilder
from .models.payment import Payment
from .patterns.strategies import (
    CreditCardStrategy,
    DigitalWalletStrategy,
    PayPalStrategy,
)
from .models.rating import Rating
from .models.feedback import FeedBack
from .patterns.commands.rating_commands import (
    SetFiveStarCommand,
    SetFourStarCommand,
    SetOneStarCommand,
    SetTwoStarCommand,
    SetThreeStarCommand,
)
from .patterns.commands.feedback_commands import (
    SetFeedBackCommand,
)
from .services.order_service import Order
from .patterns.states import PlacedState, PreparingState, BakingState
import asyncio
import random
from .patterns.strategies.tracker import (
    DeliveryTracker,
    PickUpTracker,
    OrderTrackingStrategy,
)
from .repositories import AuthenticationRepository
from .repositories import PizzaRepository
from colorama import init, Fore, Style
import os

init()


class UI:
    def __init__(self):
        self.custom_notifier = CustomerNotifier()
        self.kitchen_display = KitchenDisplay()
        self.order = None
        self.authentication_repository = AuthenticationRepository()
        self.pizza_repository = PizzaRepository()
        #
        self.BORDER = "═" * 50
        self.MENU_BORDER = "─" * 50
        self.LOGO = """
        🍕 PIZZA ORDERING SYSTEM 🍕
        """

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def save_favorite_pizza(self, user: User, pizza: Pizza):
        user.add_favorite_pizza(pizza)
        print(f"{Fore.GREEN}Pizza saved to favorites!{Style.RESET_ALL}")

    def reorder_favorite_pizza(self, user: User):
        favorite_pizzas = user.get_favorite_pizzas()

        if not favorite_pizzas:
            print(f"{Fore.YELLOW}No favorite pizzas found!{Style.RESET_ALL}")
            return None

        print(f"\n{Fore.CYAN}Your Favorite Pizzas:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        for idx, pizza in enumerate(favorite_pizzas, 1):
            print(f"{Fore.GREEN}{idx}.{Style.RESET_ALL} {pizza}")
        print(self.MENU_BORDER)

        while True:
            try:
                choice = int(input(f"\nSelect pizza (1-{len(favorite_pizzas)}): "))
                if 1 <= choice <= len(favorite_pizzas):
                    return PizzaBuilder(favorite_pizzas[choice - 1])
                print(
                    f"{Fore.RED}Invalid choice. Please enter 1-{len(favorite_pizzas)}{Style.RESET_ALL}"
                )
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")

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
            print(f"\n{Fore.BLUE}═══ {response} ═══{Style.RESET_ALL}")
            if response:
                return login.user
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
        self.print_header(f"Welcome back, {user.username}!")

        print(f"{Fore.YELLOW}Your Loyalty Points:{Style.RESET_ALL} {user.get_loyalty}")

        choice = input(f"""
        {Fore.GREEN}Please select an option:{Style.RESET_ALL}

        1. 🆕 Order New Pizza
        2. 📋 Order from Your Previous Orders
        3. 🌟 Order from Top Rated Pizzas
        4. ❤️ Reorder Favorite Pizza
        5. 🚪 Exit

        {Fore.CYAN}Choice:{Style.RESET_ALL} """)

        if choice == "1":
            return self.create_pizza_config()
        elif choice == "2":
            return self.order_already_existing_pizza(user)
        elif choice == "3":
            return self.order_top_rated_pizza()
        elif choice == "4":
            return self.reorder_favorite_pizza(user)
        elif choice == "5":
            print("Exiting...")
            exit(0)

    def order_top_rated_pizza(self):
        self.print_header("Top Rated Pizzas")

        popular_pizzas = self.pizza_repository.get_most_popular_pizzas(top_n=5)

        if not popular_pizzas:
            print(f"{Fore.YELLOW}No rated pizzas found yet!{Style.RESET_ALL}")
            return self.create_pizza_config()

        print(f"\n{Fore.CYAN}Most Popular Pizzas:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        for idx, (pizza, rating) in enumerate(popular_pizzas.items(), 1):
            stars = "⭐" * int(rating)
            print(f"{Fore.GREEN}{idx}.{Style.RESET_ALL} {pizza} {stars} ({rating:.1f})")
        print(self.MENU_BORDER)

        while True:
            try:
                choice = int(input(f"\nSelect pizza (1-{len(popular_pizzas)}): "))
                if 1 <= choice <= len(popular_pizzas):
                    selected_pizza = list(popular_pizzas.keys())[choice - 1]
                    return selected_pizza
                print(
                    f"{Fore.RED}Invalid choice. Please enter 1-{len(popular_pizzas)}{Style.RESET_ALL}"
                )
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")

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
            selected_set = set()  # Track unique selections

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
                        selected_item = options[choice - 1]
                        if selected_item in selected_set:
                            print(
                                f"{Fore.RED}You've already selected {selected_item}!{Style.RESET_ALL}"
                            )
                            continue
                        selections.append(selected_item)
                        selected_set.add(selected_item)
                        print(f"{Fore.GREEN}Added {selected_item}{Style.RESET_ALL}")
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
        pizza_builder = SeasonalPromotionsDecorator(pizza_builder).apply(Fore, Style)

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

    def review_order(self):
        print(f"\n{Fore.YELLOW}Current Order:{Style.RESET_ALL}")
        print(self.MENU_BORDER)
        for idx, pizza in enumerate(self.order.pizzas, 1):
            print(f"{Fore.GREEN}{idx}.{Style.RESET_ALL} {pizza}")
        print(self.MENU_BORDER)

    def pay(self, order: Order, user: User):
        total_price = sum(pizza.price.price for pizza in order.pizzas)
        self.print_header("Payment")
        print(f"{Fore.GREEN}Total Amount:{Style.RESET_ALL} ${total_price:.2f}")
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
        payment = Payment(total_price, user, payment_strategies[choice])

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

    def feedback(self, pizza: Pizza):
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
        self.pizza_repository.add_pizza_rating(pizza, user_rating)
        print("\nThank you for your feedback!")
        print(f"Your rating: {'⭐' * user_rating}")
        print(f"Your comment: {user_feedback}")
        return user_rating

    async def main(self):
        user = self.authentication()
        while True:
            self.order = Order(user)
            while True:
                pizza = self.add_on_decorators(self.home_page(user)).build()
                self.order.add_pizza(pizza)
                user.add_order(pizza)
                self.review_order()
                if input("Add another pizza to this order? (y/n): ").lower() == "n":
                    break
            tracker = self.get_tracker()
            self.pay(self.order, user)
            print(f"\n{Fore.GREEN}Payment successful!{Style.RESET_ALL}")
            tracking = asyncio.create_task(self.tracking(self.order, tracker))
            tracking = await tracking
            for pizza in self.order.pizzas:
                self.feedback(pizza)
            if input("Place another order? (y/n): ").lower() == "n":
                break
