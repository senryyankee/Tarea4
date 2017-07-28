import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import nbinom

#Carga archivo

a=np.loadtxt("datos_CAMINATA.txt")

#Arreglo a llenar

su=[]

r=len(a)
for i in range (r):
	su.append(sum(a[i]))

miu,sig =norm.fit(su)
x=np.linspace(3000,4000,1000)
y=norm.pdf(x,miu,sig)


miub= miu/1000

probabilidad= miub/10

print (" La probabilidad de sacar una cara con esta moneda es :",probabilidad)

#Histograma de la primera fila
plt.hist(a[0], normed=True)
plt.savefig("bonomial.png")
plt.close()
#Histograma de la suma de cada fila
plt.plot(x,y)
plt.hist(su, normed=True, bins=200)
plt.savefig("normal.png")
plt.close()


