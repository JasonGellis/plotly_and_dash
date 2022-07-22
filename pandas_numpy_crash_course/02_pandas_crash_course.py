# plotly and dash crash course in pandas

import pandas as pd
import numpy as np

# create the dataset
salaries = pd.DataFrame({'Name':['John', 'Sally', 'Alyssa'],
                         'Salary':[50000,120000,80000],
                         'Age':[34,45,27]})

salaries

# select only the salary column
salaries['Salary']

# pass a list for multiple columns
salaries[['Salary', 'Name']]

# use min, max, and mean for columns
salaries['Salary'].min()
salaries['Salary'].max()
salaries['Salary'].mean()

# conditional filtering
salaries['Age'] > 30 # returns the boolean values
salaries[salaries['Age'] > 30] # apply the boolean to filter the data set

# get unique values
salaries['Age'].unique()

# get number of unique values
salaries['Age'].nunique()

# descriptives
salaries.columns # columns names
salaries.describe() # stats summaries
salaries.info() # data frame information
salaries.index # range index

# combine numpy and pandas

# create an array in numpy
mat = np.arange(0,25).reshape(5,5)
mat
type(mat)

# use pandas to convert the numpy array into a pandas dataframe
df = pd.DataFrame(data = mat)
df
type(df)

# rename columns using the column argument
df = pd.DataFrame(data = mat, columns = ['A', 'B', 'C', 'D', 'E'])
df
