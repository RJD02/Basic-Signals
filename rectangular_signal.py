import matplotlib.pyplot as plt
import numpy as np
# n = int(input('Enter the number of samples: '))
fs = 100
T = 5 # Width of the rectangular pulse
t = np.linspace(-0.5, 0.5, fs // 2)
y = np.arange(fs // 2) % 10 < T
plt.title('Rectangular Pulse width = ' + str(T) + 's')
plt.xlabel('Time')
plt.ylabel('Amplitude')
# plt.plot(t, y)
plt.stem(t, y)