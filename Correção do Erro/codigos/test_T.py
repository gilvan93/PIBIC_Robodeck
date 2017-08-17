import numpy as np
sample1 = np.array([11.66731173,12.52398073,7.43231323,12.87647848,9.08564523])
sample2 = np.array([ 4.93084723,3.63001298,3.16584573,0.37998802,2.46667998])
# paired sample -> the difference has mean 0
difference = sample1 - sample2
# the t-value is easily computed with numpy
t = (np.mean(difference))/(difference.std(ddof=1)/np.sqrt(len(difference)))
# unfortunately, numpy does not have a build in CDF
# here is a ridiculous work-around integrating by sampling
s = np.random.standard_t(len(difference), size=100000)
p = np.sum(s<t) / float(len(s))
# using a two-sided test
print("There is a {} % probability that the paired samples stem from distributions with the same means.".format(2 * min(p, 1 - p) * 100))