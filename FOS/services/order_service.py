class Order:
    def __init__(self, customer_id: str):
        self.order_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.pizzas: List[Pizza] = []
        self.state = OrderState.PLACED
        self.observers: List[OrderObserver] = []
        self.created_at = datetime.now()
        self.delivery_address: Optional[str] = None

    def add_observer(self, observer: OrderObserver) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(self.order_id, self.state, message)

    def add_pizza(self, pizza: Pizza) -> None:
        self.pizzas.append(pizza)

    def set_delivery_address(self, address: str) -> None:
        self.delivery_address = address

    def process_next_state(self) -> None:
        if isinstance(self.state, OrderState):
            self.state.next_state(self)
