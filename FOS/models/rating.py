from dataclasses import dataclass, field


@dataclass
class Rating:
    rating: int = field(default=None)

    def set_rating(self, rating: int):
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        self.rating = rating

    def clear_rating(self):
        self.rating = None
