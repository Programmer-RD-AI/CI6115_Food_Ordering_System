import datetime
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class PickUpObserver(OrderObserver):
    # User can pick up items and it will shown that
    # Would be called in a certain amt of period every time, and would give a update on the delivery
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"PickUp Observer: {data}")
