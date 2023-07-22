# -*- coding: utf-8 -*-
"""Polynomial Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D51xAcBwXygH2bgHG_yAzd6ifjIqaHN7

# Polynomial Regression

## Importing Libraries
"""

import numpy as py
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing Data Set"""

data_set = pd.read_csv("/content/RBC in Humans.csv")
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, -1].values

"""## Training the Linear Regression model on the whole dataset"""

from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()
linear_reg.fit(X, y)

"""## Training the Polynomial Regression model on the whole dataset

we put polynomial into degree format so it eventually comes out in linear regression together
"""

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
polynomial_reg = PolynomialFeatures(degree = 6)
X_poly = polynomial_reg.fit_transform(X) #converted into degree based feature using polynimial Features

linear_reg_2 = LinearRegression()
linear_reg_2.fit(X_poly, y)

"""## Visualising the Linear Regression results"""

plt.scatter(X, y, color = "red")
plt.plot(X, linear_reg.predict(X), color = 'blue')
plt.title("RBS linear Regression")
plt.xlabel('Age')
plt.ylabel('RBC')
plt.show

"""huge difference in results

## Visualising the Polynomial Regression results (for higher resolution and smoother curve)
"""

X_grid = py.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = "red")
plt.plot(X, linear_reg_2.predict(X_poly), color = 'blue')
plt.title("RBS Polynomial linear Regression")
plt.xlabel('Age')
plt.ylabel('RBC')
plt.show

"""very smooth and curvy and is nearby to all the points

## Predicting a new result with Linear Regression
"""

linear_reg.predict([[6.5]])

"""## Predicting a new result with Polynomial Regression

"""

linear_reg_2.predict(polynomial_reg.fit_transform([[6.5]]))