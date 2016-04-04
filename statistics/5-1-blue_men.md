[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

ht_min = 2.54 * (5*12 + 10)
ht_max = 2.54 * (6*12 + 1)

low = dist.cdf(ht_min)
high = dist.cdf(ht_max)

print 'The fraction of the male pop that is less than or equal to 5\'10" is %s' % low
print 'The fraction of the male pop that is less than or equal to 6\'1" is %s' % high
print 'The fraction of the male pop that can be in Blue Man Group is %s' % (high-low)
```
