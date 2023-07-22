# -*- coding: utf-8 -*-
"""Random Forest Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14DhN_3rGEoer7YpiopSFTxK3AHHuXP-A

# Random Forest Regression

## Importing Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing Data Set"""

dataset = pd.read_csv('/content/ Data Random Forest Regre.csv')
X = dataset.iloc[:, 1:-1].values #indexes values in a dataframe
y = dataset.iloc[:, -1].values

print(X)
print(y)

"""## Training the dataset"""

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 12, random_state = 42 )
regressor.fit(X, y)

"""## Predicting a new result"""

regressor.predict([[5.5]])

"""## Visualising the Random Forest Regression"""

X_grid = np.arange(min(X), max(X), 0.01) #smoothing the graph w inc of 0.01
X_grid = X_grid.reshape((len(X_grid), 1)) #rehsaping
plt.scatter(X, y, color = 'red') #we get continous values
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('Grade')
plt.ylabel('Salary')
plt.show()