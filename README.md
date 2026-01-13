# ✈️ Data Analysis Project: Airline Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Finished-success)
![Data Science](https://img.shields.io/badge/Area-Data%20Science-orange)

## 📋 Project Description
This project involves a comprehensive statistical analysis and predictive modeling of pricing behaviors in the air travel industry. Using **Multiple Linear Regression** techniques in Python, key variables determining ticket costs were identified, and rigorous statistical assumptions were validated.

The primary objective was to build a mathematical model capable of predicting sales prices and understanding consumer behavior.

## 🛠️ Technologies Used
* **Python**: Main programming language.
* **Pandas & NumPy**: Data manipulation and cleaning.
* **Statsmodels**: Statistical modeling and hypothesis testing (OLS).
* **Matplotlib & Seaborn**: Data visualization and residual diagnostics.

---

## 📊 Key Findings: Market Behavior
After performing a descriptive analysis of the data, 5 fundamental patterns were detected:

1.  **Premium Market Dominance:** **50% of the analyzed bookings** correspond to *First Class*, indicating a sample with a high willingness to pay.
2.  **High Price Variability:** The average price is **$376 USD**, with a range oscillating between $300 and $620 depending on purchase conditions.
3.  **Purchase Window:** Users purchase tickets with an average of **45 days in advance** (range: 8 to 123 days).
4.  **Market Share:** **American Airlines** leads traveler preference (30.6%), followed by Southwest and United.
5.  **Traveler Profile:** 43.5% of users are "Casual" travelers, while frequent flyers represent a minority.

---

## 📈 Methodology & Modeling

### 1. Multicollinearity Analysis (VIF)
Redundancy between variables was evaluated using the *Variance Inflation Factor*.
* **Alert:** Severe multicollinearity was detected in the `Trips` variable (VIF > 14), suggesting it is highly correlated with the traveler type.

### 2. Mathematical Model Equation
The generated model explains **63.9% ($R^2$)** of the variation in prices. The resulting equation is:

$$
Price = 239.72 + 167.77(AA) + 143.81(Delta) + 176.75(United) - 0.40(Days) + 84.35(FirstClass) - 33.69(Business)
$$

**Interpretation:**
* **Airlines:** Flying with United or AA significantly increases the base price.
* **Advance Purchase:** There is a saving of **$0.40 USD** for every extra day of advance purchase.
* **Class:** Flying *First Class* increases the cost by an average of **$84.35 USD**.

---

## 🧪 Statistical Assumption Validation

To ensure model robustness, visual and numerical diagnostic tests were performed:

### A. Normality of Errors
> **Shapiro-Wilk Test:** p-value = 0.389 (Normality Accepted).

The histogram and Q-Q plot confirm that the residuals follow a normal distribution, validating the model's hypothesis tests.

![Normality Plot](path/to/your/histogram_qq_image.png)
*(Make sure to upload your image and place the correct path here)*

### B. Homoscedasticity (Constant Variance)
> **Breusch-Pagan Test:** p-value < 0.05 (Heteroscedasticity Exists).

A slight "funnel" shape is observed in higher prices. This indicates that the model is highly accurate for standard fares but has a larger margin of error for very expensive tickets.

![Residuals Plot](path/to/your/residuals_image.png)

---


