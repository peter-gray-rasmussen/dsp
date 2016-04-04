[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
import numpy as np
import thinkstats2 as th
import thinkplot

# sample = np.random.random_sample(1000,)
sample = np.random.random(1000,)
pmf = th.Pmf(sample)

thinkplot.Pmf(pmf, label='random')
thinkplot.Show()

cdf = th.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Random Number', ylabel='CDF')
```
