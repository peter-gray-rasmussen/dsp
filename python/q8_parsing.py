import csv
from pandas import DataFrame, read_csv
import pandas 
import sys

print 'Python version ' + sys.version
print 'Pandas version ' + pandas.__version__

df = pandas.read_csv(r'football.csv') 
