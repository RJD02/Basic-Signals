import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(-50, 50, 41)
y = np.zeros(20, dtype=int)
y = np.append(y, 1)
y = np.append(y, np.zeros(20, dtype=int))
y = y.tolist()
plt.stem(t, y)
plt.plot(t, y)