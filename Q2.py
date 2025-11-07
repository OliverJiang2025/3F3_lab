import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 2
b = 3
num_bin = 50
N = 1000

x_data = np.random.normal(0, 1, N)
y_data = a * x_data + b
g_data = x_data**2

x = np.linspace(-5,5,N)
x_theoretical = stats.norm.pdf(x, 0, 1)

y = np.linspace(b-5*a,b+5*a,N)
y_theoretical = stats.norm.pdf(y, b, a)

g = np.linspace(0,10,N)
g_theoretical = np.e**(-g/2)/(np.sqrt(2*np.pi*g))


fig, axs = plt.subplots(1,3,figsize=(15,6))

axs[0].hist(x_data, bins = num_bin, density = True)
axs[0].plot(x, x_theoretical, linestyle = '--')
axs[0].axvline(0, color = 'red', linestyle = '--')
axs[0].set_title('Standard Gaussian Distribution, x')

axs[1].hist(y_data, bins = num_bin, density = True)
axs[1].plot(y, y_theoretical, linestyle = '--')
axs[1].axvline(b, color = 'red', linestyle = '--')
axs[1].set_title(f'Distribution of ax+b in which a = {a}, b = {b}')

axs[2].hist(g_data, bins = num_bin, density = True)
axs[2].plot(g, g_theoretical, linestyle = '--')
axs[2].set_ylim(0,2)
axs[2].set_title('Distribution of x^2')

plt.show()