[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> REPLACE THIS TEXT WITH YOUR RESPONSE
```
# Question 2, Chapter 3, Exercise 1
# Make a PMF of numkdhh, the number of children under 18 in the respondent's household

import thinkstats2 
import chap01soln
import thinkplot
resp = chap01soln.ReadFemResp()

numkdhh = resp.numkdhh
pmf = thinkstats2.Pmf(numkdhh)

thinkplot.Pmf(pmf, label='numkdhh')
print numkdhh.head()

# Define BiasPmf

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)
 
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

# Make a biased Pmf of children in the household, as observed if you surveyed the children instead of respondents

biased = BiasPmf(pmf, label = 'biased')

# Display the Pmf and the biased Pmf on same axis

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

# Compute the means of the two Pmfs

print 'The pmf mean is %s' % pmf.Mean()

print 'The biased pmf mean is %s' % biased.Mean()
```

