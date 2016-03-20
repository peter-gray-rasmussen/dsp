# Import modules
import pandas as pd
from pandas import DataFrame, read_csv

# Read CSV
df = pd.read_csv('football.csv', index_col = 'Team')

# Calculate goal difference and assign to new column
df['G-GA'] = abs(df['Goals'] - df['Goals Allowed'])

# Find team with minimum goal difference
diff_min = df['G-GA'].argmin()

# Print team with minimum goal difference
print "The team with the minimum goal difference is %s" % diff_min
