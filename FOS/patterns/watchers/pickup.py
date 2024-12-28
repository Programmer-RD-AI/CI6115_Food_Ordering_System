# ...existing code...
class PickUpTracker:
    def __init__(self):
        self.status = "Waiting for pickup"

    def track(self):
        print(f"Pickup status: {self.status}")
        # ...other logic for pickup tracking...
        self.status = "Picked up"
        print(f"Pickup status updated to: {self.status}")
