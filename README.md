# Stock Risk Analyzer

A simple Python program that analyzes stocks using one year of historical market data.

## Features

The program calculates:

- Current Price
- 1-Year Return
- Annualized Volatility
- Sharpe Ratio
- Maximum Drawdown

Users can enter any number of stock tickers.

## Requirements

- Python 3
- yfinance
- pandas
- numpy

## Installation

Install the required packages:

    pip install -r requirements.txt

## Usage

Run the program:

    python analysis.py

Enter stock tickers separated by spaces:

    Enter stock tickers separated by spaces: AAPL NVDA META
    Enter risk-free rate (%): 6.5

For NSE stocks, use the `.NS` suffix:

    Enter stock tickers separated by spaces: RELIANCE.NS TCS.NS HDFCBANK.NS

## Metrics

### Current Price

The latest available price for each stock.

### 1-Year Return

The percentage change in the stock's price over the analyzed period.

### Volatility

Measures how much the stock's daily returns fluctuate. Higher volatility means greater price variability.

### Sharpe Ratio

Measures return relative to volatility after accounting for the risk-free rate entered by the user.

### Maximum Drawdown

The largest decline from a previous peak during the analyzed period.

## Data

Stock data is obtained from Yahoo Finance through the `yfinance` library.

## Limitations

- Uses approximately one year of historical data.
- Sharpe Ratio uses a simplified calculation based on the user-providid risk-free rate.
- Historical performance does not guarantee future results.