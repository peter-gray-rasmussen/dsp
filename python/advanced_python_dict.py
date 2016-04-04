# Q6 code
# Dict with last name as key and degrees, titles, and emails as values

# Import modules
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
from collections import Counter
import re
from collections import defaultdict
import csv

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
print '*' * 20
# Question 7: key is a tuple with first and last name

faculty_dict = defaultdict(list)
professor_dict = defaultdict(list)

with open('faculty.csv','r') as f:
  reader = csv.reader(f)
  reader.next() # skip header row
  for row in reader:
    name = row[0]
    match = re.search(r'(.*)\s([\w.-]+)$',name)
    first = match.group(1)
    last = match.group(2)

    degree = row[1]

    title = row[2]
    proper_title = re.search(r'[\w\s]*Professor',title).group()

    email = row[3]

    faculty_dict[last].append([degree, proper_title, email])
    professor_dict[(first, last)] = [degree, proper_title, email]
print professor_dict

print '*' * 20
# Q8

# print by last name order
sorted_keys = sorted(professor_dict.keys(), key = lambda x:x[-1])
for key in sorted_keys:
  print key, professor_dict[key]

