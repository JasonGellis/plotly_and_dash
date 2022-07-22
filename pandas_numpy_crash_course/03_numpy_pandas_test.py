# review exercise

# Task1: Import pandas and numpy
import pandas as pd
import numpy as np

# Task 2: set numpy's random seed generator to 101
np.random.seed(101)

# Task 3: create a numpy matrix of 100 rows, 5 colums, and random ints from 1 -100
mat = np.random.randint(1,101, (100,5))

# Task 4: read this numpy matrix into a pandas data frame
pd.DataFrame(mat)

# Task 5: rename the colums to f1, f2, f3, f4, label
pd.DataFrame(data = mat, columns = ['f1', 'f2', 'f3', 'f4', 'label'])
# or
mat.colums = ['f1', 'f2', 'f3', 'f4', 'label']

# Task 6: create a data frame with columns A, B, C, D. Each columns should have
# 50 rows of randon numbers between 0 and 100

mat = np.random.randint(0,100, (50,4))
pd.DataFrame(data = mat, columns = ['A', 'B', 'C', 'D'])
