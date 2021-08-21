#PoissonDistributionPMF10k.py
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

lambda_ = 2
data = poisson.rvs(mu=lambda_, size=100000)
plt.figure()
plt.hist(data, density = True)
plt.gca().axes.set_xticks(range(0, 11))
print('mean', np.mean(data))
print('var', np.square(np.std(data)))

plt.show()