# distribution plot exercise

# use the iris dataset to create a distplot that compares the petal lengths
# of each class.

# import libraries
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# import data
df = pd.read_csv('data/iris.csv')

# investigate data
df.info()
df.columns
#['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

setosa = df[df['class']=='Iris-setosa']['petal_length']
versicolor = df[df['class']=='Iris-versicolor']['petal_length']
virginica = df[df['class']=='Iris-virginica']['petal_length']

hist_data = [setosa, versicolor, virginica]
group_labels = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

fig = ff.create_distplot(hist_data, group_labels,
                         bin_size=[.05, .05, .05]) 
pyo.plot(fig)
