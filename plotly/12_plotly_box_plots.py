# box plots visualize variation of a (continuous numerical) feature 
# through quartiles. Good for data distributions.
# in plotyle - midlle line = median, between q1 and q3 = 50% of data (iqr).
# outliers are 1.5 times the iqr, or greater than (q3-q1) * 1.5
# box plots can be used to compare the distributions of multiple samples 

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

# create data 
data = [go.Box(y=y,
               boxpoints='all', # switch to 'outliers to show only outliers
               jitter=0.3,
               pointpos=0)] # pointpos determines how points are overlayed
pyo.plot(data)

# compare the word frequency of Twain and Snodgrass
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

# create two boxplots
data2 = [go.Box(y=snodgrass, name='Snodgrass'),
         go.Box(y=twain, name='Twain')]

pyo.plot(data2)