import random
import time
from datetime import datetime

from .order_tracking_strategy import OrderTrackingStrategy


class PickUpTracker(OrderTrackingStrategy):
    def __init__(self):
        self.states = [
            "🏪 Order received",
            "👨‍🍳 Pizza preparation started",
            "🔥 Baking your pizza",
            "✨ Fresh out of the oven",
            "📦 Ready for pickup",
            "✅ Order picked up",
        ]

    def track(self):
        estimated_time = 1200  # 20 minutes initial estimate

        for state in self.states:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            status = f"[{current_time}] {state}"

            if "picked up" not in state.lower():
                mins = int(estimated_time // 60)
                status += f"\nEstimated ready in {mins} minutes"

            yield status
            time.sleep(random.uniform(2, 4))
            estimated_time = max(0, estimated_time - random.randint(120, 240))
