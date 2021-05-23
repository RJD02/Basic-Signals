import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-5, 5, 500)
y = 4 * np.sinc(np.multiply(t, 4))
plt.title('Sinc Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.plot(t, y)
# plt.stem(t, y)