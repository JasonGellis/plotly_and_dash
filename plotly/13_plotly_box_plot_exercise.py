# make a dataframe from the abalone dataset.
# Take two independent randon samples of different sizes from the rings field
# using np.random.choice. Example: np.random.choice(df['rings'], 10, replace = False)
# takes 10 random values.
# use box plots to show that the samples do derive from the same population.

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# import data
df = pd.read_csv('data/abalone.csv')

# inspect the data
df.info()
df.columns

setA = np.random.choice(df['rings'], 350, replace = False)
setB = np.random.choice(df['rings'], 270, replace = False)

# create box plots

data = [go.Box(y=setA, name= 'Random sample A'),
        go.Box(y=setB, name= 'Random sample B')]

pyo.plot(data)
