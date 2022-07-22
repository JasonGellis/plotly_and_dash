# distribution plots - typically three plots on top of one another
# 1) a histogram
# 2) a rug plot
# 3) a kernel density estimate (kde)

# import libraries
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

# create data
x = np.random.randn(1000)

hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig)

######
## multiple groups
######

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1, x2, x3, x4]
group_labels = ['x1','x2', 'x3', 'x4']

fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[.2, .1, .3, .4]) # create a list for each hostogram
pyo.plot(fig)

######
## Real world example
######

# compare the word frequency of Twain and Snodgrass
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass, twain]
group_labels = ['Snodgrass','Twain']

fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[0.005, 0.005]) 
pyo.plot(fig)
