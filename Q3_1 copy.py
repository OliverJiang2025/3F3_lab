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
Nlist = [100, 200, 500, 1000, 2000, 3000, 5000, 8000, 10000, 20000, 50000, 100000, 200000] # number of samples
M = 100 # number of trials of each set of samples

def inverse_cdf(N, bin_num=bin_num, width=width):
    x_data = np.random.uniform(0,1,N)
    y_data = -np.log(1-x_data)
    mu = 0
    for y in y_data:
        mu += y
    mu = mu / N
    return mu

def MC_MSE(Nlist,M):
    mses = []
    for n in Nlist:
        mus = []
        for i in range(M):
            mu = inverse_cdf(n)
            mus.append(mu)
        mus = np.array(mus)
        mse = np.mean((mus - 1)**2)
        mses.append(mse)
    idx = np.linspace(100,20000)
    plt.plot(Nlist, mses)
    plt.xlabel('Number of samples N')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.title('MSE of Sample Mean vs Number of Samples N')
    plt.xscale('log')
    #plt.plot(idx, 1/np.sqrt(idx) ,'--')
    plt.show()
    



if __name__ == "__main__":
    MC_MSE(Nlist,M)







