import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
from sklearn import linear_model
import numpy as np

#-2 to 2 with 5 values
# -2 -1 0 1 2
x = np.linspace(-2,2,5)

#-1 to 1 with 3 values
# -1 0 -1
y = np.linspace(-1,1,3)

# x by y
# (-2, 1) (-1, 1) (-1, 1) (-1, 1) (-1, 1) 
# (-2, 0) (-1, 0) (-1, 0) (-1, 0) (-1, 0) 
# (-2, -1) (-1, -1) (0, -1) (1, -1) (2, -1) 
X, Y = np.meshgrid(x, y)

plt.scatter(X, Y)
plt.show()