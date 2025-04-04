import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# === DATA LOADING ===

def load_stock_data(tickers, start="2020-01-01", end="2025-01-01"):
    """Loads stock closing price data from Yahoo Finance."""
    data = yf.download(tickers, start=start, end=end)["Close"]
    return data

# Input stock tickers to analyze
tickers = input("Input Tickers separated by commas: ")
# Split the input string into a list of tickers
try:
    tickers = [ticker.strip() for ticker in tickers.split(',')]  # Split and strip whitespace
except ValueError:
    print("Ошибка ввода тикеров!")
    exit()

data = load_stock_data(tickers)

# Data check
if data.isnull().values.any():
    print("Некоторые тикеры недоступны или содержат пропуски. Проверьте их:")
    print(data[data.isnull().any()])
    exit()

# === RETURN AND VOLATILITY CALCULATION ===

returns = data.pct_change().dropna()  # Stock returns
mean_returns = returns.mean() * 252  # Average annual return
cov_matrix = returns.cov() * 252  # Annual covariance matrix (risk/volatility)
std_deviation = returns.std() * np.sqrt(252)  # Annual standard deviation

# === OPTIMIZATION FUNCTIONS ===

def portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate=0.02):
    """Calculates the Sharpe Ratio (return / risk)"""
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk
    return -sharpe_ratio  # Negative because minimize() minimizes the function

# Constraints (sum of weights = 1)
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
# Ensure bounds are created for each ticker
bounds = tuple((0, 1) for _ in range(len(tickers)))  # Weights between 0-100%
# Ensure initial weights are created for each ticker
initial_weights = np.ones(len(tickers)) / len(tickers)  # Even distribution

# Portfolio optimization
opt_results = minimize(portfolio_performance, initial_weights, args=(mean_returns, cov_matrix),
                       method='SLSQP', bounds=bounds, constraints=constraints)

# Optimal weights
optimal_weights = opt_results.x
optimal_returns = np.dot(optimal_weights, mean_returns)
optimal_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(cov_matrix, optimal_weights)))
optimal_sharpe = (optimal_returns - 0.02) / optimal_risk

# === MINIMUM RISK PORTFOLIO ===

def min_volatility(weights, mean_returns, cov_matrix):
    """Calculates portfolio volatility"""
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

min_vol_results = minimize(min_volatility, initial_weights, args=(mean_returns, cov_matrix),
                           method='SLSQP', bounds=bounds, constraints=constraints)

min_vol_weights = min_vol_results.x
min_vol_risk = np.sqrt(np.dot(min_vol_weights.T, np.dot(cov_matrix, min_vol_weights)))
min_vol_return = np.dot(min_vol_weights, mean_returns)

# === EFFICIENT FRONTIER VISUALIZATION ===

def generate_efficient_frontier(mean_returns, cov_matrix, num_portfolios=5000, risk_free_rate=0.02):
    """Generates points on the efficient frontier"""
    results = np.zeros((3, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.dirichlet(np.ones(len(tickers)), size=1).flatten()
        weights_record.append(weights)

        portfolio_return = np.dot(weights, mean_returns)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

        results[0, i] = portfolio_return
        results[1, i] = portfolio_risk
        results[2, i] = sharpe_ratio

    return results, weights_record

# Generate random portfolios for efficient frontier
results, _ = generate_efficient_frontier(mean_returns, cov_matrix)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap="viridis", marker="o", alpha=0.5)
plt.colorbar(label="Sharpe Ratio")
plt.scatter(optimal_risk, optimal_returns, c="red", marker="*", s=200, label="Optimal Portfolio")
plt.scatter(min_vol_risk, min_vol_return, c="blue", marker="*", s=200, label="Minimum Risk Portfolio")
plt.xlabel("Risk (Standard Deviation)")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier")
plt.legend()
plt.grid(True)
plt.show()

# === RESULTS OUTPUT ===

def print_results(name, returns, risk, sharpe_ratio=None):
    print(f"\n{name} Portfolio:")
    print(f"  Expected Return: {returns:.2%}")
    print(f"  Expected Volatility (Risk): {risk:.2%}")
    if sharpe_ratio is not None:
        print(f"  Sharpe Ratio: {sharpe_ratio:.2f}")

# Output the average return and risk of assets
print("\nAverage returns and risks of assets:")
for ticker, ret, risk in zip(tickers, mean_returns, std_deviation):
    print(f"{ticker}: Return = {ret:.2%}, Risk = {risk:.2%}")

# Output optimal portfolio results
print_results("Optimal", optimal_returns, optimal_risk, optimal_sharpe)

# Output minimum volatility portfolio results
print_results("Minimum Volatility", min_vol_return, min_vol_risk)
