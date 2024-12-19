from routingpy.routers import OSRM


class DeliverEstimator:
    def __init__(
        self, initial_coordinates: list[int], final_coordinates: list[int], client: OSRM
    ) -> None:
        self.client = client or OSRM()
        self.origin = initial_coordinates
        self.destination = final_coordinates

    def get_estimated_delivery_time(self) -> float:
        route = self.client.route(self.origin, self.destination)
        return route.duration / 60
