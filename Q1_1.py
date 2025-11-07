import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

N = 100
num_bins = 30
width = 0.5 # width of ks density function 

def plot_data(N, num_bins, width):
    # plot gaussian data and uniform data with length N
    # in a histogram with bins number of num_bins
    gauss_data = np.random.normal(0, 1, N)
    unif_data = np.random.uniform(1, 0, N)

    gauss_x = np.linspace(-5, 5, N)
    gauss_pdf = stats.norm.pdf(gauss_x, 0, 1)

    unif_x = np.linspace(0, 1, N)
    unif_pdf = np.ones(100)
    
    gauss_ks_density = ksdensity(gauss_x, width=width)


    fig, axs = plt.subplots(2, 2, figsize = (12,6))
 
    
    axs[0,0].set_title("Gaussian Distribution")
    axs[0,0].hist(gauss_data, bins = num_bins, density = True)
    axs[0,0].plot(gauss_x, gauss_pdf, label = 'standard Gaussian distribution')


    axs[0,1].set_title("Uniform Distribution")
    axs[0,1].hist(unif_data, bins = num_bins, density = True)
    axs[0,1].plot(unif_x, unif_pdf, label = 'standard uniform distribution')
    
    axs[1,0].plot(gauss_x, gauss_ks_density(gauss_x))

 



    fig.tight_layout()
    plt.show()



plot_data(N, num_bins, width)