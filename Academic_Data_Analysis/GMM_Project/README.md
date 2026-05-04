# Gaussian Mixture Models (GMM) & PCA: Clustering and Generative Modeling

## 📌 Objective
This project explores the application of Gaussian Mixture Models (GMM) for unsupervised clustering, semi-supervised classification, and generative sampling. The analysis spans both synthetic, non-linear datasets (Two-Moons) and high-dimensional real-world image data (MNIST Digits).

## 🛠️ Tech Stack & Methodologies
* **Language:** Python
* **Libraries:** `scikit-learn`, `numpy`, `scipy`, `matplotlib`
* **Core Algorithms:** Gaussian Mixture Models (GMM), Principal Component Analysis (PCA), Gradient Boosting Classifier
* **Statistical Metrics:** Bayesian Information Criterion (BIC), Log-Likelihood, Component Covariance Analysis

## 🔄 Project Workflow & Architecture

### Part 1: Non-Linear Density Estimation (Two Moons)
* **Objective:** Fit a probability distribution to a highly non-linear dataset.
* **Optimization:** Engineered a GridSearchCV pipeline to determine the optimal number of GMM components and covariance type by minimizing the Bayesian Information Criterion (BIC).
* **Visualization:** Mapped the probability density function (PDF) of the fitted model, plotting custom contour level sets to visualize the multivariate normal distributions of each component.

### Part 2: Semi-Supervised Classification & Generative Sampling
* **Classification:** Mapped continuous GMM components to discrete binary classes using majority-rule probabilities ($P(X|Y)$).
* **Model Validation:** Split data into training/testing sets, evaluating component models to minimize classification test error.
* **Generative Sampling:** Utilized the optimized GMM weights, means, and covariance matrices to act as a generative model, successfully sampling and plotting new, synthetic data points that follow the original non-linear distribution.

### Part 3: High-Dimensional Image Generation (MNIST)
* **Dimensionality Reduction:** Applied Principal Component Analysis (PCA) to the MNIST digits dataset, retaining 46 components to capture the vast majority of the cumulative explained variance while heavily reducing computational load.
* **Unsupervised Clustering:** Trained a GMM on the PCA-transformed data without labels, analyzing the BIC against a supervised counterpart.
* **Latent Space Visualization:** Associated GMM components with digit classes and performed inverse PCA transformations to successfully visualize the "mean" generated image for each digit class.
* **Synthetic Image Generation:** Sampled the latent space of the unsupervised GMM to generate brand-new, synthetic handwritten digits.
* **Benchmarking:** Trained a Gradient Boosting Classifier on the PCA-reduced feature set to benchmark baseline predictive accuracy.

## 🚀 Key Takeaways
This project demonstrates the flexibility of GMMs not just as a clustering algorithm, but as a powerful **generative statistical model**. By combining GMMs with PCA, the model successfully learns the underlying distribution of complex, high-dimensional datasets well enough to generate statistically sound synthetic representations.
