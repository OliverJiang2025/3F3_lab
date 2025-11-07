import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
inverse CDF of exponential distribution with mean m is:
-ln(1-x)
"""

x_data = np.random.uniform(0,1,1000)
y_data = -np.log(1-x_data)

y = np.linspace(0,5,1000)
exp_theoretical = np.e**(-y)

fig, axs = plt.subplots(1,2,figsize = (12,6))

axs[0].hist(y_data, density = "True")
axs[0].plot(y, exp_theoretical)

plt.show()