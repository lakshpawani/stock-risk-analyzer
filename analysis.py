import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)

user_input = input("Enter stock tickers separated by spaces: ").upper()
tickers = user_input.split()  
risk_free_rate = float(input("Enter risk-free rate (%): ")) / 100
if not tickers:
    print("Please enter at least one ticker.")
    exit()
data = yf.download(tickers, period="1y", auto_adjust=True)

valid_tickers = data["Close"].dropna(axis=1, how="all").columns.tolist()
invalid_tickers = [ticker for ticker in tickers if ticker not in valid_tickers]
if invalid_tickers:
    print(f"Invalid tickers: {', '.join(invalid_tickers)}")
prices = data["Close"].dropna(axis=1, how="all").dropna()
if prices.empty:
    print("No valid stock tickers found.")
    exit()
current_price = prices.iloc[-1]
returns = (prices.iloc[-1] / prices.iloc[0]) - 1
daily_returns = prices.pct_change().dropna()
daily_volatility = daily_returns.std()
annualized_volatility = daily_volatility * np.sqrt(252)
sharpe_ratio = (returns - risk_free_rate) / annualized_volatility

peak = prices.cummax()
drawdown = (prices - peak) / peak
max_drawdown = drawdown.min()
normalized_prices = prices / prices.iloc[0] * 100
ax = normalized_prices.plot(figsize=(10, 6))
ax.set_title("Normalized Stock Performance")
ax.set_xlabel("Date")
ax.set_ylabel("Value (Start = 100)")
ax.grid(True)
ax.legend(title="Ticker")
plt.tight_layout()
plt.show()

results = pd.DataFrame({
    "Price": current_price,
    "1Y Return (%)": returns * 100,
    "Volatility (%)": annualized_volatility * 100,
    "Sharpe Ratio": sharpe_ratio,
    "Max Drawdown (%)": max_drawdown * 100
})

print("\nStock Analysis")
print(results.round(2))