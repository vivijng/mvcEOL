#this library is for making data structures that enable us to work with data
import pandas
#this library is used to perform linear regression
from sklearn import linear_model
#this library allows us to standardize data (not work with raw values)
from sklearn.preprocessing import StandardScaler

#creates an object that can perform the standardizing process
scale = StandardScaler()

#DataFrame object from csv file using pandas
#DataFrame is like a table
frame = pandas.read_csv("data.csv")

# inputs are two columns from DataFrame
# Two explanatory variables
inputs = frame[['Weight', 'Volume']]
# One response variable
outputs = frame['CO2']

# to standardize data subtract mean of the variable from observed value of that variable
# then divide by standard deviation
# z scores are useful when seeing how far a value is from the mean of its own distribution
scaledInputs = scale.fit_transform(inputs)

#linear regression object
reg = linear_model.LinearRegression()
#now the inputs are the scaled versions!!!
reg.fit(scaledInputs, outputs)

# now the data is trained on scaled values
# when we want to predict an output given raw data we must standardize that data
# the transform function takes in 2d array as parameter since one output has two input variables
# those two input variables get scaled relative to their category
scaled = scale.transform([[2300, 1300]])
print([scaled[0]])

# getting the first row of the 2d array produced with the transform call since we only transformed one set of inputs
# same answer as prediction with raw values
print(reg.predict([scaled[0]]))