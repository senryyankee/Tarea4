import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Lee el archivo

datos = np.loadtxt("room-temperature.csv", delimiter=",", skiprows=1, usecols=[1,2,3,4])

#Transpongo los datos para otros analisis

datost = datos.T


#Normalizo los datos llenando una matriz inicialmente llena de ceros

norm=np.zeros(datos.shape)
for i in range (len(norm)):
	norm[i,:]=(datos[i,:]-np.mean(datos[i,:]))/np.std(datos[i])

normt=norm.T
#Calculo la matriz de covarianza para las 4 variables, para lo que era necesario transponer la matriz de datos

mcov=np.cov(normt)

#obtengo los vectores propios y los valores propios de la matriz de covarianza

valores, vectores = np.linalg.eig(mcov)

print "PC1 es", vectores[:,0]
print "PC2 es", vectores[:,1]

#Calculo las variables en funcion de las componentes principales, se transpone la matriz de vectores para hacer el producto punto y que cada vector corresponda a las variables

dot=np.dot(vectores.T, datost)

#

redot=np.dot(dot, datos)

plt.scatter(redot[0,0],redot[1,0], label="Front left")
plt.scatter(redot[0,1],redot[1,1], label="Front Right", color="green")
plt.scatter(redot[0,2],redot[1,2], label="BackLeft", color="red")
plt.scatter(redot[0,3],redot[1,3], label="BackRight"color="black")
plt.title("Agrupaciones")
plt.xlabel("Datos En El Sistema De La Primera Componente")  
plt.ylabel("Datos En El Sistema De La Segunda Componente")
plt.legend(loc=7, prop={'size':8})
plt.savefig("Agrupaciones.pdf")
plt.close()
