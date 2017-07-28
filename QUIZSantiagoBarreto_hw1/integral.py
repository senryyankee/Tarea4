import numpy as np

#Defino el seno

def f(x):
	return np.sin(x)

#Defino el numero de intervalos N

n=10000

#Creo 10000 numeros diferentres dentro del intervalo 

b = np.pi
a = 0

x=np.random.rand(n) * (b - a)

#Segun la definicion se puede decir que la integral es el promedio de la funcion evaluada en todos los valores multiplicado por el intervalo

y=f(x)
integral=0
for i in range (20):

	integral += np.average(y) * (b - a)

print "El valor de la integral es", (integral/20)
