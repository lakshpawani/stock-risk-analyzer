import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)

user_input = input("Enter stock tickers separated by spaces: ").upper()
tickers = user_input.split()    
data = yf.download(tickers, period="1y", auto_adjust=True)

# Removes stocks with no data and dates with missing prices.
prices = data["Close"].dropna(axis=1, how="all").dropna()
if prices.empty:
    print("No valid stock tickers found.")
    exit()
current_price = prices.iloc[-1]
returns = (prices.iloc[-1] / prices.iloc[0]) - 1
daily_returns = prices.pct_change().dropna()
daily_volatility = daily_returns.std()
# Annualizes daily volatility using approximately 252 trading days per year.
annualized_volatility = daily_volatility * np.sqrt(252)
# Simplified Sharpe ratio: return divided by annualized volatility.
sharpe_ratio = returns / annualized_volatility

# Tracks the highest price reached up to each date.
peak = prices.cummax()
drawdown = (prices - peak) / peak
# The minimum drawdown represents the stock's largest decline from a previous peak.
max_drawdown = drawdown.min()

results = pd.DataFrame({
    "Price": current_price,
    "1Y Return (%)": returns * 100,
    "Volatility (%)": annualized_volatility * 100,
    "Sharpe Ratio": sharpe_ratio,
    "Max Drawdown (%)": max_drawdown * 100
})

print("\nStock Analysis")
print(results.round(2))