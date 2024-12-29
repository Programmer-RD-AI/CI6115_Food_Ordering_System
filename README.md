# 🍕 Pizza Ordering System

A comprehensive pizza ordering system implementing various design patterns to create a flexible, maintainable and feature-rich application.

## 🌟 Features

### 🛠 Pizza Customization

- Multiple crust options, sauces, toppings and cheese selections
- Custom pizza combinations with naming capability
- Chain of Responsibility pattern for processing customizations

### 🛍 Ordering Process

- Intuitive step-by-step ordering flow
- Support for delivery and pickup options
- Real-time delivery estimates using coordinates
- Builder pattern for complex order creation

### 👤 User Management

- Profile creation and management
- Saved favorite combinations
- Order history tracking
- One-click reordering of favorites

### 📍 Real-Time Tracking

- Live order status updates
- Push notifications for order stages
- State pattern for order status management
- Delivery/Pickup tracking with estimated times

### 💳 Payment & Loyalty

- Multiple payment methods:
  - Credit Card
  - Digital Wallet
  - PayPal
- Loyalty points system
- Points redemption for discounts
- Strategy pattern for payment processing

### 🎉 Promotions

- Seasonal discounts
- Holiday specials
- Extra toppings promotions
- Decorator pattern for special offers

### ⭐ Ratings & Feedback

- Order rating system
- Customer feedback collection
- Popular combinations showcase
- Command pattern for feedback actions

## 🏗 Design Patterns Used

1. **Chain of Responsibility**

   - Pizza customization handling
   - Order validation

2. **Builder Pattern**

   - Pizza construction
   - Order assembly

3. **Observer Pattern**

   - Order status notifications
   - Delivery updates

4. **State Pattern**

   - Order status management
   - Delivery tracking

5. **Strategy Pattern**

   - Payment processing
   - Delivery calculations

6. **Decorator Pattern**

   - Pizza customizations
   - Special offers

7. **Command Pattern**
   - Order operations
   - Feedback handling

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/pizza-ordering-system.git

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Usage Example

```python
from FOS.user_interface import UI
import asyncio

ui = UI()
asyncio.run(ui.main())
```

## Architeture

```plaintext
FOS/
├── models/          # Data models
├── patterns/        # Design pattern implementations
├── services/        # Business logic
├── utils/          # Helper utilities
├── repositories/   # Data access
└── ui/            # User interface
```

## ✨ Features Showcase

### Pizza Creation

```python
pizza_builder = (
    PizzaBuilder()
    .set_crusts(["Thin"])
    .set_sauces(["Tomato"])
    .set_toppings(["Pepperoni"])
    .set_cheeses(["Mozzarella"])
    .build()
)
```

### Payment Processing

```python
payment = Payment(
    price=pizza.price,
    user=current_user,
    strategy=CreditCardStrategy()
)
payment.process_payment(use_loyalty=True)
```

### Order Tracking

```python
tracker = DeliveryTracker(store_coords, delivery_coords)
for status in tracker.track():
    print(f"Order Status: {status}")
```
