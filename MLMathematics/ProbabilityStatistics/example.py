from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

norm_rv = norm(loc=0, scale=1)
x = np.linspace(0, 2, 1000)

sample_n = 100
x_array = []
for i in range(1000000):
    norm_rvs = norm_rv.rvs(size=sample_n)
    x_bar = sum(norm_rvs) / float(sample_n)
    s = sum(np.square((norm_rvs - x_bar))) / float(sample_n-1)
    s_array.append(s)

print(np.mean(s_array))
plt.hist(x_array, bins=100, normed=True, alpha=0.6)
plt.axvline(0, ymax=0.8, color='r')
plt.gca().axes.set_xlim(-0.4, 0.4)
plt.show()