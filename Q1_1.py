import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plot_ksdensity import ksdensity

N = 1000
num_bins = 50
width = 0.4 # width of ks density function 


def plot_data(N, num_bins, width):
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

    fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2,figsize = (12,6))
  
    ax1.plot(gauss_x, gauss_pdf, 
                     label = 'Theoretical Gaussian Distribution')
    ax1.plot(gauss_x, ks_density(gauss_x),
                     label = 'Kernel density estimate for Gaussian random numbers')
    ax1.set_title("KSD of Gaussian random numbers")
    

    ax2.hist(gauss_data, bins = num_bins, density = True,
                     label = 'random generated Gaussian number')
    ax2.plot(gauss_x, gauss_pdf,
                     label = 'exact Gaussian curve')
    ax2.set_title("Histogram of Gaussian random numbers")
  
    mu = 0.5
    sigma = width
    x = np.linspace(-1,2,N)
    y = np.where(
                (x >= 0) & (x <= 1),  # 条件：x在 [a,b] 内
                1,           # 满足条件：PDF=1/(b-a)
                0                     # 不满足条件：PDF=0
                )
    ax3.plot(x, stats.norm.pdf(x, 0.5, width**(1/2)),
                     label = f'exact Gaussian curve with mean = {mu}, variance = {sigma}')
    ax3.plot(x, ks_density_unif(x),
                     label = 'Kernel density estimate for Uniform random numbers')
    ax3.plot(x,y,'--',
                     label = 'theoretical uniform probability density distribution')
    ax3.set_title('KSD of Uniform random numbers')

    ax4.hist(unif_data, bins = num_bins, density = True,
                     label = 'Uniform random numbers')
    ax4.plot(unif_x, unif_pdf,
                     label = 'exact uniform curve')
    ax4.set_title('Histogram of Uniform random numbers')

    #plt.tight_layout()
    plt.suptitle(f'Comparison of distributions (kernel width = {width})')
    plt.legend()
    plt.show()



plot_data(N, num_bins, width)