# Q5 code

# Extract emails into a csv file
print 40 * '*'
df['email'].to_csv('emails.csv',sep=',', index = False, encoding='utf-8')
print 'Answer printed to emails.csv'


