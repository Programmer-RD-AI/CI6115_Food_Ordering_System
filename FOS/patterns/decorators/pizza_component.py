from abc import ABC, abstractmethod
from typing import List


class PizzaComponent(ABC):
    @abstractmethod
    def get_cheeses(self) -> List[str]:
        pass

    @abstractmethod
    def set_cheeses(self, cheeses: List[str]) -> None:
        pass

    @abstractmethod
    def get_packaging(self) -> str:
        pass

    @abstractmethod
    def set_packaging(self, packaging: str) -> None:
        pass
