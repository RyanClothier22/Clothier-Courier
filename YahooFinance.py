import time

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def make_chart(stock, num):
    # Initialize the stock for yfinance API
    ticker = yf.Ticker(stock)

    # Obtain history as DataFrame
    history = ticker.history(period="1d", interval="5m")

    # Get Informational data and save it as string
    open_price = round(history["Open"].iloc[0], 2)
    close_price = round(history["Close"].iloc[-1], 2)
    percent_change = round((close_price - open_price) / open_price*100, 2)
    min_price = round(min(history["Open"].min(), history["Close"].min()), 2)
    max_price = round(max(history["Open"].max(), history["Close"].max()), 2)
    info = f"Start: ${open_price} | End: ${close_price} | High: ${max_price} | Low: ${min_price} | Change: {percent_change}%"

    # Put information into MatPlotLib Chart
    sf = history["Open"]
    df = pd.DataFrame({'Values': sf.values})
    x_values = np.arange(len(df["Values"]))
    plt.style.use('seaborn-v0_8-notebook')
    fig = plt.figure(num)
    plt.plot(x_values, df["Values"])
    plt.xticks([], [])
    plt.ylabel("Price ($)", fontsize=16)
    plt.title(stock, fontsize=32)

    return [fig, info]


def get_news(i):
    # Initialize the stock for yfinance API
    try:
        stock = yf.Ticker(i)
    except:
        news = {'title': "", 'link': ""}
    # Get top news story from Yahoo Finance News
    else:
        news = stock.news[0]
    # Save as dictionary with News Title and Link
    paper = {'title': news['title'], 'link': news['link']}
    return paper

if __name__ == "__main__":
    portfolio = ["SPY", "VTI", "QQQ", "BRK-B", "GOVT", "BND"]
    for i in portfolio:
        get_news(i)
    print(plt.style.available)