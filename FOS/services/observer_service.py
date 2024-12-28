from ..patterns.observers.order_observer import OrderObserver


class ObserverService:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: OrderObserver):
        self.observers.append(observer)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.update(message)
