# CI6115_Food_Ordering_System

## Pizza Customization

[x] ◦ Allow customers to choose from a variety of crusts, sauces, toppings, and cheese options.
[x] ◦ Implement a system that enables customers to create custom pizza combinations and name them.
[x] Implement the Chain of Responsibility pattern for processing order customization requests, allowing different handlers to manage specific customizations.

## Ordering Process

[x] ◦ Design an intuitive ordering process that guides customers through crust selection, sauces, toppings, quantity, and order review.
[ ] ◦ Support both pickup and delivery options. For delivery, integrate with a mapping service to provide accurate delivery estimates.
[ ] Use the Observer pattern to notify users about order changes and provide real time updates on the progress of their orders.
[x] Apply the Builder pattern to construct complex orders with various customizations, ensuring a flexible and readable order creation process.

## User Profiles and Favorites

[x] ◦ Implement user profiles where customers can save their favorite pizza combinations.
[ ] ◦ Allow users to reorder their favorite combinations with a single click.

## Real-Time Order Tracking:

[ ] ◦ Integrate a real-time order tracking system that updates customers on the status of their pizza orders, including preparation and delivery stages.
[ ] ◦ Provide notifications for significant updates, such as the pizza being prepared or out for delivery.
[x] Utilize the State pattern to represent the different states of an order (placed, in preparation, out for delivery), making it easy to manage transitions and updates.

## Payment and Loyalty Program:

[x] ◦ Design a payment processing system that supports credit cards, digital wallets, and possibly a loyalty program for repeat customers (No need to integrate an actual payment service. Just mock the procedure for this requirement.).
[ ] ◦ Implement a loyalty program where customers earn points for each purchase, leading to discounts or free items.
[x] Apply the Strategy pattern for payment processing, allowing the system to easily integrate new payment methods and promotions.

## Seasonal Specials and Promotions:

[x] ◦ Allow the shop to easily introduce and manage seasonal specials and promotions, such as discounts on certain toppings or pizza sizes during specific times of the year.
[x] Use the Decorator pattern to enhance orders with additional features, such as extra toppings or special packaging.

## Feedback and Ratings:

[x] ◦ Enable customers to provide feedback and ratings for each pizza order.
[ ] ◦ Use the feedback to improve service and showcase highly-rated combinations to other customers.
[x] Apply the Command pattern to represent user actions, such as placing an order or providing feedback, as objects that can be queued, undone, or logged.
