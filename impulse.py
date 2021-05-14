import matplotlib.pyplot as plt
import math
import numpy as np

# x = np.ones(20, dtype=int)
# y = np.zeros(20, dtype=int)
# for i in range(len(x)):
#     if i < len(x) // 2:
#         x[i] = 0
# plt.plot(x, y)

x = np.linspace(0, 30, 100)
y = x ** 2
plt.plot(x, y)
plt.show()