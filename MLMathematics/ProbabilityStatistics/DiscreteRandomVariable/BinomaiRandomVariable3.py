#BinomailRandomVariable3.py
import numpy as np
from scipy.stats import binom

binom_rv = binom(n=10, p=0.25)
mean, var, skew, kurt = binom_rv.stats(moments='mvsk')

binom_rvs = binom_rv.rvs(size=100000)
E_sim = np.mean(binom_rvs)
S_sim = np.std(binom_rvs)
V_sim = S_sim * S_sim

print('mean={}, var={}'.format(mean,var))
print('E_sim{}, V_sim={}'.format(E_sim,V_sim))
print('E=np={},V=np(1-P)={}'.format(10*0.25,10*0.25*0.75))
