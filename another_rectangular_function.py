import matplotlib.pyplot as plt
import numpy as np

def rect_wave(x,c,c0): #Starter is c0, rectangular wave of width c
     if x>=(c+c0):
          r=0.0
     elif x<c0:
          r=0.0
     else:
          r=1
     return r

T = 0.2
x=np.linspace(-2,4,1000)
y=np.array([rect_wave(t,T,-1.0) for t in x])
plt.ylim(-0.2,1.2)
plt.title('Rectangular Pulse Width=' + str(T) + 's')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.plot(x,y)
plt.show()