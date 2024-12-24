from abc import ABC, abstractmethod


class PizzaComponent(ABC):

    @abstractmethod
    def set_cheeses(self):
        pass

    @abstractmethod
    def set_packaging(self):
        pass

    @abstractmethod
    def get_cheeses(self):
        pass

    @abstractmethod
    def get_packaging(self):
        pass
