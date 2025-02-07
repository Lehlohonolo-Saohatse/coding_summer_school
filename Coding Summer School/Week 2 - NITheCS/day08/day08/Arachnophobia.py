# CHPC Summer School 2025
# Probability & Statistics: Numerical Data & Regression
# Example: Arachnophobia

#%%
# Import packages and functions

import numpy as np
from sklearn.linear_model import LinearRegression

#%%
# Give the values for x and for y			

x = np.array([3, 4.3, 9.2, 7.6, 13, 6.4, 9.9, 3.3, 5.6, 12, 10.4, 13.9, 5.9, 4.7, 9.5, 11.3, 15, 11.9, 10.7, 6.5, 5.3, 11.6, 14.8, 8.9])
y = np.array([15, 20, 30, 25, 35, 18, 40, 10, 11, 28, 26, 36, 27, 17, 34, 41, 50, 43, 37, 21, 14, 38, 45, 24])

#%%
# Calculate the correlation coefficient between x and y

np.corrcoef(x, y)

#%%
# Reshape x to have one column (and 24 rows)

x = x.reshape((-1, 1))

#%%
# Fit the regression model

lrm = LinearRegression().fit(x, y)
lrm.intercept_
lrm.coef_

#%%
# Determine the predicted values of y

y_pred = lrm.predict(x)

# Calculate the residuals

e = y - y_pred

#%%
# Calculate R_square

r_sq = lrm.score(x, y)