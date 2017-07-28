import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as mpimg
from scipy import fftpack
from scipy.signal import convolve2d
from scipy.fftpack import fft, fftfreq


#Lee la imagen 

moon=plt.imread("http://www.scipy-lectures.org/_images/moonlanding.png")

x,y=moon.shape
#Aplica transformada de Fourier a los datos
frec= fftpack.fft2(moon, shape=moon.shape) / np.sqrt(x*y)

#Hace 0 todas las frecuencias menos las 50 ultimas y las primeras y las agrega a un nuevo arreglo de la imagen reconstruida

moonr=np.zeros(moon.shape)

for i in range(len(moon[:,0])):
	for j in range(len(moon[0,:])):
		if (i < 50 and j<50) : 
				moonr[i,j] = 0
		elif (i> len(moon[:,0])-50 and j>len(moon[0,:])):
			moonr[i,j] = 0
		else:
			moonr[i,j]=frec[i,j]

#Calcula el espectro de potencias

EP=np.fft.fftshift(frec)
POT=abs(EP)**2

print EP
#Hace las 4 graficas en una imagen

plt.subplot(221)
plt.title("Original Image")
imgplot = plt.imshow(moon, cmap="gray")

plt.subplot(222)
plt.title("Power Espectrum")
imgplot = plt.imshow(np.log10(POT))

plt.subplot(223)
plt.title("Reconstructed Image")
imgplot = plt.imshow(np.real(moonr), cmap="gray")

plt.subplot(224)
plt.title("Filtered Espectrum")
imgplot = plt.imshow(moon, cmap="gray")

plt.savefig("moon_landing.png")
plt.close()
