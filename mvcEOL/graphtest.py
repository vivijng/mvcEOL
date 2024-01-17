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

x = np.linspace(0, 1, 3)
# [0 .5 1]
# [0 .5 1]
y = np.linspace(0, 1, 2)
# [0, 0, 0]
# [1, 1, 1]

# inputs x and y are the same size - every x matches with every y
X, Y = np.meshgrid(x, y)
# (0, 1) (.5, 1) (1, 1)
# (0, 0) (.5, 0) (1, 0)

plt.scatter(X, Y)
plt.show()