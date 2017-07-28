import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Cargo el archivo, tomando solamente los datos que interesan y tengo un arreglo de cada variable
datos = np.array(pd.read_csv('../SantiagoBarreto_hw2/DatosBancoMundial5.csv', skiprows=0, usecols=np.arange(4, 227)))
datost=datos.T

#Normalizo los datos llenando una matriz inicialmente llena de ceros

norm=np.zeros(datos.shape)
for i in range (len(norm)):
	norm[i,:]=(datos[i,:]-np.mean(datos[i,:]))/np.std(datos[i])

#Grafico los datos normalizados, definiendo el espacio en el que se va a graficar, tomado del codigo trabajado en el laboratorio

fig, textures=plt.subplots(5,1)
x = np.linspace(0.0,1,len(datost))

textures[0].plot(x, norm[0])
textures[1].plot(x, norm[1], color="Green")
textures[2].plot(x, norm[2], color="Red")
textures[3].plot(x, norm[3], color="Black")
textures[4].plot(x, norm[4], color="Brown")

plt.savefig("ExploracionDatos.pdf")
plt.close()

#Calculo la matriz de covarianza:

mcov=np.zeros((5,5))
M=len(norm[0,:])
for i in range (0,5):
	for j in range (0,5):
		mcov[i,j] = sum((norm[i,:] - norm[i,:].mean())*(norm[j,:]- norm[j,:].mean())) / (M-1)

#Calculo componentes principales con sus valores e imprimo los mensajes

#va son los valores, y ve son los vectores

va, ve = np.linalg.eig(mcov)

print "La primera componente principal es", ve[:,0]
print "La segunda componente principal es", ve[:,1]


#Calculo las variables en funcion de las componentes principales, se transpone la matriz de vectores para 

f=np.dot(ve.T, norm)

plt.scatter(f[0,:],f[1,:])
plt.title("Primera Componente vs Segunda Componente")
plt.xlabel("Datos En El Sistema De La Primera Componente")  
plt.ylabel("Datos En El Sistema De La Segunda Componente")
plt.savefig("PCAdatos.pdf")
plt.close()

#Hacer una grafica donde se puedan ver las agrupaciones de las variables originales en el sistema de referencia de los dos componentes principales.

g=np.dot(f, norm.T)

plt.title("Agrupaciones de las variables originales")

plt.scatter(g[0,0],g[1,0], label="Total tax rate (% of commercial profits)")
plt.scatter(g[0,1],g[1,1], label="Cost of business start-up procedures (% of GNI per capita)", color="Red")
plt.scatter(g[0,2],g[1,2], label="Unemployment, female (% of female labor force) (modeled ILO estimate)", color="Yellow")
plt.scatter(g[0,3],g[1,3], label="Unemployment, male (% of male labor force) (modeled ILO estimate)", color="Green")
plt.scatter(g[0,4],g[1,4], label="Ratio of female to male labor force participation rate (%) (modeled ILO estimate)", color="Brown")
plt.legend(loc=7, prop={'size':8})
plt.savefig("PCAvariables.pdf")
plt.close()

print "Las variables que estan correlacionadas son", "Total tax rate y Cost of business start-up procedures", "Tambien esta correlacionado el desempleo de hombre con el desempleo de mujeres", "Ratio of female to male labor force participation rate no esta correlacionada con ninguna otra variable" 









