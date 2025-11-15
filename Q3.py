import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity
"""
inverse CDF of exponential distribution with mean m is:
-ln(1-x)
"""
bin_num = 30
width = 0.3
x_data = np.random.uniform(0,1,1000)
y_data = -np.log(1-x_data)

y = np.linspace(0,5,1000)
exp_theoretical = np.e**(-y)

ks_density = ksdensity(y_data, width=width)



fig, axs = plt.subplots(1,2,figsize = (15,6))

axs[0].hist(y_data, bins = bin_num, density = "True", label = 'Random Generated Data')
axs[0].plot(y, exp_theoretical, '--', label = 'Theoretical Distribution')   
axs[0].set_title('Histogram of random generated data from y = -ln(1-x)')
axs[0].legend()

axs[1].plot(y, ks_density(y), color = 'blue', label = 'Kernel Density Estimate')
axs[1].plot(y, exp_theoretical, '--', color = 'orange', label = 'Theoretical Distribution')
axs[1].set_title(f'Kernel Density Estimate of random generated data with width = {width}')

plt.legend()
plt.show()