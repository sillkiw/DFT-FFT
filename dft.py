'''
Basic implementation of DFT algorithm in Python
X_k = sum(x_n * exp(-j*2*PI*k*n/N))
Reference:
https://en.wikipedia.org/wiki/Discrete_Fourier_transform
'''

__author__ = 'Darko Lukic'
__email__ = 'lukicdarkoo@gmail.com'

import numpy as np
import matplotlib.pyplot as plt




SAMPLE_RATE = 8192
N = 128 # Windowing

x_values = np.arange(0, N, 1)

x = np.sin((2*np.pi*x_values / 32.0)) # 64 - 256Hz
x += np.sin((2*np.pi*x_values / 64.0)) # 64 - 128Hz
X = list()

for k in range(0, N):
	X.append(0+0j)
	for n in range(0, N):
		X[k] += x[n] * np.exp(np.imag(0, -2*np.pi*k*n/N))




# Plotting 
_, plots = plt.subplots(2)

## Plot in time domain
plots[0].plot(x)

## Plot in frequent domain
powers_all = np.abs(np.divide(X, N/2))
powers = powers_all[0:N/2]
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N/2)), N)
plots[1].plot(frequencies, powers)


## Show plots
plt.show()