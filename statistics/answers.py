# 02-4 Cohen's D

# Using the variable totalwgt_lb, investigate whether first babies are lighter
# or heavier than other. Compute Cohen's d to quantify the difference between groups.
# How does it compare to the difference in pregnancy length?

import thinkstats2
import nsfg
import numpy as np

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
group1 = live[live.birthord == 1]
group2 = live[live.birthord != 1]
group1 = [1, 2, 3]
group2 = [3, 2, 4]
the_mean = group1.np.mean()

def CohenEffectSize(group1, group2):
    diff = group1.np.mean() - group2.np.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print preg.head()
print type(group1)

cohen_d = CohenEffectSize(group1, group2)

