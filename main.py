from FOS.services.pizza_customization import PizzaCustomizationService

data = {
    "Crusts": "Thin Crust",
    "Sauces": ["Mayo", "Tomato"],
    "Toppings": ["Pepperoni", "Sausage", "Mushrooms"],
    "Cheese": "Mozzarella",
}

pizza_customization_service = PizzaCustomizationService(user_configuration=data)
pizza = pizza_customization_service.apply_customizations()
print(pizza)
