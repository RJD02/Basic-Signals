# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:49:21 2021

@author: Dulange
"""

import matplotlib.pyplot as plt
import numpy as np

n = int(input('Enter the value of n: '))
t = np.linspace(0, n - 1, n)
y = np.ones(n, dtype=int)
plt.plot(t, y)
plt.stem(t, y)