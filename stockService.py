from subject import Subject
from copy import deepcopy

class StockService(Subject):
    def __init__(self) -> None:
        self._state: dict[str, int] = {}
        super().__init__()

    def getState(self):
        return deepcopy(self._state)
    
    def setState(self, new_state: dict[str, int]):
        self._state = new_state
        self.notify()