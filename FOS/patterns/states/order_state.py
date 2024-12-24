from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def next_state(self, order) -> None:
        pass
