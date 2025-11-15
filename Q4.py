import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha = 1.5 # alpha in (0,2)/{1}
beta = 0    # beta in [-1,1]
N = 100000

def generate_x(alpha, beta, N):
    def b(alpha, beta):
        temp1 = beta*np.tan(np.pi*alpha/2)
        temp2 = np.arctan(temp1)
        return temp2/alpha

    def s(alpha, beta):
        temp1 = beta*np.tan(np.pi*alpha/2)
        temp2 = 1 + temp1**2
        temp3 = 1/(2*alpha)
        return temp2**(temp3)

    u = np.random.uniform(-np.pi/2,np.pi/2,N)

    v = -np.log(1-np.random.uniform(0,1,N))

    b = b(alpha, beta)
    s = s(alpha, beta)

    def x(b,s,u,v):
        temp1 = np.sin(alpha*(u + b))
        temp2 = (np.cos(u))**(1/alpha)
        temp3 = np.cos(u - alpha*(u + b))/v
        temp4 = (1-alpha)/alpha
        return s*temp1/temp2*(temp3**temp4)
    return x(b,s,u,v)

fig, axs = plt.subplots(2,5,figsize = (15,6))

for i in range(2):
    if i == 0:
        alpha = 0.5
    elif i == 1:
        alpha = 1.5
    for j in range(5):
        beta = -1 + j*0.5
        x = generate_x(alpha, beta, N)
        axs[i,j].hist(x, bins = int(np.sqrt(N)), density = True)



plt.show()