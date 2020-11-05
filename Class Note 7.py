# SciPy and Pandas
# Use documentations to learn these two useful packages.
# SciPy: math functions
# Pandas: data analysis and manipulation (data visualization)

import pandas as pd

contestants = {'name': ['Mariam', 'Hashim', 'Ana', 'Ronan', 'Louisa', 'Benjamin'],
               'age': [51, 32, 33, 46, 29, 44],
               'city': ['Perth', 'Edinburgh', 'Glasgow', 'Inverness', 'Falkirk', 'Aberdeen'],
               'team': ['red', 'red', 'blue', 'red', 'blue', 'blue']}

# set the data frame
df = pd.DataFrame(contestants, index=[f'Contestant {i}' for i in range(1,7)])   # set the index
print(df)

# print the row
print(df['age'])   # use the key

# print specific elements
print(df.loc['Contestant 3', :])
print(df.loc['Contestant 3', 'age'])
# use the column number
print(df.iloc[2, 1])

# select required date
print(df['team'] == 'blue')
print(df.loc[df['team'] == 'blue', 'age'])   # print ages that satisfy team == blue
print(df.loc[df['team'] == 'blue', ['age', 'name']])   # print ages and names

