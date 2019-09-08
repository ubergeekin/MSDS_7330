# Import libraries
import pandas_datareader as web, datetime

# Read ticker symbols from file
symbol = []
with open('D:/TradingAnalysis/Amex/amex_symbols_clean.csv') as f:
    for line in f:
        symbol.append(line.strip())
f.close

# Define start date
start = datetime.datetime(2019, 1, 1)

# Define stop date
end = datetime.datetime(2019, 2, 6)

# Define path for csv output
path_out = ('D:/TradingAnalysis/Amex/')

#for first ticker symbol write a fresh copy of csv file for historical data
#on remaining ticker symbols append historical data to the file written for
#the first ticker symbol and do not include a header row
 
i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out+'amex_prices_volumes.csv')
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out+'amex_prices_volumes.csv',mode = 'a',header=False)
            print (i, symbol[i],'has data stored to csv file')
    continue
    i=i+1
