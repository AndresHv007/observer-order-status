from .observer import Observer


class AuditObserver(Observer):
    def __init__(self):
        self.entries = []

    def update(self, order_id: str, status: str) -> None:
        self.record(order_id, status)

    def record(self, order_id: str, status: str) -> None:
        self.entries.append((order_id, status))
