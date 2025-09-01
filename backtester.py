#Today we're making a simple python backtester using python modules
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG #SMA = simple moving avegrage from this we also import the stock/crypto (have a play around with it)

# We're going to create a simple stratergy looking over 2 SMA's and see if we should sell or buy
class MySMAStratergy(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10) # This looks into a 10 day SMA 
        self.ma2 = self.I(SMA, price, 20) # This looks into a 20 day SMA 
    
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy() # so if the 2 crossover each other then we'll buy
        elif crossover(self.ma2, self.ma1):
            self.sell()

# Now our simple stratergy is done, we'll backtest it
backtest = Backtest(GOOG, MySMAStratergy, commission=.002, exclusive_orders=True)
#we're looking into the stratergy to evaluate and commisson is the percentage we pay per transaction
stats = backtest.run()
print(stats)
backtest.plot()

