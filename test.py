from scipy import stats
import numpy as np

a= stats.poisson.rvs(mu= 10, size=10000)
b = np.random.poisson(lam=10, size=1000)
#b = np.random.normal(10, 2, 10000)
k, p = stats.kstest(a, b)
print(p)