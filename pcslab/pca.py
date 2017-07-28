import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random


x=np.loadtxt("food-texture.csv", delimiter=",", skiprows=1, usecols=[1,2,3,4,5])


z=np.zeros(x.shape)
"""
for i in range(len(z)):
	z[i]= (x[i]-np.std(x))/

fig, textures=plt.subplots(5,1)


textures[0].hist(x[:,0])
textures[1].hist(x[:,1])
textures[2].hist(x[:,2])
textures[3].hist(x[:,3])
textures[4].hist(x[:,4])
"""



c=np.cov(x)

h=x.T


"""
for i in range (len(h)):
	h[i]=(h[i]-c[i])/
"""


plt.scatter(h[0],h[1])
plt.show()
plt.close()


print h
