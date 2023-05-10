import yfinance as yf
from sms import send_sms

aapl = yf.Ticker("AAPL").info
aapl_market_price = aapl['currentPrice']
aapl_previous_close_price = aapl['regularMarketPreviousClose']
print('Ticker: AAPL')
print('Market Price:', aapl_market_price)
print('Previous Close Price:', aapl_previous_close_price)

message = f'\nTicker: AAPL\nMarket Price: {aapl_market_price}\nPrevious Close Price: {aapl_previous_close_price}'
send_sms('+18636143724', message)
