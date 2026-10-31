from .observer import Observer


class CustomerNotifier(Observer):
    def __init__(self):
        self.messages = []

    def update(self, order_id: str, status: str) -> None:
        self.notify_customer(order_id, status)

    def notify_customer(self, order_id: str, status: str) -> None:
        self.messages.append(f"{order_id}:{status}")
