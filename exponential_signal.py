import matplotlib.pyplot as plt
import numpy as np

n = int(input('Enter the n value'))
t = np.linspace(0, n, n)
a = float(input('Enter the a value'))
z = np.multiply(t, a)
y = np.exp(z)
plt.xlabel('Time')
plt.ylabel('Amplitude')
# plt.stem(t, y);
plt.plot(t, y)
#n = 20, a = 0.2