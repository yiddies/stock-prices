import yfinance as yf
from sms import send_sms
import datetime
import time

# Define market open and close times in Eastern Standard Time (EST)
market_open_time = datetime.time(hour=9, minute=30, second=0)
noon_time = datetime.time(hour=12, minute=0, second=0)
market_close_time = datetime.time(hour=16, minute=0, second=0)

while True:
    # Get the current time in EST
    current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))).time()

    # If it's market open time, noon time, or market close time, send an SMS message with the AAPL ticker information
    if current_time == market_open_time:
        aapl = yf.Ticker("AAPL").info
        market_price = aapl['currentPrice']
        previous_close_price = aapl['regularMarketPreviousClose']
        message = f'Ticker: AAPL\nMarket Price: {market_price}\nPrevious Close Price: {previous_close_price}'
        send_sms('number', message)
    elif current_time == noon_time:
        aapl = yf.Ticker("AAPL").info
        market_price = aapl['currentPrice']
        previous_close_price = aapl['regularMarketPreviousClose']
        message = f'Ticker: AAPL\nMarket Price: {market_price}\nPrevious Close Price: {previous_close_price}'
        send_sms('number', message)
    elif current_time == market_close_time:
        aapl = yf.Ticker("AAPL").info
        market_price = aapl['currentPrice']
        previous_close_price = aapl['regularMarketPreviousClose']
        message = f'Ticker: AAPL\nMarket Price: {market_price}\nPrevious Close Price: {previous_close_price}'
        send_sms('number', message)
    
    # Wait for 1 minute before checking the time again
    time.sleep(60)
