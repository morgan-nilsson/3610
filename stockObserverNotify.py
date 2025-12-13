from observer import Observer
from stockService import StockService, Subject

class StockObserverNotify(Observer):

    def __init__(self, conditions) -> None:
        self.conditions = conditions

    def update(self, subject) -> None:
        if isinstance(subject, StockService):
            state = subject.getState()
            for stock in state.keys():
                # for every condition
                for condition in self.conditions:
                    # if the condition given is true notify
                    if condition(stock, state[stock]):
                        print("NOTIFICATION:", stock, "is at", state[stock])
        else:
            print("Update passed incorrect parameter subject must be of StockService")
