import numpy as np
import matplotlib.pyplot as plt


datos=np.genfromtxt("datos.dat")

x=datos[0,:]

y=datos[1,:]

plt.plot(x,y)
plt.show()
plt.close()
