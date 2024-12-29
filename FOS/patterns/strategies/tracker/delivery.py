from datetime import datetime
import random
import time
from .order_tracking_strategy import OrderTrackingStrategy
from ....utils.delivery_estimator import DeliverEstimator


class DeliveryTracker(OrderTrackingStrategy):
    def __init__(
        self,
        store_coordinates: tuple[float, float],
        delivery_coordinates: tuple[float, float],
    ):
        self.estimator = DeliverEstimator(store_coordinates, delivery_coordinates)
        self.states = [
            "🏪 Order received and being prepared",
            "👨‍🍳 Pizza is being crafted with care",
            "🔥 Your pizza is in the oven",
            "✨ Fresh out of the oven!",
            "🚗 Out for delivery",
            "📍 Driver nearby",
            "✅ Delivered",
        ]

    def track(self):
        estimated_time = self.estimator.get_estimated_delivery_time()

        for state in self.states:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            status = f"[{current_time}] {state}"

            if "Delivered" not in state:
                mins = int(estimated_time // 60)
                status += f"\nEstimated delivery in {mins} minutes"

            yield status
            time.sleep(random.uniform(2, 5))
            estimated_time = max(0, estimated_time - random.randint(180, 300))
