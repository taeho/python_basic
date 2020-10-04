# nan.py -*- coding: utf-8 -*- 

import numpy as np

height = np.array([45, 75, 60, 51, np.nan])
print(np.mean(height))
print(np.nanmean(height))

x = np.array([1, -1, 0, np.infty, -np.inf])
# RuntimeWarning: invalid value encountered in true_divide  >>  print(x/0)
print(x/0)
# untimeWarning: invalid value encountered in true_divide >>  print(x/np.Infinity)
print(x/np.Infinity)


