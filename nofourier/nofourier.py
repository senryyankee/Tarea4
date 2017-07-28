import numpy as np
import matplotlib.pylab as plt
from numpy import fft


m=np.loadtxt('magnitude.dat')
p=np.loadtxt('phase.dat')
f= m * np.exp(1j*p)

im=fft.ifft2(f)

fig = plt.figure(1, figsize=(9.5,9))

plt.imshow(np.real(im), cmap='gray')
plt.savefig('secret.jpg')

plt.show()
plt.close()
