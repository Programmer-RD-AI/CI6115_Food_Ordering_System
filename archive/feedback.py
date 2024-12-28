# ...existing code...
class Rating:
    def __init__(self):
        self._ratings = []

    def add_rating(self, rating: int):
        self._ratings.append(rating)

    def get_average_rating(self) -> float:
        if not self._ratings:
            return 0.0
        return sum(self._ratings) / len(self._ratings)


class Feedback:
    def __init__(self):
        self._feedbacks = []

    def add_feedback(self, feedback: str):
        self._feedbacks.append(feedback)

    def get_feedbacks(self):
        return self._feedbacks
