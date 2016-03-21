# Import modules
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
from collections import Counter

# Read CSV
df = pd.read_csv('faculty.csv')

# Clean up column names
df.columns = df.columns.str.strip()

# Q1 CODE

# Extract degrees as a series
s1 = pd.Series(df['degree'])

# Remove leading spaces
s1 = s1.str.lstrip()

# Fix ScD
s1 = s1.replace(to_replace='Sc(.*)D(.*)', value='ScD', regex=True)

# Fix PhD
s1 = s1.replace(to_replace='Ph(.*)D(.*)', value='PhD', regex=True)

# Fix BSEd
s1 = s1.replace(to_replace='B.S.Ed.', value='BSEd', regex=True)

# Fix MS
s1 = s1.replace(to_replace='M.S.', value='MS', regex=True) 

# Fix none
s1 = s1.replace(to_replace='0', value='None')

# Convert series to list
l = s1.tolist()

# Create new list, iterate over each element in nested list, split strings separated by ' ', and add strings to new list
l_split = []

for x in l:
    l_split.extend(x.split(' '))

# Total number of degrees
total_d = len(l_split) 

# Count frequency
count_d = Counter(l_split) 

# Number of types of degrees
num_deg = len(count_d)

# Q1 answer
print 40 * '*'
print 'The answer to question 1 is:'
print 'The total number of degrees is %s' % total_d
print 'There are %s types of degrees' % num_deg
print count_d

# Q2 CODE

# Extract titles as a series
s2 = pd.Series(df['title'])

# Remove leading spaces
s2 = s2.str.lstrip()

# Fix 'is' error
s2 = s2.replace(to_replace= 'is Bio', value='of Bio', regex=True)

# Convert series to list
l2 = s2.tolist()

# Total number of titles
total_t = len(l2)

# Count frequency
count_d2 = Counter(l2) 

# Number of types of titles
num_titles = len(count_d2)

# Q2 answer
print 40 * '*'
print 'The answers to question 2 are:'
print 'The total number of titles is %s' % total_t
print 'There are %s types of titles' % num_titles
print count_d2

# Q3 code

# Extract emails as a list
print 40 * '*'
l3 = df['email'].values.tolist()
print 'The answer to question 3 is below:'
print l3

# Q4 code

# Extract emails into a series
s4 = pd.Series(df['email'])

# Remove any leading or trailing spaces
s4 = s4.str.lstrip().str.rstrip()

# Remove text up to and including @

s4 = s4.replace(to_replace='(.*)@', value='', regex=True)

# Get unique domains
s4_uni = s4.unique().tolist()
# Convert back to data frame
s4 = s4.to_frame('email')

s4 = s4.groupby('email')
s4_hist = s4['email'].count()
s4_types = len(s4_hist)
# Number of unique domains
s4_uni_dom = len(s4)
print 40 * '*'
print 'The answers to question 4 are below:'
print 'There are %s unique domains and the list of them is below:\n%s' % (s4_uni_dom, s4_uni)

# Q5 code

# Extract emails into a csv file
print 40 * '*'
df['email'].to_csv('emails.csv',sep=',', index = False, encoding='utf-8')
print 'Answer printed to emails.csv'

# Q6 code

#df6 = df['name'].str.split().str[-1]
#df6.columns = ['foo', 'lname']

#df.append(df6['lname'])
#print df6
# Create series from name
#s6 = pd.Series(df['name'])

# Extract last names
#s6 = s6.str.rsplit(None, 1)[-1]
#print s6

#df['last_name'] = df['name'].replace(to_replace=' .$', value


# Create a dictionary with last name as key


