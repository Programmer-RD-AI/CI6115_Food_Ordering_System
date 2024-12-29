from abc import ABC, abstractmethod


class OrderTrackingStrategy(ABC):
    @abstractmethod
    def track(self):
        """Generator method to yield status updates"""
        pass
