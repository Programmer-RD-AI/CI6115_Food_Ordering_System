from ....models.feedback import FeedBack
from ..base_command import Command


class ClearFeedBackCommand(Command):
    def __init__(self):
        self.feedback: FeedBack = None

    def set_feedback(self, feedback_obj):
        self.feedback: FeedBack = feedback_obj

    def execute(self):
        self.feedback.clear_feedback()
