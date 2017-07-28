import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Valores

k=42.0

g=9.8

mu=0.15

m=0.25

x_0=0.2

xprime_0=0.0

x2prime_0= (-(k/m)*x_0)-(mu*g)

h=0.0001

n_points=1000

t=np.linspace(0,4, n_points)

x0=[x_0]
x1=[xprime_0]
x2=[x2prime_0]


for i in range(n_points):
	x0.append(x0[i-1]+x1[i]*h)
	x1.append(x1[i-1]+x2[i]*h)
	



















