#this library is for making data structures that enable us to work with data
import pandas
#this library is used to perform linear regression
from sklearn import linear_model

#DataFrame object from csv file using pandas
#DataFrame is like a table
frame = pandas.read_csv("data.csv")

# inputs are two columns from DataFrame
# Two explanatory variables
inputs = frame[['Weight', 'Volume']]
# One response variable
outputs = frame['CO2']

#linear regression object
reg = linear_model.LinearRegression()
reg.fit(inputs, outputs)

#the predict function is called on the linear regression object
#prints a predicted emission value for a car with 2300 as weight and 1300 as volume
print(reg.predict([[2300, 1300], [2000, 1490]]))

#prints two values known as coefficients
#first value is the predicted increase of emission when weight increases by one unit
#second value is the predicted increase of emission when volume increases by one unit
print(reg.coef_)

#this is just a way to get the x coefficient and y coefficient separately
#uses indexes
xCoeff = reg.coef_[0]
yCoeff = reg.coef_[1]
print(str(xCoeff) + " " + str(yCoeff))

#gets the z intercept (when both x and y are zero)
#using z intercept and x and y coefficients, we can graph the best fit line
print(reg.intercept_)