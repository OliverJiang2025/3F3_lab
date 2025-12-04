import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

N = 1000
num_bins = 50
width = 0.1 # width of ks density function 


def plot_data(N, num_bins, width, type, kernel):
    # plot gaussian data and uniform data with length N
    # in a histogram with bins number of num_bins
    gauss_data = np.random.normal(0, 1, N)
    unif_data = np.random.uniform(1, 0, N)

    gauss_x = np.linspace(-5, 5, N)
    gauss_pdf = stats.norm.pdf(gauss_x, 0, 1)

    unif_x = np.linspace(0, 1, N)
    unif_pdf = np.ones(N)
    
    ks_density = ksdensity(gauss_data, width=width)
    ks_density_unif = ksdensity(unif_data, width=width)

    plt.figure(figsize = (12,6))
    if type == "Gaussian":
        if kernel:
            plt.plot(gauss_x, gauss_pdf, 
                     label = 'Theoretical Gaussian Distribution')
            plt.plot(gauss_x, ks_density(gauss_x),
                     label = 'Kernel density estimate for Gaussian random numbers')
            plt.title(f"Kernel density estimate with width = {width} for Gaussian random numbers overlaid on exact Gaussian curve")
        else:
            plt.hist(gauss_data, bins = num_bins, density = True,
                     label = 'random generated Gaussian number')
            plt.plot(gauss_x, gauss_pdf,
                     label = 'exact Gaussian curve')
            plt.title("Histogram of Gaussian random numbers overlaid on exact Gaussian curve")
    elif type == "Uniform":
        if kernel:
            mu = 0.5
            sigma = width
            x = np.linspace(-1,2,N)
            y = np.where(
                            (x >= 0) & (x <= 1),  # 条件：x在 [a,b] 内
                            1,           # 满足条件：PDF=1/(b-a)
                            0                     # 不满足条件：PDF=0
                            )
            plt.plot(x, stats.norm.pdf(x, 0.5, width**(1/2)),
                     label = f'exact Gaussian curve with mean = {mu}, variance = {sigma}')
            plt.plot(x, ks_density_unif(x),
                     label = 'Kernel density estimate for Uniform random numbers')
            plt.plot(x,y,'--',
                     label = 'theoretical uniform probability density distribution')
            plt.title(f'Kernel density estimate with width = {width} for uniform random number overlaid on exact Gaussian curve')
        else:
            plt.hist(unif_data, bins = num_bins, density = True,
                     label = 'Uniform random numbers')
            plt.plot(unif_x, unif_pdf,
                     label = 'exact uniform curve')
            plt.title('Histogram of Uniform numbers overlaid on exact uniform curve')

    #plt.tight_layout()
    
    plt.legend()
    plt.show()



plot_data(N, num_bins, width, "Uniform", kernel = True)