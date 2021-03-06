# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset

dataset = pd.read_csv("Salary_Data.csv")

x = dataset.iloc[:,:-1].values
y = dataset.iloc[: ,1].values

#from sklearn.cross_validation import train_test_split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 1/3, random_state= 0)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_train, y_train, color = 'red')

#plt.plot(x_train, y_train, color = 'blue')

plt.plot(x_train,regressor.predict(x_train) , color = 'blue')

plt.title('Salary Versus Experience(Training-Set) ')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')