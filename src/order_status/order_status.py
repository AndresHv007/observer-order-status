from .observer import Observer


class OrderStatus:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.status = "NEW"
        self.observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def set_status(self, status: str) -> None:
        self.status = status
        for observer in self.observers.copy():
            observer.update(self.order_id, self.status)
