from dataclasses import dataclass, field


@dataclass
class Loyalty:
    amount: int = field(default=None)

    def loyalty_points(self) -> float:
        return self.amount * 0.05
