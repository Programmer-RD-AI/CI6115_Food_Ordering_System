from ..base_command import Command
from ....models.rating import Rating


class ClearStarCommand(Command):
    def __init__(self, rating):
        self.rating = rating

    def execute(self):
        self.rating.clear_rating()
