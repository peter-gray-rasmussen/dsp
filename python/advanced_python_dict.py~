# Q6 code
# Dict with last name as key and degrees, titles, and emails as values

# Import modules
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
from collections import Counter

# Question 6

# Read CSV
df6 = pd.read_csv('faculty.csv')

# Clean up column names
df6.columns = df6.columns.str.strip()

# Extract last names from name column
df6['name'] = df6['name'].str.split().str[-1]

# Dataframe to dict
faculty_dict = df6.set_index('name').T.to_dict('list')

# Three keys: Putt, Feng, and Bilker
name_1 = faculty_dict['Putt']
name_2 = faculty_dict['Li']
name_3 = faculty_dict['Bilker']

# Print answers
print 'Putt: %s' % name_1
print 'Li: %s' % name_2
print 'Bilker: %s' % name_3

print type(name_1)

# Question 7: key is a tuple with first and last name

# Read CSV
df7 = pd.read_csv('faculty.csv')

# Clean up column names
df7.columns = df7.columns.str.strip()

# Extract first names
for i in range(len(df7)['name']):
    x=df7['name'][i].split(' ')
    t=(x[0], x[-1])
    df7['name'][i]=t



#df7['fnames'] = df7['name'].str.rsplit(' ', 1)[0]

#test = 'Python: I fucking love this shit'
#new = test.rsplit(' ', 1)[0]

#print new

