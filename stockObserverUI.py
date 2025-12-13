from observer import Observer
from stockService import StockService, Subject

class StockObserverUI(Observer):
    def update(self, subject: Subject) -> None:
        if isinstance(subject, StockService):
            state = subject.getState()
            print("\n====== Update =========")
            for stock in state.keys():
                print(stock, "has", state[stock], "in stock")
        else:
            print("Update passed incorrect parameter subject must be of StockService")