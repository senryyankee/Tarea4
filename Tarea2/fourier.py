import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.fftpack import fft, fftfreq
from numpy import pi
import scipy.io.wavfile

#Lee el Archivo de C y de G

rateC, dataC = scipy.io.wavfile.read('Do.wav')

rateG, dataG = scipy.io.wavfile.read('Sol.wav')

#La estructura de las transformadas de fourier fue tomada y basada no de forma literal de http://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/ y tambien del GitHub del curso 

#Esta forma de entenderlo se hace como un producto punto entre la matriz de transformacion y el vector a transformar, la matriz se define y el producto punto dicta la transformada 

def DFT(x):
	x = np.asarray(x, dtype=float)
	N = len(x)
	n = np.arange(N)
	k = np.reshape((N, 1))
	#Matriz de transformacion
	M = np.exp(-2j * np.pi * k * n / N)
	return np.dot(M, x)

#Uso el metodo de numpy por falta de memoria en mi computador no transforma con el metodo de arreglos
DoTrans=np.fft.fft(dataC)
SolTrans=np.fft.fft(dataG)


#Para obtener las freuencias multiplico los datos trasformados por la frecuencia de muestreo

#Frecuencias de Do
FreqC=np.zeros(len(dataC))

for i in range(len(dataC)):
	FreqC[i]=DoTrans[i]*rateC
#Frecuencias de Sol
FreqG=np.zeros(len(dataG))

for i in range(len(dataC)):
	FreqG[i]=SolTrans[i]*rateG

#Elimina la frecuencia de mayor amplitud

def filtro1(frec):
	ampmax=np.amax(frec)
	for i in range(len(frec)):
		if (frec[i] == ampmax):
			frec[i]=0
	return frec		
#Elimina las frecuencias mayores a 1000

def filtro2(frec):
	for i in range(len(frec)):
		if (frec[i]>1000):
			frec[i]=0
	return frec
#Grafico los datos originales y los filtrados
fig, textures=plt.subplots(3,1)
#Defino x y los datos filtrados
x = np.linspace(0.0,1.0,len(FreqC))
c1=filtro1(FreqC)
c2=filtro2(FreqC)
#Grafico
textures[0].plot(x, dataC)
textures[1].plot(x, c1)
textures[2].plot(x, c2)
plt.savefig("DoFiltros.pdf")
plt.close()

#Creo un archivo con Do diferente

scipy.io.wavfile.write("DoSol.wav",rateG, dataC)

#Comparo y grafico
rateCG, dataCG = scipy.io.wavfile.read('DoSol.wav')

fig, textures=plt.subplots(2,1)
t = np.linspace(0.0,1.0,len(SolTrans))
h = np.linspace(0.0,1.0,len(dataCG))
textures[0].plot(t, SolTrans)
textures[1].plot(h, dataCG)
plt.savefig("DoSol.pdf")
plt.close()

#Creo los ultimos archivos de audio

scipy.io.wavfile.write("Do_pico.wav",rateC, c1)
scipy.io.wavfile.write("Do_pasabajos.wav",rateC, c2)







