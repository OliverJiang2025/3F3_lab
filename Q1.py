import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from plot_ksdensity import *

N = 0
num_bins = 0

def plot_data(N, num_bins):
    # plot gaussian data and uniform data with length N
    # in a histogram with bins number of num_bins
    guassian_data = np.random.normal(0, 1, N)
    unif_data = np.random.uniform(0, 1, N)

