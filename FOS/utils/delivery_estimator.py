import math


class DeliverEstimator:
    def __init__(
        self,
        initial_coordinates: tuple[float, float],
        final_coordinates: tuple[float, float],
    ) -> None:
        self.origin = initial_coordinates
        self.destination = final_coordinates
        self.avg_speed = 30  # km/h

    def calculate_distance(self) -> float:
        """Calculate distance between two points using Haversine formula"""
        R = 6371  # Earth's radius in km

        lat1, lon1 = self.origin
        lat2, lon2 = self.destination

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
            math.radians(lat1)
        ) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance

    def get_estimated_delivery_time(self) -> float:
        """Returns estimated delivery time in seconds"""
        distance = self.calculate_distance()
        time_hours = distance / self.avg_speed
        return time_hours * 3600  # Convert to seconds
