from ..base_command import Command


class SetTwoStarCommand(Command):
    def __init__(self, rating):
        self.rating = rating

    def execute(self):
        self.rating.set_rating(2)
