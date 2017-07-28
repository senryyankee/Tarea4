import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.fftpack import fft, fftfreq
import scipy.io.wavfile


#Leo el archivo del violin 

rateViolin, dataViolin = scipy.io.wavfile.read('violin.wav')

#Aplico la transformada de fourier a los datos

ViolinTrans=np.fft.fft(dataViolin)
inverrate=(1.0/rateViolin)
#Hallo las frecuencias 

freqViolin=np.fft.fftfreq(dataViolin.size, inverrate)
print freqViolin
#Elimino las frecuencias mayores que 2000 hz y menores que 1000 hz
def filtro(freq):
	for i in range(0,len(freq)):
		if (freq[i]<1000):
			np.delete(freq, i)
		if (freq[i]>2000):
			np.delete(freq, i)		
	return freq

#Grafico los datos, definiendo un espacio en el que grafico

x=np.linspace(0, 1, len(ViolinTrans))

plt.plot(x, np.abs(ViolinTrans))
plt.savefig('Violin.pdf')
plt.close()

#Aplico la funcion fitlro a las frecuencias
 
freqFilt=filtro(freqViolin)

#Recupero la senal



#Grafico la senal con y sin el filtro

fig, textures=plt.subplots(2,1)
textures[0].plot(x, np.abs(dataViolin))
textures[1].plot(x, freqFilt)
plt.savefig('ViolinFiltro.pdf')
plt.close()




















