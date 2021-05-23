# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:49:21 2021

@author: Dulange
"""

import matplotlib.pyplot as plt
import numpy as np

n = int(input('Enter the value of n: '))
t = np.linspace(-n, n - 1, 2 * n)
# y = np.ones(2 * n, dtype=int)
y = np.zeros(n, dtype=int);
y = np.append(y, np.ones(n, dtype=int))
plt.xlabel('Time');
plt.ylabel('Amplitude')
plt.plot(t, y)
plt.stem(t, y)