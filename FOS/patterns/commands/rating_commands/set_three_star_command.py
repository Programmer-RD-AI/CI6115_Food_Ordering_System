from ..base_command import Command
from ....models.rating import Rating


class SetThreeStarCommand(Command):
    def __init__(self, rating):
        self.rating = rating

    def execute(self):
        self.rating.set_rating(3)
