import matplotlib.pyplot as plt
import numpy as np

n = int(input('Enter the number of samples: '))
t = np.linspace(0, n, n)
y = np.linspace(0, 1, n)
plt.xlabel('Time')
plt.ylabel('Amplitude')
# plt.stem(t, y)
plt.plot(t, y)
