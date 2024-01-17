#this library creates graphs
import matplotlib.pyplot as plt
#this library creates 3d graphs
from mpl_toolkits.mplot3d import Axes3D
#this library is for making data structures that enable us to work with data
import pandas
#this library is used to perform linear regression
from sklearn import linear_model
#works wtih arrays
import numpy as np

#creates a figure
fig = plt.figure()
#111 specifies that this plot is the only plot in the figure
#projection specifies that 3 axes should be viewable
ax = fig.add_subplot(111, projection='3d')

#DataFrame object from csv file using pandas
#DataFrame is like a table
frame = pandas.read_csv("data.csv")

#x and y are the independent/explanatory variables
xs = frame['Weight']
ys = frame['Volume']
#a meshgrid produces two 2d arrays for x and y points
#the grids line up and are the same size
# so each x is paired with the y at the same index of the y 2D array
x, y = np.meshgrid(xs, ys)

#2D array of weight and volume (both inputs)
inputs = frame[['Weight', 'Volume']]

# One response variable
outputs = frame['CO2']

#linear regression object
reg = linear_model.LinearRegression()
reg.fit(inputs, outputs)

#first coefficient (what happens to CO2 when weight increases by 1 unit)
xCoeff = reg.coef_[0]
#second coefficient (what happens to CO2 when volume increases by 1 unit)
yCoeff = reg.coef_[1]
#z intercept (supposed CO2 value when x and y are 0)
intercept = reg.intercept_

#using the data that LinearRegression gives us
#equation to model x y and z
z = (xCoeff * x) + (yCoeff * y) + intercept

#labeling axes
ax.set_xlabel("Weight")
ax.set_ylabel("Volume")
ax.set_zlabel("CO2")

#original data
ax.scatter(xs, ys, outputs)

#best fit plane for data
#in 3d work with planes not lines
ax.plot_surface(x, y, z, color='red')

plt.show()