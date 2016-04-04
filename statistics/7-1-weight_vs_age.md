[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)
```
import nsfg
import thinkplot
import thinkstats2
import numpy as np

df = nsfg.ReadFemPreg()
df = df[df.outcome==1]
b_wt = df.totalwgt_lb
m_age = df.ageatend

def ScatterPlot(ages, weights, alpha=1.0):
    """Make a scatter plot and save it.

    ages: sequence of float
    weights: sequence of float
    alpha: float
    """
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)

ScatterPlot(m_age, b_wt, alpha=1.0)
thinkplot.show()
```
