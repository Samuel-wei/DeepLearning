# Copyright sharebee.cn INC All rights reserved
# Author: Samuel
# Reference: https://gitbook.cn/gitchat/column/5d9efd3feb954a204f3ab13d/topic/5da00eaceb954a204f3ad045

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import seaborn
seaborn.set()

params = [0.25, 1, 10]
x = np.linspace(0, 1, 100)
f, ax = plt.subplots(len(params), len(parms), sharex=True, sharey=True)

for i in range(len(params)):
    for j in range(len(params)):
        a = params[i]
        b = params[j]
        y = beta(a, b).pdf(x)
        ax[i, j].plaot(x, y, color='red')
        ax[i, j].set_title('`$\\alpha$={},$\\beta={}$`'.format(a,b))
        ax[i, j].set_ylim(0, 10)

ax[0, 0].set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax[0, 0].set_yticks([0, 2.5, 5, 7.5, 10])
ax[1, 0].set_ylabel('`$p(\\theta)$`')
ax[2, 1].set_xlabel('`$\\theta$`')
plt.show()

