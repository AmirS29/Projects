# Quantitative Finance & Statistical Data Analysis Projects

## 📌 Overview
This repository contains a collection of academic projects focused on quantitative finance, stochastic modeling, and advanced statistical analysis. These projects were completed collaboratively and leverage **Python, C++, and C** to solve complex financial engineering problems, ranging from derivative pricing and portfolio optimization to volatility estimation and probabilistic forecasting.

## 🛠️ Core Competencies Demonstrated
* **Stochastic Modeling:** Monte Carlo Simulations, Geometric Brownian Motion (GBM), Markov Chains, Gaussian Copulas.
* **Quantitative Finance:** Option Pricing (European, Look-back, Shout), Credit Default Swaps (CDS), Interest Rate Derivatives.
* **Statistical Analysis:** Principal Component Analysis (PCA), Hidden Markov Models (HMM), Bayesian Updating, Maximum Likelihood Estimation (MLE).
* **Optimization & Algorithms:** Metropolis Algorithm, Variance Reduction (Antithetic/Control Variates), Random Number Generator (RNG) validation.

---

## 📁 Project Summaries

### 1. Statistical Validation of Random Number Generators (RNGs)
* **Objective:** Rigorously tested the uniformity and statistical independence of popular RNG algorithms (Mersenne Twister, MWC, and Knuth's 64-bit LCG) in two- and three-dimensional spaces.
* **Techniques:** Validated performance using bin-distribution analysis and standard normal distribution mapping to ensure mathematical reliability for high-dimensional Monte Carlo simulations.

### 2. Stochastic Simulation & Credit Risk Modeling
* **Objective:** Applied uniform random sampling to generate structured randomness for distribution sampling and financial risk assessment.
* **Techniques:** Utilized Accept/Reject and Inverse Transform methods for spatial sampling. Simulated a homogeneous Markov Chain to track corporate credit rating transitions over a 10-year period, ultimately calculating the fair annual premium for a Credit Default Swap (CDS) using a 5% discount rate.

### 3. Monte Carlo Variance Reduction for Option Pricing
* **Objective:** Priced complex derivatives while reducing the computational expense and high variance inherent in standard Monte Carlo simulations.
* **Techniques:** Implemented **antithetic variables** and **control variables** to stabilize estimators. Priced European, Look-back, and Shout options using Geometric Brownian Motion, benchmarking results against closed-form Black-Scholes solutions to prove convergence efficiency.

### 4. Gaussian Copulas & Electoral Forecasting
* **Objective:** Investigated the failures of probabilistic forecasting models (specifically FiveThirtyEight's 2016 election model) by challenging the assumption of independent state-level outcomes.
* **Techniques:** Built a Monte Carlo simulation utilizing a Gaussian Copula model to introduce state-to-state correlation. Calibrated the $\rho$ parameter using Maximum Likelihood Estimation (MLE) to assess the true role of dependence in electoral outcomes.

### 5. Principal Component Analysis (PCA) on the DJIA
* **Objective:** Identified the dominant, latent macroeconomic factors driving the daily price movements of the 30 Dow Jones Industrial Average (DJIA) components throughout 2020.
* **Techniques:** Computed covariance and correlation matrices to extract eigenvalues and eigenvectors. Analyzed the first principal component's relationship with CAPM betas to interpret market-wide and sector-specific risk factors.

### 6. Portfolio Optimization via the Metropolis Algorithm
* **Objective:** Minimized portfolio variance for the 30 DJIA stocks under strict allocation constraints.
* **Techniques:** Deployed the Metropolis algorithm (simulated annealing) to probabilisticly search for low-energy (low variance) portfolio states, using empirical covariance matrices to escape local minima and find optimal asset allocations.

### 7. Option Pricing under GARCH(1,1) Volatility
* **Objective:** Priced European call options on ExxonMobil (XOM) by modeling time-varying, clustered market volatility, moving beyond flat Black-Scholes assumptions.
* **Techniques:** Simulated stock paths updating daily variance via $\sigma_t^2 = \alpha \sigma_{\text{LT}}^2 + \beta R_{t-1}^2 + \gamma \sigma_{t-1}^2$. Computed implied volatilities across various strikes and visualized the resulting volatility smile/skew under different GARCH parameter sets.

### 8. Hidden Markov Chain (HMC) Volatility Estimation
* **Objective:** Estimated the historical daily volatility of ExxonMobil over a ten-year period by treating true volatility as an unobservable random walk.
* **Techniques:** Utilized recursive Bayesian updating to compute the posterior distribution of hidden states. Extracted the Maximum a Posteriori (MAP) estimate to infer volatility, benchmarking the HMC model's performance against standard EWMA models.

### 9. Recursive Valuation of Structured Interest Rate Derivatives
* **Objective:** Developed computationally efficient valuation models for highly sensitive structured products (the "Funky Collar" and "Funky Put") based on U.S. Treasury par curves.
* **Techniques:** Utilized a Nelson-Siegel yield curve fit and recursive programming in C++ (`Collar-Rec.cpp`, `Put-Rec.cpp`) to compute fair values and optimal stopping times for American-style exercise constraints.
