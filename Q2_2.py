import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N = 1000
x_data = np.random.uniform(0, 2*np.pi, N)
y_data = np.sin(x_data)


idx = np.linspace(-1, 1, N)
theoretical = 1/(np.pi * np.sqrt(1 - idx**2))

plt.hist(y_data, bins=50, density=True, label='histogram of $y=sin(x)$')
plt.plot(idx, theoretical, linestyle='--', label='Theoretical PDF')
plt.xlabel('y = sin(x)')
plt.ylabel('Density')
plt.title('Histogram of y=sin(x) and Theoretical PDF')
plt.legend()
plt.show()