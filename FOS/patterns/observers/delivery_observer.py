from dataclasses import dataclass, field
from typing import Any, Dict
import datetime

@dataclass
class DeliveryObserver(OrderObserver):
    # Would be called in a certain amt of period every time, and would give a update on the delivery
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"Deliver Observer: {data}")
