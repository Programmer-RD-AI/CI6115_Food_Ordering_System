from FOS.patterns.observers.custom_notifier import CustomerNotifier
from FOS.patterns.observers.kitchen_display import KitchenDisplay
from FOS.models.user import User
from FOS.services.pizza_service import PizzaService

# Setup Observers
custom_notifier = CustomerNotifier()
kitchen_display = KitchenDisplay()

# Authentication
## Utilize FOS/authentication

user = User(
    "testing",
    "prdai_2008",
    "go2ranuga@gmail.com",
)
print(user)

# Create Custom Pizza
## kitchen_observer

pizza_config = {
    "Crusts": [
        "Thin Crust",
    ],
    "Sauces": [
        "Tomato Sauce",
    ],
    "Toppings": [
        "Pepperoni",
    ],
    "Cheeses": [
        "Mozzarella",
    ],
}
pizza_builder = PizzaService(user_configuration=pizza_config).apply_handlers()
print(pizza_builder.build())
# Create Already Created Pizza
## kitchen_observer

# Decorator Pattern for Additional Features
## kitchen_observer
## Seasonal Specials and Promotions

# Payment
## Take into consideration loyalty points and such

# States
## Placed
## Preparing
## Baking

# Delivery / Pick Up
## Implement custom delivery and pick up trackers maybe? so that till the food is handed off to the customer this will repeat on

# Rating / Feedback
