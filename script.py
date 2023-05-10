import yfinance as yf

#AAPL why is it aapl, shouldn't it be appl?
aapl = yf.Ticker("AAPL").info
market_price = aapl['currentPrice']
previous_close_price = aapl['regularMarketPreviousClose']
print(previous_close_price)
print(market_price)
