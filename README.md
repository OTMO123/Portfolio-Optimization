
# Portfolio Optimization with Python

This project demonstrates portfolio optimization techniques using Python. It utilizes financial data from Yahoo Finance to calculate the expected returns, risk (volatility), and Sharpe ratio of a portfolio, along with methods for portfolio optimization.

The goal of this project is to help investors create an optimal investment portfolio by applying modern portfolio theory, which aims to maximize returns for a given level of risk.

## Project Overview

The code applies various financial calculations, including:
- Calculating stock returns and volatility
- Optimizing portfolios using the Sharpe ratio
- Creating a Minimum Risk Portfolio
- Visualizing the Efficient Frontier (a graph showing the best risk-return trade-offs)

The project is designed to:
1. Download stock data for multiple tickers from Yahoo Finance.
2. Calculate annual returns, risk (standard deviation), and covariance.
3. Use optimization techniques to determine the optimal portfolio weights and the minimum risk portfolio.
4. Visualize the efficient frontier of various portfolio allocations.
5. Output the results of the portfolio analysis, including the expected return, volatility, and Sharpe ratio.

## Features

- **Stock Data Loading**: Automatically download stock price data from Yahoo Finance using the `yfinance` library.
- **Return and Volatility Calculation**: Calculates annualized returns, risk (standard deviation), and covariance matrix based on historical data.
- **Portfolio Optimization**: Optimizes portfolios using the Sharpe ratio to find the optimal portfolio allocation.
- **Minimum Risk Portfolio**: Finds the portfolio with the least volatility.
- **Efficient Frontier**: Generates a graph of the efficient frontier, helping visualize risk-return trade-offs.
- **Interactive**: The code prompts the user for stock tickers, making it flexible for different asset classes.

## Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `yfinance`
  - `matplotlib`
  - `scipy`

You can install the necessary libraries with `pip`:
```bash
pip install numpy pandas yfinance matplotlib scipy
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/OTMO123/Portfolio-Optimization.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Portfolio-Optimization
   ```

3. Run the script:
   ```bash
   python portfolio_optimization.py
   ```

4. Enter the stock tickers you want to analyze when prompted. For example:
   ```text
   Input Tickers separated by commas: AAPL, MSFT, TSLA, AMZN
   ```

5. The script will output the average returns, risks, and optimal portfolio details, including:
   - Expected return and volatility for the optimal portfolio
   - Sharpe ratio for the optimal portfolio
   - Minimum risk portfolio details
   - A graph of the efficient frontier with optimal portfolio points

## Example Output

```
Average returns and risks of assets:
AAPL: Return = 22.57%, Risk = 29.81%
MSFT: Return = 18.45%, Risk = 25.12%
TSLA: Return = 44.32%, Risk = 54.23%
AMZN: Return = 19.87%, Risk = 28.67%

Optimal Portfolio:
  Expected Return: 23.67%
  Expected Volatility (Risk): 22.34%
  Sharpe Ratio: 1.34

Minimum Volatility Portfolio:
  Expected Return: 16.12%
  Expected Volatility (Risk): 18.25%
```

## Efficient Frontier Visualization

The efficient frontier will be visualized in a plot with the following:
- The red point represents the optimal portfolio.
- The blue point represents the minimum volatility portfolio.
- A color gradient shows the Sharpe ratio across different portfolios.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The code leverages `yfinance` for stock data, `scipy` for optimization, and `matplotlib` for data visualization.
- This project uses principles from **Modern Portfolio Theory** (MPT) developed by Harry Markowitz.
