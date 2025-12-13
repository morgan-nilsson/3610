from observer import Observer
from stockService import StockService, Subject

class StockObserverStats(Observer):

    def __init__(self) -> None:
        self._previous_states: list[dict[str, int]] = []
        super().__init__()

    def update(self, subject: Subject) -> None:
        if isinstance(subject, StockService):
            print("Stats module received a new update")
            self._previous_states.append(subject.getState())
        else:
            print("Update passed incorrect parameter subject must be of StockService")

    def getMaxPrice(self, stock: str) -> int:
        max = 0
        for state in self._previous_states:
            if state[stock] > max:
                max = state[stock]

        return max

    def getMinPrice(self, stock: str) -> int:
        min = 1000000000000000
        for state in self._previous_states:
            if state[stock] < min:
                min = state[stock]

        return min