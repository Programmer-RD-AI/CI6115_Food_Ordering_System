import datetime
from dataclasses import dataclass, field
from typing import Any, Dict


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
