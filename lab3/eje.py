import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import expon
from scipy.stats import norm


n=[]
n=np.random.exponential(0.1,1000)
#(a,b)=expon.fit(n)
#plt.hist(n, normed=True, bins=200)

#print a,b

x=np.linspace(0,1,2000)
#y=expon.pdf(x,a,b)
#plt.plot(x,y)


arr=[]

for i in range (1,1000):
	arr.append(sum(np.random.exponential(0.1,1000)))


(a,b)=norm.fit(arr)
y=norm.pdf(x,a,b)

plt.hist(arr, normed=True, bins=200)
plt.plot(x,y)
plt.show()
plt.close()

