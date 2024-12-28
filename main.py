# ...existing code...
from uuid import uuid4

from FOS.models.user import User

# Assume these classes exist in the directory for Decorator, Payment, States, Delivery, and Feedback
from FOS.patterns.decorators.extra_cheese_decorator import (  # , SeasonalSpecials
    ExtraCheeseDecorator,
)
from FOS.patterns.payment import Payment
from FOS.patterns.states import BakingState, PlacedState, PreparingState
from FOS.patterns.watchers.delivery import DeliveryTracker
from FOS.patterns.watchers.feedback import Feedback, Rating
from FOS.patterns.watchers.pickup import PickUpTracker
from FOS.services.order_service import Order
from FOS.services.pizza_service import PizzaService

# Setup Observers

# Authentication
user = User("testing", "prdai_2008", "go2ranuga@gmail.com")
print(user)

# Create Custom Pizza (kitchen_observer could notify observers about pizza creation)
pizza_config = {
    "Crusts": ["Thin Crust"],
    "Sauces": ["Tomato Sauce"],
    "Toppings": ["Pepperoni"],
    "Cheeses": ["Mozzarella"],
}
pizza_builder = PizzaService(user_configuration=pizza_config).apply_handlers()
pizza = pizza_builder.build()
print(pizza)
custom_notifier.update(uuid4(), "Custom pizza created.")
kitchen_display.update(uuid4(), "Custom pizza ready on screen.")

# Create Already Created Pizza (kitchen_observer)
already_created_pizza = pizza_builder.build()
print(already_created_pizza)
custom_notifier.update(uuid4(), "Existing pizza creation repeated.")
kitchen_display.update(uuid4(), "Existing pizza displayed on screen.")

# Decorator Pattern for Additional Features (kitchen_observer, Seasonal Specials)
extra_cheesed_pizza = ExtraCheeseDecorator(pizza_builder)
extra_cheesed_pizza.apply_extra()
# seasonal = SeasonalSpecials()
# seasonal.apply_special("Winter Promotion")

# Payment (consider loyalty points)
pay = Payment(price=already_created_pizza.price, loyalty_points=10)
pay.process_payment()
order = Order(user)

# States (Placed, Preparing, Baking)
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

# Rating / Feedback
rating = Rating()
rating.add_rating(5)
rating.add_rating(4)
print("Current average rating:", rating.get_average_rating())

feedback = Feedback()
feedback.add_feedback("Delicious pizza, fast service!")
print("Feedback list:", feedback.get_feedbacks())
# ...existing code...
