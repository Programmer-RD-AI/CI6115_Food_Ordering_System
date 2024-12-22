import datetime
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class GeneralObserver(OrderObserver):
    # Observe all of the general pizza making steps
    observer_logs: Dict[str, Any] = field(default_factory=dict)

    def update_observer(self, data: Any) -> None:
        self.observer_logs[datetime.datetime.now()] = data
        print(f"General Observer: {data}")
