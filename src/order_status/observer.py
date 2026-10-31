from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: str, status: str) -> None:
        raise NotImplementedError
