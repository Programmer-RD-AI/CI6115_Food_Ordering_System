class LoyaltyRepository(object):
    def __init__(self, initial_datastore: Dict[str, Loyalty] = {}):
        self.loyalty_repository = initial_datastore or {}
