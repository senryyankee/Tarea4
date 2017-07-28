import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#Lee el archivo

datos = np.loadtxt("room-temperature.csv", delimiter=",", skiprows=1, usecols=[1,2,3,4])
datost = datos.T

#Genera las graficas 
fig, textures=plt.subplots(4,1)

#Define el spacio a graficar 
x = np.linspace(0.0,1,len(datos))

#inicializo y lleno la matriz que sera la normalizada
z=np.zeros(datost.shape)

for i in range (len(z)):
	z[i]=(datost[i]-np.mean(datost[i]))/np.std(datost[i])

#Defino a graficar los datos NO normalizados
textures[0].plot(x, datost[0])
textures[1].plot(x, datost[1])
textures[2].plot(x, datost[2])
textures[3].plot(x, datost[3])

plt.savefig("temp.png")
plt.show()
plt.close()

#Calculo y muestro la matriz de covarianza
mcova = np.cov(datost)

print mcova

#Calculo componentes principales con sus valores e imprimo los mensajes

va, ve = np.linalg.eig(mcova)

print "La primera componente principal es", ve[:,0], "con valor", va[0]
print "La segunda componente principal es", ve[:,1], "con valor", va[1]

#Sumo los valores y calculo los porcentajes respectivos a las componentes

tvalores=sum(va)

com1=(va[0]/tvalores)*100
com2=(va[1]/tvalores)*100

print "La primera componente principal explica el",com1,"\% de la varianza."
print "La segunda componente principal explica el",com2,"\% de la varianza."


#Defino el espacio en el que voy a graficar el vector

vectorx= np.linspace(-3.0,3.0, len(z))

#Hago la grafica de Front Riight vs Front Left

plt.title("Front Right vs Front Left")
plt.xlabel("Front Right")  
plt.ylabel("Front Left")
plt.scatter(z[1],z[0])
plt.plot(vectorx, vectorx*ve[1,0]/ve[0,0], label="Primera Componente")
plt.plot(vectorx, vectorx*ve[1,1]/ve[0,1], label="Segunda Componente")
plt.legend(loc="upper left")
plt.savefig("pca_fr_fl.pdf")
plt.show()
plt.close()

#Hago la grafica de Back Left vs Front Left

plt.title("Back Left vs Front Left")
plt.xlabel("Back Left")  
plt.ylabel("Front Left")
plt.scatter(z[2],z[0])
plt.plot(vectorx, vectorx*ve[1,0]/ve[0,0], label="Primera Componente")
plt.plot(vectorx, vectorx*ve[1,1]/ve[0,1], label="Segunda Componente")
plt.legend(loc="upper left")
plt.savefig("pca_bl_fl.pdf")
plt.show()
plt.close()














