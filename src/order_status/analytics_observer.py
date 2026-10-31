from .observer import Observer


class AnalyticsObserver(Observer):
    def __init__(self):
        self.events = []

    def update(self, order_id: str, status: str) -> None:
        self.events.append({"order_id": order_id, "status": status})
