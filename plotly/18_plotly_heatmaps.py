# heatmaps allow for the visualization of 3 features:
# 1) categorical or continuous variables on the x axis
# 2) categorical or continuous variables on the y axis
# 3) a third continuous feature displayed through color.
# the z variable (color) can not be a Pandas colums, and must be converted to 
# a list. Use .values.tolist()

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

# import data
df = pd.read_csv('data/2010SantaBarbaraCA.csv')

# investigate data
df.info()
df.columns

# create data and layout
data = [go.Heatmap(x=df['DAY'],
                   y=df['LST_TIME'],
                   z=df['T_HR_AVG'].values.tolist(),
                   colorscale = 'Jet')]

layout = go.Layout(title = 'SB CA Temps')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)


######
## graphing multiple plots (subplots)
######

# import data
df1 = pd.read_csv('data/2010SitkaAK.csv')
df2 = pd.read_csv('data/2010SantaBarbaraCA.csv')
df3 = pd.read_csv('data/2010YumaAZ.csv')

# create data and layout for the three data sets
trace1 = go.Heatmap(x=df1['DAY'],
                    y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'].values.tolist(),
                    zmin=5, zmax=40, # set min and max to keep color scales consistent between plots
                    colorscale = 'Jet')

trace2 = go.Heatmap(x=df2['DAY'],
                    y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'].values.tolist(),
                    zmin=5, zmax=40, # set min and max to keep color scales consistent between plots
                    colorscale = 'Jet')

trace3 = go.Heatmap(x=df3['DAY'],
                    y=df3['LST_TIME'],
                    z=df3['T_HR_AVG'].values.tolist(),
                    zmin=5, zmax=40, # set min and max to keep color scales consistent between plots
                    colorscale = 'Jet')

fig = tools.make_subplots(rows=1, cols=3,
                          subplot_titles=['Sitka, AK', 'SB, CA', 'Yuma, AZ'],
                          shared_yaxes=False) # False = different y axis 

fig.append_trace(trace1,1,1) # row 1, column 1
fig.append_trace(trace2,1,2) # row 1, column 2
fig.append_trace(trace3,1,3) # row 1, column 3

# add a title to the entire plot
fig['layout'].update(title='Temperature plots for 3 cities')

pyo.plot(fig)
