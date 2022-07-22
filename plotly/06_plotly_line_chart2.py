import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2017-alldata.csv')
df.head()

# filter out New England
df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True) # sets a specified column as an index, inplace sets for that specific df

# select only population columns (they start with POP)
list_of_populations = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_populations]

# use list comprehension to build traces for line chart
data = [go.Scatter(x=df2.columns,
                   y=df2.loc[state_name],
                   mode='lines',
                   name=state_name) for state_name in df2.index] # for every name in the df2 index

pyo.plot(data)
