class LoyaltyService:
    def __init__(self, user_id: int, loyalty_program: str):
        self.user_id = user_id
        self.loyalty_program = loyalty_program
