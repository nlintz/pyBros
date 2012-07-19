import rpy2.robjects as robjects
import getSymbols

r = robjects.r 
r('require(quantmod)')

dataDict={}

tickers=getSymbols.returnStockTickers()
for ticker in tickers:
    data = r('data = getSymbols(ticker, auto.assign=FALSE, from="2007-01-01")')
    dataDict[ticker]=data
