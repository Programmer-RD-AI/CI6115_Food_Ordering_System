class FeedBack:
    def __init__(self):
        self.feedback: str = None

    def set_feedback(self, feedback: str) -> bool:
        if not feedback.strip():
            return False
        self.feedback = feedback
        return True

    def clear_feedback(self) -> None:
        self.feedback = None
