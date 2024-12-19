import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


class OrderObserver(ABC):
    @abstractmethod
    def update_observer(self, data: Any) -> None: ...


@dataclass
class GeneralObserver(OrderObserver):
    # Observe all of the general pizza making steps
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"General Observer: {data}")


@dataclass
class DeliveryObserver(OrderObserver):
    # Would be called in a certain amt of period every time, and would give a update on the delivery
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"Deliver Observer: {data}")


@dataclass
class PickUpObserver(OrderObserver):
    # User can pick up items and it will shown that
    # Would be called in a certain amt of period every time, and would give a update on the delivery
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"PickUp Observer: {data}")


@dataclass
class OrderSubject:
    observers: Dict[dataclass, list[OrderObserver]] = field(
        default_factory=dict
    )  # each instance gets its own unique dictionary

    def attach(self, observer: OrderObserver) -> None:
        self.observers.setdefault(observer.__class__, []).append(observer)

    def detach(self, observer: OrderObserver) -> bool:
        if observer.__class__ not in self.observers:
            return False
        self.observers[observer.__class__].remove(observer)
        return True

    def notify(self, data: Any, observer: OrderObserver = None) -> None:
        observer_iterator = (
            self.observers.items()
            if not observer
            else [(observer.__class__), (observer)]
        )
        for observer_class, observers in observer_iterator:
            for observer in observers:
                observer.update_observer(data)
        return
