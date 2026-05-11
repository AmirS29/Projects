# Quantitative Portfolio Optimization 

## 📌 Objective
A data-driven financial modeling tool that applies Modern Portfolio Theory (MPT) to optimize asset allocation across equities, commodities, and real estate. The engine calculates the Efficient Frontier, identifies optimal risk-reward portfolios, backtests historical performance, and exports structured KPIs to feed a downstream Business Intelligence (BI) dashboard.

## 🛠️ Tech Stack & Architecture
* **Language:** Python
* **Data Ingestion:** `yfinance` (Yahoo Finance API)
* **Quantitative Optimization:** `scipy.optimize` (SLSQP solver), `numpy`, `pandas`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Target Output:** Structured `.csv` datasets for Tableau/PowerBI integration

## 🔄 Methodology & Workflow

### 1. Data Ingestion & Risk-Return Profiling
* Extracts 5 years of daily historical closing prices for a diversified basket of assets (e.g., AAPL, MSFT, AMZN, JNJ, XOM, TLT, GLD, VNQ).
* Computes daily percentage changes, annualized mean returns, and the annualized covariance matrix to quantify asset correlation and historical risk.

### 2. Portfolio Optimization Engine
* **Minimum Variance Portfolio (MVP):** Utilizes the `scipy.optimize.minimize` function with bounds and constraints to find the specific asset weighting that minimizes overall portfolio volatility.
* **Maximum Sharpe Ratio Portfolio (Tangency Portfolio):** Optimizes asset weights to maximize the risk-adjusted return relative to the risk-free rate (based on current U.S. Treasury yields), plotting the Capital Market Line (CML).

### 3. Efficient Frontier Generation
* Iteratively minimizes variance across an array of target returns to map the Markowitz Bullet.
* Visualizes the risk-return tradeoff, plotting the efficient frontier, CML, and key optimal portfolios (MVP and Max Sharpe) on a single interactive plot.

### 4. Historical Backtesting
* Simulates the performance of the optimized portfolio weights over the 5-year historical window.
* Calculates core financial KPIs including **Cumulative Returns, Annualized Volatility, Sharpe Ratio, and Maximum Drawdown**.

### 5. Data Export (ETL for Dashboarding)
* Automatically structures and exports 7 distinct datasets (`returns.csv`, `weights.csv`, `efficient_frontier.csv`, `kpi_summary.csv`, etc.) to power a front-end BI dashboard for stakeholder presentation.

## 🚀 How to Run Locally

**1. Set up the Environment**
Ensure you have Python installed and create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy pandas scipy matplotlib seaborn yfinance
