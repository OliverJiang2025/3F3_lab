import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha = 0.5
beta = 0.2

def b(alpha, beta):
    return np.arctan((beta*np.tan(np.pi*alpha/2)))/alpha

def s(alpha, beta):
    return (1+beta**2*(np.tan(np.pi*alpha/2))**2)**(1/(2*alpha))

u = np.random.uniform(-np.pi/2,np.pi/2,1000)

v = -np.log(1-np.random.uniform(0,1,1000))

b = b(alpha, beta)
s = s(alpha, beta)

def x(b,s,u,v):
    temp1 = (s*np.sin(alpha*(u+b)))/((np.cos(u))**(1/alpha))
    temp2 = ((np.cos(u-alpha*(u+b)))/(v))**(1/alpha-1)
    return temp1 * temp2


x = x(b,s,u,v)


plt.figure()
plt.hist(x, bins = 50, density = False)
#plt.xlim(-10000,20000)
plt.show()