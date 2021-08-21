#GeometryDistributionPMF10k.py
from scipy.stats import geom
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

x = range(1,21)
geom_rv = geom(p=0.5)
geom_rvs = geom_rv.rvs(size=100000)
plt.hist(geom_rvs, bins=20, density=True)
plt.gca().axes.set_xticks(range(1,21))

mean, var, skew, kurt = geom_rv.stats(moments='mvsk')
print('mean={}, var={}'.format(mean, var))

plt.show()
