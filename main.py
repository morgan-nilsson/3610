from stockService import StockService
from stockObserverUI import StockObserverUI
from stockObserverNotify import StockObserverNotify
from stockObserverStats import StockObserverStats
import random

stockService = StockService()

# shows real time changes
observerUI = StockObserverUI()
stockService.attach(observerUI)

# sends notifications when the conditions are met
def ChipsHits20(stock, price):
    return stock == "Chips" and price >= 20
# guaranteed to happen the very first turn every time
def MAndMsLessThan10005(stock, price):
    return stock == "MAndM" and price <= 10005
observerNotifications = StockObserverNotify([ChipsHits20, MAndMsLessThan10005])
stockService.attach(observerNotifications)

# gather stats over the lifetime
observerStats = StockObserverStats()
stockService.attach(observerStats)
    
# initial state of the inventory
state = {}
state["SourPatchKids"] = 50
state["MAndM"] = 10000
state["Chips"] = 10
# this will count as an update
stockService.setState(state)

# name and possible change values
stocks = ["SourPatchKids", "MAndM", "Chips"]
changes = [10, -10, +5]

# amount of changes to the inventory
num_of_turns = 2

# simulate the inventory moving N number of turns
# you might not always get an notification worthy state if so just run it again
for i in range(num_of_turns):
    stock = random.choice(stocks)
    newState = stockService.getState()
    newState[stock] += random.choice(changes)
    stockService.setState(newState)

# use the stats module to get max and min inventory for each item
for stock in stockService.getState().keys():
    print()
    print(stock)
    print("Max inventory", observerStats.getMaxPrice(stock))
    print("Min inventory", observerStats.getMinPrice(stock))