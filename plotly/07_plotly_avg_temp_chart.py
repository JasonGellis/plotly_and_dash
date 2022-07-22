# Objective: Develop a Line Chart that plots 7 days worth of temperature data
# on one graph.

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# import data
df = pd.read_csv('data/2010YumaAZ.csv')

# create list of days for plot. These are in all caps, because they are in all 
# caps in the data set. The labeling must be the same.
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# create a for loop
data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY']==day]['T_HR_AVG'],
                       mode='lines',
                       name=day) # sets the name of each trace to a day in the list
    data.append(trace)
    
# use list comprehension to create traces
data2 = [go.Scatter(x=df['LST_TIME'],
                    y=df[df['DAY']==day]['T_HR_AVG'],
                    mode='lines',
                    name=day) for day in days]

# list comprehension that doesn't require the days variable
data3 = [{
    'x':df['LST_TIME'],
    'y':df[df['DAY']==day]['T_HR_AVG'],
    'name':day} for day in df['DAY'].unique()] # inclusion of df['DAY'].unique() means no days variable is needed.

# setup data and layout
layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# create the figure
fig = go.Figure(data=data2, layout=layout)
pyo.plot(fig, filename='avg_temps.html')
