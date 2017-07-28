import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

#defino la funcion a trabajar

def fun(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
	r = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10
	return r**3

#Defino los limites de integracion en los que voy a generar los numeros, entre 2 y 0
a = 0.0
b = 2.0

#Defino la cantidad de numeros que voy a generar

n=100000

#Genero N numeros para cada dimension dentro del intervalo. Esta forma de generar los valores aleatorios fue tomada del ipython notebook que se encuentra en el github de la clase https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/notes/09.Numerical_Integration-Differentiation/integration.ipynb

rx1 = np.random.rand(n) * (b-a) 
rx2 = np.random.rand(n) * (b-a)
rx3 = np.random.rand(n) * (b-a) 
rx4 = np.random.rand(n) * (b-a) 
rx5 = np.random.rand(n) * (b-a)
rx6 = np.random.rand(n) * (b-a) 
rx7 = np.random.rand(n) * (b-a) 
rx8 = np.random.rand(n) * (b-a) 
rx9 = np.random.rand(n) * (b-a) 
rx10 = np.random.rand(n) * (b-a)

#Nombro una variable como mi funcion evaluada en los puntos aleatorios que genere, por comodidad

f = fun(rx1,rx2,rx3,rx4,rx5,rx6,rx7,rx8,rx9,rx10)

#Tomo la formula del landau 6.50, donde se define que la integral se puede aproximar al promedio del valor de la funcion multiplicado por los intervalos en los que se integra, en este caso, entre 0 y 2 10 veces, y hago que se haga 20 veces diferentes. El promedio es la respuesta.

integral=0
for i in range(20):
	integral  += np.average(f) * ((b - a)**10)


print integral/20

#Variando el numero de numeros aleatorios

x = list(range(1,4097))
d=[]
integral1=0
"""
for i in range (len(x)):
	n= 2*i
	rx1 = np.random.rand(n) * (b-a) 
	rx2 = np.random.rand(n) * (b-a)
	rx3 = np.random.rand(n) * (b-a) 
	rx4 = np.random.rand(n) * (b-a) 
	rx5 = np.random.rand(n) * (b-a)
	rx6 = np.random.rand(n) * (b-a) 
	rx7 = np.random.rand(n) * (b-a) 
	rx8 = np.random.rand(n) * (b-a) 
	rx9 = np.random.rand(n) * (b-a) 
	rx10 = np.random.rand(n) * (b-a)
	f = fun(rx1,rx2,rx3,rx4,rx5,rx6,rx7,rx8,rx9,rx10)
	integral1  = np.average(f) * ((b - a)**10)

	d.append(integral1)
"""

plt.plot(x,d)
plt.savefig("num_integral.pdf")
plt.close()
#valor analitico
ana=1126400

plt.plot(escala, error)
plt.savefig("err_integral.pdf")






