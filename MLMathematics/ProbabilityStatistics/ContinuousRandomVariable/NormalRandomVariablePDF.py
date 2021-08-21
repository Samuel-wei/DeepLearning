#NormalRandomVariablePDF.py
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn
seaborn.set()

fig, ax = plt.subplots(1,1)
norm_0 = norm(loc= 0, scale = 1)
norm_1 = norm(loc= 1, scale = 2)

x = np.linspace(-10, 10, 1000)
ax.plot(x, norm_0.pdf(x), color='red',lw=5, alpha=0.6, label='loc=0, scale=1')
ax.plot(x, norm_1.pdf(x), color='blue',lw=5, alpha=0.6, label='loc=1, scale=2')
ax.legend(loc='best', frameon=False)

plt.show()