import numpy as np
import matplotlib.pyplot as plt
#Carga de datos

h=np.genfromtxt("pot.dat")

x=[]
f=[]



for i in range (len(h)):
	x.append(h[i][0])
	f.append(h[i][1])

y=np.array(x)
g=np.array(f)


#Algoritmo de central diference

def cd (g,x):
	h= (x[2]-x[1])/2
	df = ((g[1:])-(g[0:-1]))/(2*h)
	dx = x[:-1]
	return(df,dx)

#Derivo el potencial con respecto a la posicion

(ex,ef)=cd(g,x)

plt.plot(ex,ef)
plt.show()
plt.close()
