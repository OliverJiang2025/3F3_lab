import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

"""
theoretical mean and sd for the histogram count
data as a function of N
"""

N_list = [100, 1000, 10000]
bin_num = 20


def paramater(N, bin_num):
    p_j = 1/bin_num
    return N*p_j, np.sqrt(N * p_j * (1 - p_j))


def plot_data(N):
    x = np.random.uniform(1, 0, N)
    pdf = np.ones(N)
    return x, pdf



fig, axs = plt.subplots(1, 3, figsize = (12,6))

for i in range(len(N_list)):
    n = N_list[i]
    unif_data, pdf = plot_data(n)
    axs[i].hist(unif_data, bins = bin_num)
    mu, sd = paramater(n, bin_num)
    axs[i].plot(unif_data, mu*np.ones(n))
    axs[i].plot(unif_data, (mu+3*sd)*np.ones(n))
    axs[i].plot(unif_data, (mu-3*sd)*np.ones(n))

plt.show()
        




